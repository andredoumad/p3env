# -*- coding: utf-8 -*-
import os, time, random, smtplib, shutil, imaplib, email, calendar, json
from random import *
import inspect
from time import sleep
from email.message import EmailMessage
import random
import urllib.request, urllib.error, urllib.parse
import codecs
import sys
import unicodedata
import logging
import ftfy
from email_validator import validate_email, EmailNotValidError
import re
import socket
import dns.resolver
#from guerrillamail import GuerrillaMailSession
import subprocess
from subprocess import Popen, PIPE
import verifier as verify_it
from datetime import date
from pathlib import Path


def eventlog(logstring):
    # if str(socket.gethostname()) == "tr3b":
    previous_frame = inspect.currentframe().f_back
    (filename, line_number, 
    function_name, lines, index) = inspect.getframeinfo(previous_frame)
    del previous_frame  # drop the reference to the stack frame to avoid reference cycles
    caller_filepath = filename
    caller_filepath = os.path.abspath(caller_filepath)
    caller_filename = ''
    for ch in caller_filepath:
        if not ch.isalnum():
            caller_filename += str('-')
        else:
            caller_filename += str(ch)
    if len(caller_filename) > 25:
        caller_filename = caller_filename[-25:]
    caller_filename += '_log.txt'
    debug_line_number = line_number
    if line_number < 10:
        debug_line_number = str('0000' + str(line_number))        
    elif line_number < 100:
        debug_line_number = str('000' + str(line_number))
    elif line_number < 1000:
        debug_line_number = str('00' + str(line_number))
    elif line_number < 10000:
        debug_line_number = str('0' + str(line_number))
    print(str(get_hour_minute_second_string()) + ' |==| ' + str(debug_line_number) + ' |==| ' + str(filename)[-25:] + ' | ' + str(function_name) + ' | ' + str(logstring) + ' |==|')

    f = open(str(Path.home()) + '/p3env/eventlog.log', "a")
    f.write(str(get_hour_minute_second_string()) + ' |==| ' + str(debug_line_number) + ' |==| ' + str(filename)[-25:] + ' | ' + str(function_name) + ' | ' + str(logstring) + ' |==|')
    f.write('\n')
    f.close()
    if os.path.getsize(str(Path.home()) + '/p3env/eventlog.log') > 1000000:
        f = open(str(Path.home()) + '/p3env/eventlog.log', "w")
        f.write('')
        f.close()




class Tools:
    def lineno(self):
        """Returns the current line number in our program."""
        return str(' Line: ' + str(inspect.currentframe().f_back.f_lineno))

    def getListWithoutDuplicates(self, theList):
        from collections import OrderedDict
        return list(dict.fromkeys(theList))

    def get_list_from_file(self, filepath):
        listFromFile = []
        listFromFile.clear()
        working = True
        #with open(path, 'rb') as f:
            #text = f.read()
        with open(str(filepath), 'r', encoding='utf8') as fh:
            while working == True:
                for line in fh:
                    line = ftfy.fix_encoding(str(line))
                    #eventlog('get_list_from_file: ' + str(line.rstrip()))
                    listFromFile.append(line.rstrip())
                working = False
                
        #fh.close()
        return listFromFile

    def create_unique_list_emails_given_two_files(self, job_name, fileA, fileB):

        list_A = self.get_list_from_file(fileA)
        list_B = self.get_list_from_file(fileB)
        new_list = []
        if len(list_A) >= len(list_B):
            for a in list_A:
                searching = True
                found = False
                while searching == True:
                    for b in list_B:
                        if len(b) == len(a):
                            if b == a:
                                found = True
                                searching = False
                    searching = False

                if found == False:
                    new_list.append(a)
                    eventlog('unique: ' + str(a))
        else:
            for b in list_B:
                searching = True
                found = False
                while searching == True:
                    for a in list_A:
                        if len(b) == len(a):
                            if b == a:
                                found = True
                                searching = False
                    searching = False

                if found == False:
                    new_list.append(b)
                    eventlog('unique: ' + str(b))

        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%Y-%m-%d-%H:%M", named_tuple)

        iwrite = open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/unique_emails_' + time_string + '.csv'), 'w+')
        new_list = self.getListWithoutDuplicates(new_list)
        for item in new_list:
            valid, reason = Tools.verify_email(self, str(job_name), str(item))
            if valid == True:
                eventlog('VALID: ' + str(item))
                iwrite.write(str(item))
                iwrite.write(str('\n'))
            else:
                eventlog('ignored: ' + str(item))
        iwrite.close()

    def verify_email(self, job_name, email):
        valid = True
        reason = ''

        if not os.path.exists(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_email_filters.csv')):
            with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_email_filters.csv'), 'a') as f:
                f.write('')
                #f.close

        list_job_email_filters_before_at_filepath = str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_email_filters_before_at.csv'
        if os.path.exists(list_job_email_filters_before_at_filepath):
            pass
        else:
            iwrite = open(list_job_email_filters_before_at_filepath, 'a+')
            # iwrite.write('trigger_key')
            iwrite.write('\n')
            iwrite.close()

        list_job_email_filters = Tools.get_list_from_file(self, list_job_email_filters_before_at_filepath)

        def check_emails(self, thelist, value):
            searching = True
            valid = True
            reason = ''
            while searching == True:
                for item in thelist:
                    if len(item) > 0:
                        #eventlog('checking: ' + str(item))
                        values = value.split('@')
                        try:
                            #eventlog('checking: ' + values[1] + ' for ' + str(item) )
                            if str(values[0]).find(str(item)) != -1:
                                valid = False
                                searching = False
                                reason = str('email before @ ' + str(item))
                                break
                        except:
                            reason = 'exception'
                            valid = False
                            searching = False
                searching = False
            return valid, reason

        valid, reason = check_emails(self, list_job_email_filters, email)


        list_job_email_filters_after_at_filepath = str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_email_filters_after_at.csv'
        if os.path.exists(list_job_email_filters_after_at_filepath):
            pass
        else:
            iwrite = open(list_job_email_filters_after_at_filepath, 'a+')
            # iwrite.write('trigger_key')
            iwrite.write('\n')
            iwrite.close()

        list_job_email_filters = Tools.get_list_from_file(self, str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_email_filters_after_at.csv'))

        def check_emails_after_at(self, thelist, value):
            searching = True
            valid = True
            reason = ''
            while searching == True:
                for item in thelist:
                    if len(item) > 0:
                        #eventlog('checking: ' + str(item))
                        values = value.split('@')
                        try:
                            #eventlog('checking: ' + values[1] + ' for ' + str(item) )
                            if str(values[1]).find(str(item)) != -1:
                                valid = False
                                searching = False
                                reason = str('email after @ ' + str(item))
                                break
                        except:
                            reason = 'exception'
                            valid = False
                            searching = False
                searching = False
            return valid, reason

        if valid == True:
            valid, reason = check_emails_after_at(self, list_job_email_filters, email)

        #eventlog('VALID: ' + str(valid) + ' REASON: ' + str(reason) + ' EMAIL: ' + str(email))
        
        return valid, reason

    def deduplicate_file(self, filepath):
        lines = Tools.get_list_from_file(self, filepath)
        lines = Tools.getListWithoutDuplicates(self, lines)
        iwrite = open(str(filepath), 'w+')
        for item in lines:
            eventlog(str(item))
            iwrite.write(str(item))
            iwrite.write(str('\n'))
        iwrite.close()

    def deduplicate_list(self, thelist):
        lines = thelist
        lines = Tools.getListWithoutDuplicates(self, lines)
        #iwrite = open(str(filepath), 'w+')
        # for item in lines:
            # eventlog('deduplicate list: ' + str(item))
        return lines

    def deduplicate_files_in_folder(self, directorypath):
        b_dp, b_fp, list_dp, list_fp = self.get_list_files_folders_in_path(directorypath)
        if b_fp:
            for file in list_fp:
                eventlog('deduplicating: ' + str(file))
                self.deduplicate_file(file)

    def shuffle_list(self, inputlist):
        for i in range(len(inputlist)):
            swap = randint(0,len(inputlist)-1)
            temp = inputlist[swap]
            inputlist[swap] = inputlist[i]
            inputlist[i] = temp
        return inputlist

    def create_job_search_phrase(self, job_name):
        job_search_phrases = []

        def get_list_from_file(filepath):
            listFromFile = []
            listFromFile.clear()
            working = True
            with open(filepath) as fh:
                #fh = open(filepath)
                while working == True:
                    for line in fh:
                        listFromFile.append(line.rstrip())
                    working = False
                fh.close()
            return listFromFile

        if not os.path.exists(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name)):
            os.mkdir(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name))

        completed_searches_filepath = str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_phrases_complete.csv'
        queued_searches_filepath = str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_phrases.csv'

        if os.path.exists(completed_searches_filepath) and os.path.exists(queued_searches_filepath):
            pass
        else:
            iwrite = open(completed_searches_filepath, 'w')
            # iwrite.write('stringkeeper')
            # iwrite.write('\n')
            iwrite.close()
            iwrite = open(queued_searches_filepath, 'w')
            # iwrite.write('stringkeeper')
            # iwrite.write('\n')
            iwrite.close()


        added_first_phrase = False

        job_search_phrases = get_list_from_file(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_phrases.csv'))
        if len(job_search_phrases) < 1:
            eventlog('job_search_phrases is less than 1: ' )
            job_phrases_filepath = str(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_phrases.csv'))
            
            if job_name.find('_') != -1:
                eventlog('job_name contains underscores: ' + str(job_name))
                s0 = job_name.split('_')
            else:
                eventlog('job_name does not contain underscores: ' + str(job_name))
                s0 = job_name

            search_keys_filepath = str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/search_keys.csv')
            if job_name.find(' ') != -1:
                eventlog('job_name does contain spaces: ' + str(job_name))
                s1 = []
                for text in s0:
                    new_text = text.split()
                    s1.append(new_text)

                for text in s1: 
                    iwrite = open(job_phrases_filepath, 'a+')
                    iwrite.write(str(text))
                    iwrite.write('\n')
                    iwrite.close()
                    iwrite = open(search_keys_filepath, 'a+')
                    iwrite.write(str(text))
                    iwrite.write('\n')
                    iwrite.close()
                # job_search_phrases = s1
            else:
                eventlog('job_name does not contain spaces: ' + str(job_name))
                if type(s0) is not list:
                    iwrite = open(job_phrases_filepath, 'a+')
                    iwrite.write(str(s0))
                    iwrite.write('\n')
                    iwrite.close()
                    iwrite = open(search_keys_filepath, 'a+')
                    iwrite.write(str(s0))
                    iwrite.write('\n')
                    iwrite.close()
                else:
                    all_text = ''
                    for text in s0:
                        iwrite = open(job_phrases_filepath, 'a+')
                        iwrite.write(str(text))
                        iwrite.write('\n')
                        iwrite.close()
                        iwrite = open(search_keys_filepath, 'a+')
                        iwrite.write(str(text))
                        iwrite.write('\n')
                        iwrite.close()
                        all_text += str(text) + ' '
                    iwrite = open(job_phrases_filepath, 'a+')
                    iwrite.write(str(all_text))
                    iwrite.write('\n')
                    iwrite.close()
            added_first_phrase = True
        else:
            eventlog('job_search_phrases is greater than 1: ' )
        


        job_phrases_filepath = str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_phrases.csv')
        job_search_phrases = get_list_from_file(job_phrases_filepath)
        multi_word_phrase = ''

        for phrase in job_search_phrases:
            multi_word_phrase += str(phrase + ' ')

        iwrite = open(job_phrases_filepath, 'w+')
        iwrite.write(str(multi_word_phrase))
        iwrite.write('\n')
        iwrite.close()
        # eventlog('search_phrase: ' + str(search_phrase))
        job_search_phrases = get_list_from_file(job_phrases_filepath)

        search_keys_filepath = str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/search_keys.csv')
        search_keys_dir_path = str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name))
        if not os.path.exists(search_keys_dir_path):
            os.mkdir(search_keys_dir_path)
        if not os.path.exists(search_keys_filepath):
            with open(search_keys_filepath, 'a+') as f:
                # f.write('dante minuit dolce')
                f.write('\n')
                f.close
        self.search_keys = self.get_list_from_file(search_keys_filepath)

        self.search_phrase_list = []
        self.search_phrase = ''
        self.success = False
        for item in self.search_keys:
            eventlog('search_keys: ' + str(item))
        def append_word_to_search_phrase_list(self):
            appending_word = True

            while appending_word == True:
                shuffled_keys = Tools.shuffle_list(self, self.search_keys)
                for key in shuffled_keys:
                    if self.success == False:
                        eventlog('trying key: ' + str(key))
                        self.duplicate = False
                        eventlog('using key: ' + str(key) )
                        temp_search_phrase = self.search_phrase
                        temp_search_phrase += str(str(key))
                        eventlog('temp_search_phrase: ' + str(temp_search_phrase))

                        completed_searches_filepath = str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_phrases_complete.csv'
                        queued_searches_filepath = str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_phrases.csv'

                        if os.path.exists(completed_searches_filepath) and os.path.exists(queued_searches_filepath):
                            pass
                        else:
                            iwrite = open(completed_searches_filepath, 'a+')
                            # iwrite.write('stringkeeper')
                            iwrite.write('\n')
                            iwrite.close()
                            iwrite = open(queued_searches_filepath, 'a+')
                            # iwrite.write('stringkeeper')
                            iwrite.write('\n')
                            iwrite.close()

                        completed_searches = self.get_list_from_file(completed_searches_filepath)
                        queued_searches = self.get_list_from_file(queued_searches_filepath)

                        all_searches = completed_searches + queued_searches
                        searching = True
                        found = False
                        while searching == True:
                            for complete in all_searches:
                                if len(temp_search_phrase) == len(complete):
                                    if temp_search_phrase == complete:
                                        found = True
                                        searching = False
                                        break
                            searching = False
                        if found == False:
                            if len(temp_search_phrase) < 500 and len(temp_search_phrase) > 15:
                                eventlog('success search_phrase: ' + str(temp_search_phrase))
                                self.search_phrase_list.append(str(key))
                                self.search_phrase += str(str(key) + ' ')
                                self.success = True
                                appending_word = False
                            else:
                                self.search_phrase += str(str(key) + ' ')
                        else:
                            self.search_phrase += str(str(key) + ' ')

        if added_first_phrase == False:
            append_word_to_search_phrase_list(self)

            if self.success == True:
                iwrite = open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_phrases.csv'), 'a+')
                iwrite.write(str(self.search_phrase))
                iwrite.write(str('\n'))
                iwrite.close()
                eventlog('appended search_phrase: ' + str(self.search_phrase))

    def verify_hyperlink(self, url, job_name):
        valid = True

        if len(url) < 11:
            valid = False

        if valid == True:
            hyperlink_trigger_keys = Tools.get_list_from_file(self, str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/hyperlink_trigger_keys.csv')
            hyperlink_ignore_keys = Tools.get_list_from_file(self, str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/hyperlink_ignore_keys.csv')
            '''
            searching = True
            good = False
            while searching == True:
                for trigger in hyperlink_trigger_keys:
                    if len(trigger) > 0:
                        if str(url).find(str(trigger)) != -1:
                            good = True
                            searching = False
                searching = False
            '''

            hyperlink_ignore_keys.append('duckduck')
            hyperlink_ignore_keys.append('donttrack.us')
            hyperlink_ignore_keys.append('spreadprivacy')

            searching = True
            while searching == True:
                for trigger in hyperlink_ignore_keys:
                    if len(trigger) > 0:
                        if str(url).find(str(trigger)) != -1:
                            valid = False
                            searching = False
                            break
                searching = False


        return valid

    def write_list(self, filepath, thelist):
        with open(str(filepath), 'w+') as iwrite:
            for item in thelist:
                iwrite.write(str(item))
                iwrite.write(str('\n'))
            iwrite.close()

    def file_shuffle(self, filepath):
        thelist = Tools.get_list_from_file(self, filepath)
        thelist = Tools.shuffle_list(self, thelist)
        Tools.write_list(self, filepath, thelist)

    def move_file(self, filepath_source, filepath_destination):
        shutil.move(str(filepath_source), filepath_destination)

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/get_list_files_folders_in_path.history', prefix='get_list_files_folders_in_path', depth=1)
    def get_list_files_folders_in_path(self, path):
        self.list_fp = []
        self.list_dp = []
        self.b_fp = False
        self.b_dp = False
        for i in os.scandir(path):
            if i.is_file():
                #eventlog('File: ' + i.path)
                self.list_fp.append(i.path)
                self.b_fp = True
            elif i.is_dir():
                #eventlog('Folder: ' + i.path)
                self.list_dp.append(i.path + '/')
                self.b_dp = True
        return self.b_dp, self.b_fp, self.list_dp, self.list_fp

    def find_between(self, s, first, last ):
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return ''

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='getListFromFile', depth=1)
    def harvest_email_heap_full_using_csv_triggers_filters(self, job_name):
        file_named_tuple = time.localtime() # get struct_time
        file_time_string = str(time.strftime("%Y-%m-%d-%H-%M-%S", file_named_tuple))
        today_ymd = str(time.strftime("%Y-%m-%d", file_named_tuple))
        eventlog('todays date: ' + str(today_ymd))
        
        self.records = []
        emails = []
        self.completed_emails = []
        self.hyperlink_trigger_keys = Tools.get_list_from_file(self, str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/hyperlink_trigger_keys.csv'))
        self.hyperlink_ignore_keys = Tools.get_list_from_file(self, str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/hyperlink_ignore_keys.csv'))
        self.description_trigger_keys = Tools.get_list_from_file(self, str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/description_trigger_keys.csv'))
        self.description_ignore_keys = Tools.get_list_from_file(self, str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/description_ignore_keys.csv'))
        self.irrelavant_words_for_email_parsing = Tools.get_list_from_file(self, str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/irrelavant_words_for_email_parsing.csv'))



        #find all of the email heap full files inside of the  /home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/daily folder
        self.b_dp, self.b_fp, self.list_dp, self.list_fp = Tools.get_list_files_folders_in_path(self, str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + str('/harvest/contacts/emails/daily/')))

        if self.b_fp == False:
            eventlog('NO FILES FOUND IN: ' + str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + str('/harvest/contacts/emails/daily/')))


        for file in self.list_fp:
            eventlog('files found: ' + str(file))

        list_email_heap_filepaths = []
        b_found_email_heap_full = False
        for filepath in self.list_fp:
            if filepath.find('email_heap_full') != -1:
                #ignore any files created today -- just work with previous results.
                if filepath.find(str(today_ymd)) == -1:
                    list_email_heap_filepaths.append(filepath)
                    b_found_email_heap_full = True
                else:
                    eventlog('skipping ' + str(filepath))
                    sleep(2)


        if b_found_email_heap_full == False:
            eventlog('did not find email heap for processing')
        else:
            eventlog('found email heap for processing')
            with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_report_incomplete.csv'), 'a') as iwrite:
                iwrite.write(str('email,url,description,timestamp'))
                iwrite.write(str('\n'))
                iwrite.close()

            with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_final_report_included.csv'), 'a') as iwrite:
                iwrite.write(str('email,url,description,timestamp'))
                iwrite.write(str('\n'))
                iwrite.close()

            with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_final_report_ignored.csv'), 'a') as iwrite:
                iwrite.write(str('email,url,description,timestamp'))
                iwrite.write(str('\n'))
                iwrite.close()

            with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_final_invalid_reasons.csv'), 'a') as iwrite:
                iwrite.write(str('reason,email,url,description,timestamp'))
                iwrite.write(str('\n'))
                iwrite.close()

            for file in list_email_heap_filepaths:
                eventlog('list_email_heap_filepaths files found: ' + str(file))

            list_email_heap_full = []

            for file in list_email_heap_filepaths:
                newList = Tools.get_list_from_file(self, file)
                for line in newList:
                    list_email_heap_full.append(str(line))

            for line in list_email_heap_full:
                eventlog('list_email_heap_full lines found: ' + str(line))

            self.list_email_heap_full_length = len(list_email_heap_full)

            self.banned_domains = []
            if not os.path.exists(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/ignored_domains.csv')):
                with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/ignored_domains.csv'), 'a') as f:
                    f.write('\n')
                    f.write('\n')
                    f.close
            else:
                self.banned_domains = Tools.get_list_from_file(self, str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/ignored_domains.csv'))

            def ban_domain(self, url):
                self.domain = ''
                self.domain = str(Tools.find_between(self, url, '//', '/'))
                found = False
                for item in self.banned_domains:
                    if len(str(item)) > 3:
                        if item.find(self.domain) != -1:
                            found = True
                            break

                if found == False:
                    eventlog('IGNORING DOMAIN: ' + str(self.domain))
                    with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/ignored_domains.csv'), 'a') as iwrite:
                        iwrite.write(str(self.domain))
                        iwrite.write(str('\n'))
                        iwrite.close()
                    self.banned_domains.append(str(self.domain))

            def check_url_for_domain_ban(self, url):
                self.domain = ''
                self.domain = str(Tools.find_between(self, url, '//', '/'))
                found = False
                for item in self.banned_domains:
                    if len(str(item)) > 3:
                        if item.find(self.domain) != -1:
                            found = True
                            break
                return found

            def process_record(self, record, recordNumber):
                values = record.split(',')
                email = str(values[0])
                url = str(values[1])
                description = str(values[2])
                harvest = True
                reason = ''
                if harvest == True:
                    searching = True
                    while searching == True:
                        for item in self.description_ignore_keys:
                            if len(item) > 0:
                                if description.lower().find(str(item).lower()) != -1:
                                    harvest = False
                                    eventlog(str(recordNumber) + '/' + str(self.list_email_heap_full_length) + ' | INVALID description | ' + str(item) + ' | ' + str(email) + self.lineno())
                                    reason = str('description contains: ' + str(item))
                                    searching = False

                                    break
                        searching = False

                if harvest == False:
                    ban_domain(self, str(url))

                if harvest == True:
                    searching = True
                    while searching == True:
                        for item in self.hyperlink_ignore_keys:
                            if len(item) > 0:
                                #eventlog('checking: ' + str(item))
                                if url.lower().find(str(item).lower()) != -1:
                                    harvest = False
                                    eventlog( str(recordNumber) + '/' + str(self.list_email_heap_full_length) + ' |  INVALID hyperlink  | ' + str(item) + ' | ' + str(email) + self.lineno())
                                    reason = str('hyperlink contains: ' + str(item))
                                    searching = False
                                    break
                        searching = False

                #harvest = True
                return harvest, reason

            def check_for_duplicate_email(self, item, completed_emails):
                found = False
                searching = True
                while searching == True:
                    for finished_email in self.completed_emails:
                        if len(item) == len(finished_email):
                            if item == finished_email:
                                found = True
                                searching = False
                                break
                    searching = False
                return found

            heap_index = 0
            for item in list_email_heap_full:
                valid = False
                reason = 'none'
                found = check_for_duplicate_email(self, item, self.completed_emails)
                list_record_values = []

                if found == False:
                    list_record_values = item.split(',')
                    url = 'none'
                    try:
                        url = str(list_record_values[2])
                    except:
                        url = 'none'
                    found = check_url_for_domain_ban(self, url)

                if found == True:
                    eventlog('IGNORING: ' + str(url))

                if found == False:
                    email = 'none'
                    duplicate_email_found = False
                    identified_email = False
                    description = ''
                    description_list = []
                    description_max_words = 40
                    wrote_description = False
                    try:
                        email = str(list_record_values[0])
                        identified_email = True
                        searching = True
                        while searching == True:
                            for completed_email in self.completed_emails:
                                if email == completed_email:
                                    duplicate_email_found = True
                                    searching = False
                                    break
                            searching = False
                    except:
                        identified_email = False
                        email = 'none'
                    if duplicate_email_found == False and identified_email == True:
                        search_ahead = int(heap_index + 250)
                        if  search_ahead > len(list_email_heap_full):
                            search_ahead = len(list_email_heap_full)
                        for i in range(heap_index, search_ahead):
                            values = list_email_heap_full[i].split(',')
                            found_new_description = False
                            try:
                                email_in_line = values[0]
                                if len(email) == len(email_in_line):
                                    if email == email_in_line:
                                        found_new_description = True
                            except:
                                pass
                            if found_new_description == True:
                                try:
                                    if len(values[1]) > 3:
                                        description += str(values[1])
                                        description += ' '
                                        wrote_description = True
                                except:
                                    pass

                    identified_description = False
                    #shrink description based on max
                    if wrote_description == True:
                        temp_values = description.split()
                        values = []
                        irrelavant = False
                        for word in temp_values:
                            if len(str(word)) > 3:
                                for irrelavant_word in self.irrelavant_words_for_email_parsing:
                                    if str(word).lower().find(str(irrelavant_word).lower()) != -1:
                                        #eventlog('irrelavant: ' + str(word))
                                        irrelavant = True

                                if irrelavant == False:
                                    values.append(str(word))
                                    identified_description = True

                        #if len(values) > 3:
                            #identified_description = True

                        middle_int = int(len(values) / 2)
                        list_start = middle_int - int(description_max_words / 2)
                        if list_start < 0:
                            list_start = 0
                        #list_end = middle_int + int(description_max_words /2)
                        list_end = middle_int
                        if list_end > len(values):
                            list_end = len(values)
                        new_description = ''
                        for i in range(list_start, list_end):
                            new_description += str(values[i] + ' ')
                        description = new_description


                    named_tuple = time.localtime() # get struct_time
                    time_string = time.strftime("%Y-%m-%d-%H-%M-%S", named_tuple)
                    if duplicate_email_found == False and identified_email == True and identified_description == True:
                        self.record = str(str(email) + ',' + str(url) + ',' + str(description)  + ',' + str(time_string) )
                        valid, reason = Tools.verify_email(self, str(job_name), str(email))
                        if valid == True:
                            harvest, reason = process_record(self, self.record, heap_index)
                            if harvest == True:
                                with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_report_incomplete.csv'), 'a') as iwrite:
                                    self.records.append(self.record)
                                    iwrite.write(str(self.record))
                                    iwrite.write(str('\n'))
                                    iwrite.close()
                            else:
                                with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_final_invalid_reasons.csv'), 'a') as iwrite:
                                    iwrite.write(str(reason) + ',' + self.record)
                                    iwrite.write(str('\n'))
                                    iwrite.close()
                                eventlog(str(heap_index) + '/' + str(self.list_email_heap_full_length) + ' | INVALID  | ' + str(reason) + ' | ' + str(email) + self.lineno())
                        else:
                            with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_final_invalid_reasons.csv'), 'a') as iwrite:
                                iwrite.write(str(reason) + ',' + self.record)
                                iwrite.write(str('\n'))
                                iwrite.close()
                            eventlog(str(heap_index) + '/' + str(self.list_email_heap_full_length) + ' | INVALID  | ' + str(reason) + ' | ' + str(email) + self.lineno())
                        self.completed_emails.append(str(email))
                heap_index += 1
            sleep(1)

            incomplete_list = Tools.get_list_from_file(self, str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_report_incomplete.csv'))
            self.record_number = 0
            for record in incomplete_list:
                if self.record_number != 0:
                    self.found = False
                    self.reason = ''
                    for banned_domain in self.banned_domains:
                        if len(str(banned_domain)) > 3:
                            if str(record).lower().find(str(banned_domain)) != -1:
                                self.found = True
                                eventlog('BANNED DOMAIN: ' + str(banned_domain) + ' MATCHES RECORD: ' + str(record))
                                self.reason = banned_domain
                                break
                    if self.found == False:
                        eventlog('record number: ' + str(self.record_number) + ' Reason: ' + str(self.reason) +  ' INCLUDING: ' + str(record))
                        #str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/outbox'
                        values = record.split(',')
                        with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/contacts/emails/flyers/ahap_introduction/outbox/' + 'outbox_emails.csv'), 'a') as iwrite:
                            iwrite.write(str(values[0]))
                            iwrite.write(str('\n'))
                            iwrite.close()

                        with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_final_report_included.csv'), 'a') as iwrite:
                            iwrite.write(str(record))
                            iwrite.write(str('\n'))
                            iwrite.close()
                    else:
                        eventlog('record number: ' + str(self.record_number) + ' Reason: ' + str(self.reason) +  ' IGNORING: ' + str(record))
                        with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_final_report_ignored.csv'), 'a') as iwrite:
                            iwrite.write(str(record))
                            iwrite.write(str('\n'))
                            iwrite.close()

                self.record_number += 1

            ### move files to /home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/reports
            source = str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_final_invalid_reasons.csv')
            destination = str(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/reports/') + str(file_time_string) + '_email_harvest_final_invalid_reasons.csv')
            Tools.move_file(self, source, destination)
            source = str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_report_incomplete.csv')
            destination = str(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/reports/') + str(file_time_string) + '_email_harvest_report_incomplete.csv')
            Tools.move_file(self, source, destination)
            source = str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_final_report_included.csv')
            destination = str(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/reports/') + str(file_time_string) + '_email_harvest_final_report_included.csv')
            Tools.move_file(self, source, destination)
            source = str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_final_report_ignored.csv')
            destination = str(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/reports/') + str(file_time_string) + '_email_harvest_final_report_ignored.csv')
            Tools.move_file(self, source, destination)


            for filepath in list_email_heap_filepaths:
                ### move full heap to /home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/scanned
                source = str(filepath)
                destination = str(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/contacts/emails/scanned/'))
                Tools.move_file(self, source, destination)

    def remove_commas_between_symbols(self, symbol, replace, target_file):
        rows = tools.get_list_from_file(target_file)
        self.modified_rows = []
        for row in rows:
            self.b_inside_symbol = False
            self.modified_row = ''
            for ch in row:
                if str(ch).find(str(symbol)) != -1:
                    if self.b_inside_symbol == False:
                        self.b_inside_symbol = True
                    else:
                        self.b_inside_symbol = False

                if self.b_inside_symbol == False:
                    self.modified_row += str(ch)
                elif self.b_inside_symbol == True:
                    if ch.find(',') != -1:
                        self.modified_row += str(replace)
                    else:
                        self.modified_row += str(ch)
                eventlog(str(self.modified_row))
                #sleep(0.0025)
            self.modified_rows.append(str(self.modified_row))

        with open(str(target_file + str('_cleaned')), 'w+') as f:
            #f = open(str(target_file + str('_cleaned')), 'w+')
            for final_row in self.modified_rows:
                f.write(str(final_row))
                f.write('\n')
            f.close()


    #################### EMAIL TOOLS

    def test_blackmesanetwork(self, to_email):
        #blackmesanetwork.com
        EMAIL_ADDRESS = 'AKIARSYZUNZWNWNGJMWN'
        EMAIL_PASSWORD = 'BCJKvOCB8cWWWMx+H2CRgRWHqy+UrVE0I0Q1Kk2LPKIJ'

        msg = EmailMessage()
        msg['Subject'] = 'Test subject line'
        msg['From'] = 'andre@blackmesanetwork.com'
        msg['To'] = to_email
        msg.set_content('test msg content')

        with smtplib.SMTP('email-smtp.us-west-2.amazonaws.com', 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)


    def test_stringkeeper(self):
        #blackmesanetwork.com
        to_email = 'andredoumad@gmail.com'
        EMAIL_ADDRESS = 'AKIAYZ2XE524ITIKU2R2'
        EMAIL_PASSWORD = 'BOdXu8OSHD16twbYZZLElgtFh/3QH/aadSIp6y9oQiSI'

        msg = EmailMessage()
        msg['Subject'] = 'Test subject line'
        msg['From'] = 'andre@stringkeeper.com'
        msg['To'] = to_email
        msg.set_content('test msg content')

        with smtplib.SMTP('email-smtp.us-west-2.amazonaws.com', 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)



    def send_email_from_ahap(self, to_email, subject, message):
        #ahaplink.com
        EMAIL_ADDRESS = 'AKIAVP7LLQWGVXPBL5NC'
        EMAIL_PASSWORD = 'BNw8dTB+gVW55dA+j0rlCkVQEtUpDhTtjU9rW13UynOq'

        msg = EmailMessage()
        msg['Subject'] = str(subject)
        msg['From'] = 'connect@ahaplink.com'
        msg['To'] = to_email
        msg.set_content(str(message))
        Tools.check_internet_connection(self)
        with smtplib.SMTP('email-smtp.us-west-2.amazonaws.com', 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        '''
        try:
            Tools.improve_ses_status_ahaplink(self)
        except:
            eventlog('guerrillamail failure likely...')
        '''


    def improve_ses_status_ahaplink(self):
        eventlog('---------------')
        #ahaplink.com
        EMAIL_ADDRESS = 'AKIAVP7LLQWGVXPBL5NC'
        EMAIL_PASSWORD = 'BNw8dTB+gVW55dA+j0rlCkVQEtUpDhTtjU9rW13UynOq'
        eventlog('+++++')
        subject, message = Tools.generate_ahap_flyer(self)
        eventlog('+++++')
        #just send another email to a known address so that the complaint and the bounce rate doesnt matter.
        msg = EmailMessage()
        msg['Subject'] = str(subject)
        msg['From'] = 'connect@ahaplink.com'

        session = GuerrillaMailSession()
        to_email = str(session.get_session_state()['email_address'])
        msg['To'] = to_email
        msg.set_content(str(message))
        
        eventlog ('created email: ' + to_email)
        sleep_duration = random.uniform(0.002,0.004)
        sleep(sleep_duration)
        with smtplib.SMTP('email-smtp.us-west-2.amazonaws.com', 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        '''
        sleep_duration = random.uniform(14,15)
        sleep(sleep_duration)
        session.set_email_address(to_email)
        eventlog(session.email_address)
        eventlog(session.get_email_list)
        eventlog(session.get_email)
        eventlog (subprocess.check_output(['guerrillamail','setaddr', str(to_email)]))
        eventlog (subprocess.check_output(['guerrillamail','info']))
        output = Popen(['guerrillamail','list'],stdout=PIPE)
        result = output.communicate()
        #result = subprocess.check_output(['guerrillamail','list'], stdout=subprocess.PIPE)
        eventlog (result)
        email_id = Tools.find_between(self, str(result), '(*)', '  ')
        eventlog('email id: ' + str(email_id))
        
        eventlog (subprocess.check_output(['guerrillamail','get', str(email_id)]))
        eventlog('---------------')
        eventlog('\n')
        '''

    def bounce_check_email(self, email):
        
        eventlog('Bounce checking: ' + str(email))
        valid = False
        try:
            v = validate_email(email) # validate and get info
            email = v["email"] # replace with normalized form
            #eventlog('is email valid? ' + str(email))
            #eventlog('yes')
            valid = True
        except EmailNotValidError as e:
            # email is not valid, exception message is human-readable
            eventlog('INVALID EMAIL: ' + str(e))

        if valid == True:
            
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

            if match == None:
                eventlog('Bad Syntax')
                valid = False
        
        # this part is going to require more effort. -- mainly 
        # - create a lightsail server to do this part on aws - maybe use californiaprogrammer.com
        # - see https://mail.python.org/pipermail/tutor/2012-September/091454.html
        # - i don't think you can run this from citadel.blackmesanetwork.com because cox your personal isp is blocking the use of those ports, also
        # - might give ur home ip a bad name.
        '''
        if valid == True:
            values = email.split('@')
            domain = values[1]
            eventlog('checking domain: ' + str(domain))
            records = dns.resolver.query(str(domain), 'MX')
            mxRecord = records[0].exchange
            mxRecord = str(mxRecord)

            # Get local server hostname
            host = socket.gethostname()

            # SMTP lib setup (use debug level for full output)
            server = smtplib.SMTP()
            server.set_debuglevel(5)

            # SMTP Conversation
            server.connect(mxRecord)
            server.helo(server.local_hostname)
            server.mail('infiniteandredoumad@gmail.com')
            code, message = server.rcpt(str(email))
            server.quit()

            # Assume 250 as Success
            if code == 250:
                eventlog('Success - valid email ' + str(email))
                valid = True
            else:
                eventlog('Bad - bounced email: ' + str(email))
                valid = False
        '''
        
        # for now - lets use a paid bounce checker until we can build this service.
        '''
        if valid == True:
            use some api for some paid service
        '''
        
        # try https://github.com/email-verifier/verifier-py https://verifier.meetchopra.com/user
        '''
        this is broken
        if valid == True:
            if verify_it.verify(str(email)):
                eventlog("Hurray! Email is right!")
                valid = True
            else:
                eventlog("Oh! Email is not real")
                valid = True

        '''
        
        '''
        you can use this instead
        GET https://verifier.meetchopra.com/verify/bob@blackmesanetwork.com?token=8b14aa0fc18366af9853c2b93d108ab4c07d6bc70304165a82039be5bd1a7466
        now what you'll need to do to complete this is what you did witht he pipe - call it --- pipe the result... 
        however - it still isn't totally a fix because it will call emails that have boucned valid it really only checks mx records.
        '''
        if valid == True:
            eventlog('Success')
            return True
        else:
            eventlog('Bad')
            return False
        
    def send_test_flyer(self):
        # email = 'andredoumad@gmail.com'
        # eventlog('running bounce_check_email')
        # good_email = Tools.bounce_check_email(self, email)
        # if not good_email:
        #     eventlog('not good')
        #     exit()
        #subject, message = Tools.generate_ahap_flyer(self)
        subject, message = Tools.select_ahap_flyer(self)
        Tools.send_email_from_ahap(self, 'andredoumad@gmail.com', subject, message)
        Tools.send_email_from_ahap(self, 'ad@ahapinc.com', subject, message)
        Tools.send_email_from_ahap(self, 'jd@ahapinc.com', subject, message)

    def generate_ahap_flyer(self):
        subject_lines_filepath = str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/flyers/ahap_introduction/subject_lines.txt'
        A_lines_filepath = str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/flyers/ahap_introduction/A_lines.txt'
        B_lines_filepath = str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/flyers/ahap_introduction/B_lines.txt'
        C_lines_filepath = str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/flyers/ahap_introduction/C_lines.txt'
        D_lines_filepath = str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/flyers/ahap_introduction/D_lines.txt'
        E_lines_filepath = str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/flyers/ahap_introduction/E_lines.txt'
        F_lines_filepath = str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/flyers/ahap_introduction/F_lines.txt'
        thelist = []
        thelist = Tools.get_list_from_file(self, subject_lines_filepath)
        thelist = Tools.shuffle_list(self, thelist)
        subject_line = thelist[0]

        thelist = Tools.get_list_from_file(self, A_lines_filepath)
        thelist = Tools.shuffle_list(self, thelist)
        A_line = thelist[0]

        thelist = Tools.get_list_from_file(self, B_lines_filepath)
        thelist = Tools.shuffle_list(self, thelist)
        B_line = thelist[0]

        thelist = Tools.get_list_from_file(self, C_lines_filepath)
        thelist = Tools.shuffle_list(self, thelist)
        C_line = thelist[0]

        thelist = Tools.get_list_from_file(self, D_lines_filepath)
        thelist = Tools.shuffle_list(self, thelist)
        D_line = thelist[0]

        thelist = Tools.get_list_from_file(self, E_lines_filepath)
        thelist = Tools.shuffle_list(self, thelist)
        E_line = thelist[0]
        
        thelist = Tools.get_list_from_file(self, F_lines_filepath)
        thelist = Tools.shuffle_list(self, thelist)
        F_line = thelist[0]

        message_string = str(str(A_line) + '\n\n' + str(B_line) + ' ' + str(C_line) + ' ' + str(D_line) + ' ' + str(E_line) + '\n\n' + str(F_line))
        eventlog('subject: ' + str(subject_line))
        eventlog('message: ' + str(message_string))
        return str(subject_line), str(message_string)


    def select_ahap_flyer(self):
        selected_flyers_directory = str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/flyers/selected_flyers/'
        self.b_dp, self.b_fp, self.list_dp, self.list_fp = Tools.get_list_files_folders_in_path(self, selected_flyers_directory)
        random_flyer_filepath = []
        random_flyer_filepath = Tools.shuffle_list(self, self.list_fp)
        selected_flyer_filepath = str(random_flyer_filepath[0])
        eventlog('selected_flyer_filepath: ' + str(selected_flyer_filepath))
        selected_flyer_lines = Tools.get_list_from_file(self, str(selected_flyer_filepath))
        eventlog('selected flyer lines count: ' + str(len(selected_flyer_lines)))
        message_string = ''
        for line in selected_flyer_lines:
            message_string += str(str(line) + '\n') 
        subject_line = str(selected_flyer_lines[0])

        eventlog('subject: ' + str(subject_line))
        eventlog('message: ' + str(message_string))
        return str(subject_line), str(message_string)


    def check_internet_connection(self):
        loop_value = 1
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%Y-%m-%d-%H:%M", named_tuple)
        while loop_value == 1:
            #eventlog('|  network test | ' + str(loop_value))
            try:
                urllib.request.urlopen("http://www.google.com")
                loop_value = 0
                #eventlog('|    ONLINE     | ' + str(time_string))
            except urllib.error.URLError as e:

                eventlog('|    OFFLINE    | ' + str(time_string))
                eventlog(e.reason)
                #eventlog('|network offline| ' )
            sleep(3)

    def work_only_on_monday_to_friday(self):
        my_date = date.today()
        eventlog(my_date)
        day = str(calendar.day_name[my_date.weekday()])  #'Wednesday'
        eventlog(day)
        if day == 'Saturday' or day == 'Sunday':
            eventlog('Only working on monday to friday - exiting')
            exit()
        else:
            eventlog('today is a work day, sending emails !')


    #send email of flyer every 15 seconds from 830am to 1:30
    def mass_mail_ahap_introduction(self):
        Tools.work_only_on_monday_to_friday(self)

        ready_for_processing = True
        #get list of emails from outbox
        outbox_list = []
        self.b_dp, self.b_fp, self.list_dp, self.list_fp = Tools.get_list_files_folders_in_path(self, str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/outbox/'))

        if self.b_fp == False:
            eventlog('NO FILES FOUND IN: /home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/outbox/' )
            ready_for_processing = False
        else:
            temp_list = []
            for file in self.list_fp:
                if file.find('outbox_emails') != -1:
                    temp_list = Tools.get_list_from_file(self, str(file))
                    for item in temp_list:
                        if len(item) > 3:
                            outbox_list.append(str(item))

        #get list of emails from sentbox
        sentbox_list = []
        self.b_dp, self.b_fp, self.list_dp, self.list_fp = Tools.get_list_files_folders_in_path(self, str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/sent/'))

        if self.b_fp == False:
            eventlog('NO FILES FOUND IN /home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/sent/' )
            ready_for_processing = False
        else:
            temp_list = []
            for file in self.list_fp:
                if file.find('sentbox_emails') != -1:
                    temp_list = Tools.get_list_from_file(self, str(file))
                    for item in temp_list:
                        if len(item) > 3:
                            sentbox_list.append(str(item))

        #if the sentbox list contains any emails from the sent box, append them to the outbox removal list
        eventlog('length of outbox is: ' + str(len(outbox_list)))
        eventlog('length of sentbox is: ' + str(len(sentbox_list)))
        updated_outbox_list = []
        duplicate_list = []
        outbox_list = Tools.deduplicate_list(self, outbox_list)
        for sent in sentbox_list:
            for out in outbox_list:
                if len(str(out)) == len(str(sent)):
                    if str(out) == str(sent):
                        duplicate_list.append(str(out))

        for out in outbox_list:
            found = False
            for duplicate in duplicate_list:
                if len(str(duplicate)) == len(str(out)):
                    if str(duplicate) == str(out):
                        found = True
                        break
            if found == False:
                updated_outbox_list.append(str(out))

        #for every email in the outbox, if it matches an email in the removal list - do not write it, otherwise write it
        eventlog('length of updated outbox is: ' + str(len(updated_outbox_list)))
        updated_outbox_list = Tools.shuffle_list(self, updated_outbox_list)
        #overwrite the outbox file without the emails found in the sent box
        with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/outbox/outbox_emails.csv'), 'w') as iwrite:
            for out in updated_outbox_list:
                iwrite.write(str(out))
                iwrite.write('\n')
            iwrite.close()
        #for every email in the outgoing list, send an introuction email
        #for out in updated_outbox_list:
        for out in updated_outbox_list:
            sleep_duration = random.uniform(0.002,0.003)
            file_named_tuple = time.localtime() # get struct_time
            file_time_string = time.strftime("%Y-%m-%d-%H-%M-%S", file_named_tuple)
            eventlog('\n =====  \n sent email to: ' + str(out) + ' at ' +str(file_time_string))
            with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/sent/log.csv'), 'a') as iwrite:
                iwrite.write(str(str(out) + ',' + str(file_time_string)))
                iwrite.write('\n')
                iwrite.close()

            #subject, message = Tools.generate_ahap_flyer(self)
            
            subject, message = Tools.select_ahap_flyer(self)
            
            Tools.check_internet_connection(self)
            
            good_email = True

            list_removed_domains = Tools.get_list_from_file(self, str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ignored_domains.csv')
            if good_email == True:
                for domain in list_removed_domains:
                    if str(out).find(str(domain)) != -1:
                        good_email = False
                        with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/sent/sentbox_ignored_domains.csv'), 'a+') as iwrite:
                            iwrite.write(str(out))
                            iwrite.write('\n')
                            iwrite.close()
                        break



            #/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/removed_domains/removed_domains.csv
            list_removed_domains = Tools.get_list_from_file(self, str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/removed_domains/removed_domains.csv')
            if good_email == True:
                for domain in list_removed_domains:
                    if str(out).find(str(domain)) != -1:
                        good_email = False
                        with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/sent/sentbox_removed_domains.csv'), 'a') as iwrite:
                            iwrite.write(str(out))
                            iwrite.write('\n')
                            iwrite.close()
                        break

            #/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/removed_emails/removed_emails.csv
            list_removed_emails = Tools.get_list_from_file(self, str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/removed_emails/removed_emails.csv')
            if good_email == True:
                for email_address in list_removed_emails:
                    if len(str(out)) ==  len(str(email_address)):
                        if str(out) == str(email_address):
                            good_email = False
                            with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/sent/sentbox_removed_emails.csv'), 'a') as iwrite:
                                iwrite.write(str(out))
                                iwrite.write('\n')
                                iwrite.close()
                            break

            if good_email == True:
                good_email = Tools.bounce_check_email(self, str(out))
                if good_email == False:
                    with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/sent/sentbox_bounced_emails.csv'), 'a') as iwrite:
                        iwrite.write(str(out))
                        iwrite.write('\n')
                        iwrite.close()
            
            if good_email == True:
                self.sending = True
                while self.sending == True:
                    try:
                        Tools.send_email_from_ahap(self, str(out), subject, message)
                        self.sending = False
                    except:
                        sleep(3)

            with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/sent/sentbox_emails.csv'), 'a') as iwrite:
                iwrite.write(str(out))
                iwrite.write('\n')
                iwrite.close()

            sleep(sleep_duration)
        #append email to sentbox file

        #sleep 15 seconds


    def testing(self, test_input):
        file_named_tuple = time.localtime() # get struct_time
        file_time_string = time.strftime("%Y-%m-%d-%H-%M-%S", file_named_tuple)
        eventlog('testing ' + str(test_input))
        with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/testing.csv'), 'a') as iwrite:
            iwrite.write(str('testing: ' + str(test_input) + ' ' + str(file_time_string)))
            iwrite.write('\n')
            iwrite.close()
            
            
    def improve_ahaplink_ses_status_loop(self):
        working = True
        while working == True:
            Tools.improve_ses_status_ahaplink(self)
            sleep_duration = random.uniform(0.1, 0.2)
            sleep(sleep_duration)



# actual standalone functions.

def get_list_from_file(filepath):
    listFromFile = []
    listFromFile.clear()
    working = True
    with open(filepath) as fh:
        #fh = open(filepath)
        while working == True:
            for line in fh:
                listFromFile.append(line.rstrip())
            working = False
        fh.close()
    return listFromFile


def get_date_and_time_string():
    from datetime import datetime

    # datetime object containing current date and time
    now = datetime.now()
    
    print("now =", now)

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%Y/%m/%d/ %H:%M:%S")
    print("date and time =", dt_string)
    return dt_string

def get_hour_minute_second_string():
    from datetime import datetime

    # datetime object containing current date and time
    now = datetime.now()
    
    # print("now =", now)

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%H:%M:%S")
    # print("Hour minute second =", dt_string)
    return dt_string




if __name__ == '__main__':
    tools = Tools()
    job_name = 'AHAP'
    implicit_keys = ['PERSON', 'FAC', 'LOC', 'GPE', 'ORG', 'NORP', 'CARDINAL']
    explicit_keys = ['medical', 'fqhc', 'health', 'ceo', 'critical access', 'cfo', 'financial', 'director', 'chief' ]
    
    if sys.argv[1] == 'testing':
        tools.testing(sys.argv[1])


    #tools.file_shuffle(str(str(Path.home()) + '/p3env/alice/alice/spiders/AHAP/incomplete_work/2019-09-14-21-27-04_email_harvest_final_report_included-debounce.csv'))
    #tools.create_job_search_phrase('AHAP')


    if sys.argv[1] == 'harvest_email_heap_full_using_csv_triggers_filters':
        tools.harvest_email_heap_full_using_csv_triggers_filters(job_name)
    #tools.harvest_email_heap_full_using_csv_triggers_filters(job_name)

    #tools.create_unique_list_emails_given_two_files('AHAP', str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/email_heap.csv'), str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/published/total_published.csv'))

    #tools.deduplicate_files_in_folder(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/duck_duck_go')

    #target_file = str(Path.home()) + '/p3env/alice/alice/spiders/AHAP/incomplete_work/Community Health_9_19_19.csv'
    #tools.remove_commas_between_symbols('"', ' ', target_file)

    ##### EMAILS
    if sys.argv[1] == 'mass_mail_ahap_introduction':
        tools.mass_mail_ahap_introduction()
    #tools.mass_mail_ahap_introduction()
    
    if sys.argv[1] == 'generate_ahap_flyer':
        tools.generate_ahap_flyer()
        
    if sys.argv[1] == 'send_test_flyer':
        for i in range(0, 20):
            tools.send_test_flyer()
        
    if sys.argv[1] == 'test_stringkeeper':
        tools.test_stringkeeper()
        
    if sys.argv[1] == 'bounce_check_email':
        tools.bounce_check_email('jgoettler@tetonhospital.org')
    #tools.test_ahap('andre@blackmesanetwork.com')
    
    if sys.argv[1] == 'improve_ahaplink_ses_status_loop':
        tools.improve_ahaplink_ses_status_loop()
        
    if sys.argv[1] == 'work_only_on_monday_to_friday':
        tools.work_only_on_monday_to_friday()


    exit()