# -*- coding: utf-8 -*-
import os, time, random, smtplib, shutil
from random import *
import inspect
from time import sleep
from email.message import EmailMessage
import random
import urllib.request, urllib.error, urllib.parse
import codecs
import sys
import unicodedata
import ftfy

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
                    #print('get_list_from_file: ' + str(line.rstrip()))
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
                    print('unique: ' + str(a))
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
                    print('unique: ' + str(b))

        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%Y-%m-%d-%H:%M", named_tuple)

        iwrite = open(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/unique_emails_' + time_string + '.csv'), 'w+')
        new_list = self.getListWithoutDuplicates(new_list)
        for item in new_list:
            valid, reason = Tools.verify_email(self, str(job_name), str(item))
            if valid == True:
                print('VALID: ' + str(item))
                iwrite.write(str(item))
                iwrite.write(str('\n'))
            else:
                print('ignored: ' + str(item))
        iwrite.close()


    def verify_email(self, job_name, email):
        valid = True
        reason = ''

        if not os.path.exists(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_email_filters.csv')):
            with open(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_email_filters.csv'), 'a') as f:
                f.write('')
                #f.close

        list_job_email_filters = Tools.get_list_from_file(self, str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_email_filters_before_at.csv'))

        def check_emails(self, thelist, value):
            searching = True
            valid = True
            reason = ''
            while searching == True:
                for item in thelist:
                    if len(item) > 0:
                        #print('checking: ' + str(item))
                        values = value.split('@')
                        try:
                            #print('checking: ' + values[1] + ' for ' + str(item) )
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


        list_job_email_filters = Tools.get_list_from_file(self, str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_email_filters_after_at.csv'))

        def check_emails_after_at(self, thelist, value):
            searching = True
            valid = True
            reason = ''
            while searching == True:
                for item in thelist:
                    if len(item) > 0:
                        #print('checking: ' + str(item))
                        values = value.split('@')
                        try:
                            #print('checking: ' + values[1] + ' for ' + str(item) )
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

        #print('VALID: ' + str(valid) + ' REASON: ' + str(reason) + ' EMAIL: ' + str(email))
        
        return valid, reason


    def deduplicate_file(self, filepath):
        lines = Tools.get_list_from_file(self, filepath)
        lines = Tools.getListWithoutDuplicates(self, lines)
        iwrite = open(str(filepath), 'w+')
        for item in lines:
            print(str(item))
            iwrite.write(str(item))
            iwrite.write(str('\n'))
        iwrite.close()


    def deduplicate_list(self, thelist):
        lines = thelist
        lines = Tools.getListWithoutDuplicates(self, lines)
        #iwrite = open(str(filepath), 'w+')
        for item in lines:
            print('deduplicate list: ' + str(item))
        return lines


    def get_list_files_folders_in_path(self, path):

        self.list_fp = []
        self.list_dp = []
        self.b_fp = False
        self.b_dp = False
        for i in os.scandir(path):
            if i.is_file():
                #print('File: ' + i.path)
                self.list_fp.append(i.path)
                self.b_fp = True
            elif i.is_dir():
                #print('Folder: ' + i.path)
                self.list_dp.append(i.path + '/')
                self.b_dp = True
        return self.b_dp, self.b_fp, self.list_dp, self.list_fp


    def deduplicate_files_in_folder(self, directorypath):
        b_dp, b_fp, list_dp, list_fp = self.get_list_files_folders_in_path(directorypath)
        if b_fp:
            for file in list_fp:
                print('deduplicating: ' + str(file))
                self.deduplicate_file(file)

    def shuffle_list(self, inputlist):
        for i in range(len(inputlist)):
            swap = randint(0,len(inputlist)-1)
            temp = inputlist[swap]
            inputlist[swap] = inputlist[i]
            inputlist[i] = temp
        return inputlist

    def create_job_search_phrase(self, job_name):
        search_keys_filepath = str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/search_keys.csv')
        self.search_keys = self.get_list_from_file(search_keys_filepath)
        self.search_phrase_list = []
        self.search_phrase = ''
        self.success = False
        for item in self.search_keys:
            print('search_keys: ' + str(item))
        def append_word_to_search_phrase_list(self):
            appending_word = True

            while appending_word == True:
                shuffled_keys = Tools.shuffle_list(self, self.search_keys)
                for key in shuffled_keys:
                    if self.success == False:
                        print('trying key: ' + str(key))
                        self.duplicate = False
                        print('using key: ' + str(key) )
                        temp_search_phrase = self.search_phrase
                        temp_search_phrase += str(str(key))
                        print('temp_search_phrase: ' + str(temp_search_phrase))

                        completed_searches = self.get_list_from_file('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_phrases_complete.csv')
                        queued_searches = self.get_list_from_file('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_phrases.csv')
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
                                print('success search_phrase: ' + str(temp_search_phrase))
                                self.search_phrase_list.append(str(key))
                                self.search_phrase += str(str(key) + ' ')
                                self.success = True
                                appending_word = False
                            else:
                                self.search_phrase += str(str(key) + ' ')
                        else:
                            self.search_phrase += str(str(key) + ' ')

        append_word_to_search_phrase_list(self)

        if self.success == True:
            iwrite = open(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_phrases.csv'), 'a+')
            iwrite.write(str(self.search_phrase))
            iwrite.write(str('\n'))
            iwrite.close()
            print('appended search_phrase: ' + str(self.search_phrase))

    def verify_hyperlink(self, url, job_name):
        valid = True

        if len(url) < 11:
            valid = False

        if valid == True:
            hyperlink_trigger_keys = Tools.get_list_from_file(self, '/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/hyperlink_trigger_keys.csv')
            hyperlink_ignore_keys = Tools.get_list_from_file(self, '/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/hyperlink_ignore_keys.csv')
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

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/get_list_files_folders_in_path.history', prefix='get_list_files_folders_in_path', depth=1)
    def get_list_files_folders_in_path(self, path):
        self.list_fp = []
        self.list_dp = []
        self.b_fp = False
        self.b_dp = False
        for i in os.scandir(path):
            if i.is_file():
                #print('File: ' + i.path)
                self.list_fp.append(i.path)
                self.b_fp = True
            elif i.is_dir():
                #print('Folder: ' + i.path)
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

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='getListFromFile', depth=1)
    def harvest_email_heap_full_using_csv_triggers_filters(self, job_name):
        file_named_tuple = time.localtime() # get struct_time
        file_time_string = str(time.strftime("%Y-%m-%d-%H-%M-%S", file_named_tuple))
        today_ymd = str(time.strftime("%Y-%m-%d", file_named_tuple))
        print('todays date: ' + str(today_ymd))
        
        self.records = []
        emails = []
        self.completed_emails = []
        self.hyperlink_trigger_keys = Tools.get_list_from_file(self, str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/hyperlink_trigger_keys.csv'))
        self.hyperlink_ignore_keys = Tools.get_list_from_file(self, str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/hyperlink_ignore_keys.csv'))
        self.description_trigger_keys = Tools.get_list_from_file(self, str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/description_trigger_keys.csv'))
        self.description_ignore_keys = Tools.get_list_from_file(self, str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/description_ignore_keys.csv'))
        self.irrelavant_words_for_email_parsing = Tools.get_list_from_file(self, str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/irrelavant_words_for_email_parsing.csv'))



        #find all of the email heap full files inside of the  /home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/daily folder
        self.b_dp, self.b_fp, self.list_dp, self.list_fp = Tools.get_list_files_folders_in_path(self, str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + str('/harvest/contacts/emails/daily/')))

        if self.b_fp == False:
            print('NO FILES FOUND IN: ' + str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + str('/harvest/contacts/emails/daily/')))


        for file in self.list_fp:
            print('files found: ' + str(file))

        list_email_heap_filepaths = []
        b_found_email_heap_full = False
        for filepath in self.list_fp:
            if filepath.find('email_heap_full') != -1:
                #ignore any files created today -- just work with previous results.
                if filepath.find(str(today_ymd)) == -1:
                    list_email_heap_filepaths.append(filepath)
                    b_found_email_heap_full = True
                else:
                    print('skipping ' + str(filepath))
                    sleep(2)


        if b_found_email_heap_full == False:
            print('did not find email heap for processing')
        else:
            print('found email heap for processing')
            with open(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_report_incomplete.csv'), 'a') as iwrite:
                iwrite.write(str('email,url,description,timestamp'))
                iwrite.write(str('\n'))
                iwrite.close()

            with open(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_final_report_included.csv'), 'a') as iwrite:
                iwrite.write(str('email,url,description,timestamp'))
                iwrite.write(str('\n'))
                iwrite.close()

            with open(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_final_report_ignored.csv'), 'a') as iwrite:
                iwrite.write(str('email,url,description,timestamp'))
                iwrite.write(str('\n'))
                iwrite.close()

            with open(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_final_invalid_reasons.csv'), 'a') as iwrite:
                iwrite.write(str('reason,email,url,description,timestamp'))
                iwrite.write(str('\n'))
                iwrite.close()

            for file in list_email_heap_filepaths:
                print('list_email_heap_filepaths files found: ' + str(file))

            list_email_heap_full = []

            for file in list_email_heap_filepaths:
                newList = Tools.get_list_from_file(self, file)
                for line in newList:
                    list_email_heap_full.append(str(line))

            for line in list_email_heap_full:
                print('list_email_heap_full lines found: ' + str(line))

            self.list_email_heap_full_length = len(list_email_heap_full)

            self.banned_domains = []
            if not os.path.exists(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/ignored_domains.csv')):
                with open(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/ignored_domains.csv'), 'a') as f:
                    f.write('\n')
                    f.write('\n')
                    f.close
            else:
                self.banned_domains = Tools.get_list_from_file(self, str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/ignored_domains.csv'))

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
                    print('IGNORING DOMAIN: ' + str(self.domain))
                    with open(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/ignored_domains.csv'), 'a') as iwrite:
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
                                    print(str(recordNumber) + '/' + str(self.list_email_heap_full_length) + ' | INVALID description | ' + str(item) + ' | ' + str(email) + self.lineno())
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
                                #print('checking: ' + str(item))
                                if url.lower().find(str(item).lower()) != -1:
                                    harvest = False
                                    print( str(recordNumber) + '/' + str(self.list_email_heap_full_length) + ' |  INVALID hyperlink  | ' + str(item) + ' | ' + str(email) + self.lineno())
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
                    print('IGNORING: ' + str(url))

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
                                        #print('irrelavant: ' + str(word))
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
                                with open(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_report_incomplete.csv'), 'a') as iwrite:
                                    self.records.append(self.record)
                                    iwrite.write(str(self.record))
                                    iwrite.write(str('\n'))
                                    iwrite.close()
                            else:
                                with open(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_final_invalid_reasons.csv'), 'a') as iwrite:
                                    iwrite.write(str(reason) + ',' + self.record)
                                    iwrite.write(str('\n'))
                                    iwrite.close()
                                print(str(heap_index) + '/' + str(self.list_email_heap_full_length) + ' | INVALID  | ' + str(reason) + ' | ' + str(email) + self.lineno())
                        else:
                            with open(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_final_invalid_reasons.csv'), 'a') as iwrite:
                                iwrite.write(str(reason) + ',' + self.record)
                                iwrite.write(str('\n'))
                                iwrite.close()
                            print(str(heap_index) + '/' + str(self.list_email_heap_full_length) + ' | INVALID  | ' + str(reason) + ' | ' + str(email) + self.lineno())
                        self.completed_emails.append(str(email))
                heap_index += 1
            sleep(1)

            incomplete_list = Tools.get_list_from_file(self, str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_report_incomplete.csv'))
            self.record_number = 0
            for record in incomplete_list:
                if self.record_number != 0:
                    self.found = False
                    self.reason = ''
                    for banned_domain in self.banned_domains:
                        if len(str(banned_domain)) > 3:
                            if str(record).lower().find(str(banned_domain)) != -1:
                                self.found = True
                                print('BANNED DOMAIN: ' + str(banned_domain) + ' MATCHES RECORD: ' + str(record))
                                self.reason = banned_domain
                                break
                    if self.found == False:
                        print('record number: ' + str(self.record_number) + ' Reason: ' + str(self.reason) +  ' INCLUDING: ' + str(record))
                        #'/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/outbox'
                        values = record.split(',')
                        with open(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/contacts/emails/flyers/ahap_introduction/outbox/' + 'outbox_emails.csv'), 'a') as iwrite:
                            iwrite.write(str(values[0]))
                            iwrite.write(str('\n'))
                            iwrite.close()

                        with open(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_final_report_included.csv'), 'a') as iwrite:
                            iwrite.write(str(record))
                            iwrite.write(str('\n'))
                            iwrite.close()
                    else:
                        print('record number: ' + str(self.record_number) + ' Reason: ' + str(self.reason) +  ' IGNORING: ' + str(record))
                        with open(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_final_report_ignored.csv'), 'a') as iwrite:
                            iwrite.write(str(record))
                            iwrite.write(str('\n'))
                            iwrite.close()

                self.record_number += 1

            ### move files to /home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/reports
            source = str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_final_invalid_reasons.csv')
            destination = str(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/reports/') + str(file_time_string) + '_email_harvest_final_invalid_reasons.csv')
            Tools.move_file(self, source, destination)
            source = str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_report_incomplete.csv')
            destination = str(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/reports/') + str(file_time_string) + '_email_harvest_report_incomplete.csv')
            Tools.move_file(self, source, destination)
            source = str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_final_report_included.csv')
            destination = str(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/reports/') + str(file_time_string) + '_email_harvest_final_report_included.csv')
            Tools.move_file(self, source, destination)
            source = str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/' + str(file_time_string) + '_email_harvest_final_report_ignored.csv')
            destination = str(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/reports/') + str(file_time_string) + '_email_harvest_final_report_ignored.csv')
            Tools.move_file(self, source, destination)


            for filepath in list_email_heap_filepaths:
                ### move full heap to /home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/scanned
                source = str(filepath)
                destination = str(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/contacts/emails/scanned/'))
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
                print(str(self.modified_row))
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

    def send_email_from_ahap(self, to_email, subject, message):
        #ahaplink.com
        EMAIL_ADDRESS = 'AKIAVP7LLQWGVXPBL5NC'
        EMAIL_PASSWORD = 'BNw8dTB+gVW55dA+j0rlCkVQEtUpDhTtjU9rW13UynOq'

        msg = EmailMessage()
        msg['Subject'] = str(subject)
        msg['From'] = 'connect@ahaplink.com'
        msg['To'] = to_email
        msg.set_content(str(message))

        with smtplib.SMTP('email-smtp.us-west-2.amazonaws.com', 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)


    def generate_ahap_flyer(self):
        subject_lines_filepath = '/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/flyers/ahap_introduction/subject_lines.txt'
        A_lines_filepath = '/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/flyers/ahap_introduction/A_lines.txt'
        B_lines_filepath = '/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/flyers/ahap_introduction/B_lines.txt'
        C_lines_filepath = '/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/flyers/ahap_introduction/C_lines.txt'
        D_lines_filepath = '/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/flyers/ahap_introduction/D_lines.txt'
        E_lines_filepath = '/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/flyers/ahap_introduction/E_lines.txt'
        F_lines_filepath = '/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/flyers/ahap_introduction/F_lines.txt'

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

        message_string = str(str(A_line) + ' ' + str(B_line) + ' ' + str(C_line) + ' ' + str(D_line) + ' ' + str(E_line) + ' ' + str(F_line))
        print('subject: ' + str(subject_line))
        print('message: ' + str(message_string))
        return str(subject_line), str(message_string)


    def check_internet_connection(self):
        loop_value = 1
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%Y-%m-%d-%H:%M", named_tuple)
        while loop_value == 1:
            #print('|  network test | ' + str(loop_value))
            try:
                urllib.request.urlopen("http://www.google.com")
                loop_value = 0
                #print('|    ONLINE     | ' + str(time_string))
            except urllib.error.URLError as e:

                print('|    OFFLINE    | ' + str(time_string))
                print(e.reason)
                #print('|network offline| ' )
            sleep(3)


    #send email of flyer every 15 seconds from 830am to 1:30
    def mass_mail_ahap_introduction(self):
        ready_for_processing = True
        #get list of emails from outbox
        outbox_list = []
        self.b_dp, self.b_fp, self.list_dp, self.list_fp = Tools.get_list_files_folders_in_path(self, str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/outbox/'))

        if self.b_fp == False:
            print('NO FILES FOUND IN: /home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/outbox/' )
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
        self.b_dp, self.b_fp, self.list_dp, self.list_fp = Tools.get_list_files_folders_in_path(self, str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/sent/'))

        if self.b_fp == False:
            print('NO FILES FOUND IN /home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/sent/' )
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
        print('length of outbox is: ' + str(len(outbox_list)))
        print('length of sentbox is: ' + str(len(sentbox_list)))
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
        print('length of updated outbox is: ' + str(len(updated_outbox_list)))
        updated_outbox_list = Tools.shuffle_list(self, updated_outbox_list)
        #overwrite the outbox file without the emails found in the sent box
        with open(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/outbox/outbox_emails.csv'), 'w') as iwrite:
            for out in updated_outbox_list:
                iwrite.write(str(out))
                iwrite.write('\n')
            iwrite.close()
        #for every email in the outgoing list, send an introuction email
        #for out in updated_outbox_list:
        for out in updated_outbox_list:
            sleep_duration = random.uniform(10, 15)
            file_named_tuple = time.localtime() # get struct_time
            file_time_string = time.strftime("%Y-%m-%d-%H-%M-%S", file_named_tuple)
            print('sent email to: ' + str(out) + ',' +str(file_time_string))
            with open(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/sent/log.csv'), 'a') as iwrite:
                iwrite.write(str('sent email to: ' + str(out) + str(file_time_string)))
                iwrite.write('\n')
                iwrite.close()

            subject, message = Tools.generate_ahap_flyer(self)
            Tools.check_internet_connection(self)
            Tools.send_email_from_ahap(self, str(out), subject, message)
            with open(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/flyers/ahap_introduction/sent/sentbox_emails.csv'), 'a') as iwrite:
                iwrite.write(str(out))
                iwrite.write('\n')
                iwrite.close()

            sleep(sleep_duration)
        #append email to sentbox file

        #sleep 15 seconds


    def testing(self, test_input):
        file_named_tuple = time.localtime() # get struct_time
        file_time_string = time.strftime("%Y-%m-%d-%H-%M-%S", file_named_tuple)
        print('testing ' + str(test_input))
        with open(str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/testing.csv'), 'a') as iwrite:
            iwrite.write(str('testing: ' + str(test_input) + ' ' + str(file_time_string)))
            iwrite.write('\n')
            iwrite.close()

if __name__ == '__main__':
    tools = Tools()
    job_name = 'AHAP'
    implicit_keys = ['PERSON', 'FAC', 'LOC', 'GPE', 'ORG', 'NORP', 'CARDINAL']
    explicit_keys = ['medical', 'fqhc', 'health', 'ceo', 'critical access', 'cfo', 'financial', 'director', 'chief' ]
    
    if sys.argv[1] == 'testing':
        tools.testing(sys.argv[1])


    #tools.file_shuffle(str('/home/gordon/p3env/alice/alice/spiders/AHAP/incomplete_work/2019-09-14-21-27-04_email_harvest_final_report_included-debounce.csv'))
    #tools.create_job_search_phrase('AHAP')


    if sys.argv[1] == 'harvest_email_heap_full_using_csv_triggers_filters':
        tools.harvest_email_heap_full_using_csv_triggers_filters(job_name)
    #tools.harvest_email_heap_full_using_csv_triggers_filters(job_name)

    #tools.create_unique_list_emails_given_two_files('AHAP', str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/email_heap.csv'), str('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/contacts/emails/published/total_published.csv'))

    #tools.deduplicate_files_in_folder('/home/gordon/p3env/alice/alice/spiders/DATABASE/JOBS/AHAP/harvest/duck_duck_go')

    #target_file = '/home/gordon/p3env/alice/alice/spiders/AHAP/incomplete_work/Community Health_9_19_19.csv'
    #tools.remove_commas_between_symbols('"', ' ', target_file)

    ##### EMAILS
    if sys.argv[1] == 'mass_mail_ahap_introduction':
        tools.mass_mail_ahap_introduction()
    #tools.mass_mail_ahap_introduction()
    #tools.generate_ahap_flyer()
    #tools.test_ahap('andre@blackmesanetwork.com')


    exit()