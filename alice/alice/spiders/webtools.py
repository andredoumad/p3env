# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from os.path import sameopenfile
from bs4 import NavigableString
from bs4 import BeautifulSoup
#from urlparse import urlsplit
from AliceRequiredModules import *
from chronos import Chronos
from databasetools import DatabaseTools
from threaded import *
from standalone_tools import Tools
# from .AliceRequiredModules import *
# from .chronos import Chronos
# from .databasetools import DatabaseTools
# from .threaded import *
# from .standalone_tools import Tools
import urllib.request, urllib.error, urllib.parse
import urllib.parse
#from alice.spiders.multithreaded_web_browser import *
import os
import queue
import threading
import time
import shutil
from collections import Counter
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.common.exceptions import TimeoutException
from multiprocessing.pool import ThreadPool
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from standalone_tools import *
# from .standalone_tools import *

LANGUAGE = "english"
#SENTENCES_COUNT = 10

DOMAIN_FORMAT = re.compile(
    r"(?:^(\w{1,255}):(.{1,255})@|^)" # http basic authentication [optional]
    r"(?:(?:(?=\S{0,253}(?:$|:))" # check full domain length to be less than or equal to 253 (starting after http basic auth, stopping before port)
    r"((?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+" # check for at least one subdomain (maximum length per subdomain: 63 characters), dashes in between allowed
    r"(?:[a-z0-9]{1,63})))" # check for top level domain, no dashes allowed
    r"|localhost)" # accept also "localhost" only
    r"(:\d{1,5})?", # port [optional]
    re.IGNORECASE
)
SCHEME_FORMAT = re.compile(
    r"^(http|hxxp|ftp|fxp)s?$", # scheme: http(s) or ftp(s)
    re.IGNORECASE
)

(_ROOT, _DEPTH, _BREADTH) = range(3)

_FINISH = False
_HARVEST_COUNT = 0
_HARVESTED_EMAIL_COUNT = 0
_URL_TARGETS = []
_OLD_DOMAINS = []
#_THREADLOCK = threading.Lock()

class WebTools:

    def __init__(self, charlotte):
        self.charlotte = charlotte
        self.activeThreads = False

    def clear_screen(self):
        pass

        # with open(str(Path.home()) + '/p3env/alice/alice/spiders/nohup.out', 'w') as f:
        #     f.write('')
        #     f.close()

        # # Clear command as function of OS
        # command = "cls" if platform.system().lower()=="windows" else "clear"

        # # Action
        # return subprocess.call(command) == 0
        
        
    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='debuginfo', depth=1)
    def debuginfo(self, message):
        caller = getframeinfo(stack()[1][0])
        self.debugMessageList = []
        if message is not list:
            self.debugMessageList.append(message)
        else:
            self.debugMessageList = message
        self.f = open("parse.txt", "a+")
        if message is list:
            for i in range(0, len(self.debugMessageList)):
                eventlog(str("WebTools|" + str(caller.lineno) + "|START| " + str(self.debugMessageList[i]) + "  " + str(caller.lineno) +" |END|"))
                #self.f.write(str("" + str(caller.lineno) + "|START| " + str(self.debugMessageList[i]) + "  " + str(caller.lineno) +" |END|"))
        else:
            eventlog(str("WebTools|" + str(caller.lineno) + "|START| " + str(self.debugMessageList[0])  + "  " + str(caller.lineno) +" |END|"))
        self.f.close()

    def file_len(self, fname):
        i = 0
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1
    
    def lineno(self):
        """Returns the current line number in our program."""
        return str(' line: ' + str(inspect.currentframe().f_back.f_lineno))

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='get_list_ignore', depth=1)
    def get_list_ignore(self):
        self.list_ignore = []
        try:
            #self.debuginfo("\n" + str(os.getcwd() + "/list_ignore.csv") +"\n")
            #self.debuginfo("\n" + ignoreFilepath)
            with open("list_ignore.csv") as f:
                while True:
                    line = f.readline()
                    if line == '':
                        break
                    self.list_ignore.append(line.rstrip())
                f.close()

            #for ignored in self.list_ignore:
                #self.debuginfo(" WebTools will IGNORE urlS CONTAINING: " + str(ignored))
            return self.list_ignore
        except:
            eventlog("\n\n - - - - - - - - - EXCEPTION - - - - - - - - - \n\n" + 
                    " - - - - - - - - - get_list_ignore " +
                    "\n\n - - - - - - - - - EXCEPTION - - - - - - - - - \n\n")
            #self.debuginfo("\n\n - - - - - - - - - EXCEPTION - - - - - - - - - \n\n")
            #self.debuginfo(" self.list_ignore.csv was not found. Create an self.list_ignore.csv to ignore things. \n")
            #sleep(0.01)


    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='validate_url', depth=1)
    def validate_url(self, url, list_ignore):
        url = url.strip()
        boolValid = True
        complete = False
        while complete == False:
            if not url:
                boolValid = False
                complete = True
            if len(url) > 2048:
                boolValid = False
                complete = True
            result = urllib.parse.urlparse(url)
            scheme = result.scheme
            domain = result.netloc
            if not scheme:
                boolValid = False
                complete = True
            if not re.fullmatch(SCHEME_FORMAT, scheme):
                boolValid = False
                complete = True
            if not domain:
                boolValid = False
                complete = True
            if not re.fullmatch(DOMAIN_FORMAT, domain):
                boolValid = False
                complete = True
            for ignored in list_ignore:
                if url.find(ignored) != -1:
                    boolValid = False
                    complete = True
            #self.debuginfo(" " + url + " " + " is " + str(boolValid) )

            complete = True
        return boolValid
    '''
    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='soupGetPhone', depth=1)
    def extract_phone(self, data, siteLink):
        phone = re.findall(re.compile(r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|suffix)\s*(\d+))?'), data)

        if phone:
            number = ''.join(phone[0])
            if len(number) > 10:
                #self.debuginfo(str(siteLink))
                #self.debuginfo("\n +++++ FOUND ++++ " + str(number) + " +++++ FOUND ++++ \n")
                return True, str('+' + number)
            else:
                #self.debuginfo(str(siteLink))
                #self.debuginfo("\n +++++ FOUND ++++ " + str(number) + " +++++ FOUND ++++ \n")
                return True, str(number)
        else:
            return False, ''
    '''
    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='csvFormat', depth=1)
    def format_csv_string(self, string):
        self.dataString = string
        self.s0 = ''
        #if not data:
            #s0 = 'EMPTY'
        try:
            if self.dataString != '':
                if len(self.dataString) > 500:
                    self.s0 = self.dataString[:500]
        except:
            #self.debuginfo("\n\n - - - - - - - - - EXCEPTION - - - - - - - - - \n\n")
            if len(self.dataString) > 100:
                self.s0 = self.dataString[:75]
        if self.s0 == '':
            self.s0 = 'EMPTY'
        #self.debuginfo(self.s0)
       #sleep(0.1)
        return self.s0

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='Alice_Get_Entity', depth=1)
    def nlp_get_entity(self, data, a_nlp, a_matcher):
        try:
            #nlp = spacy.load("en_core_web_sm")
            doc = a_nlp(data)
            self.a_entity_texts = []
            self.a_entity_start_char = []
            self.a_entity_end_char = []
            self.a_entity_label = []
            for ent in doc.ents:
                self.a_entity_texts.append(str(ent.text))
                self.a_entity_start_char.append(str(ent.start_char))
                self.a_entity_end_char.append(str(ent.end_char))
                self.a_entity_label.append(str(ent.label_))
            return True, self.a_entity_texts, self.a_entity_start_char, self.a_entity_end_char, self.a_entity_label
        except:
            return False, '', '', '', ''

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/extract_emails.history', prefix='extract_emails', depth=1)
    def extract_emails(self, filepath):
        #raw = self.driver.page_source
        with open(filepath) as f:
            self.raw = f.read()
            '''
            soup = BeautifulSoup(raw, "lxml")
            hrefList = []
            for a in self.soup.find_all('a', href=True):
                #self.debuginfo("Found the url:", a['href'])
                hrefList.append(a['href'])
            '''
            emails = []
            emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", self.raw)
            duplicateLessEmails = []

            self.cleanedEmails = []

        return self.cleanedEmails

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/get_between.history', prefix='get_between', depth=1)
    def get_between(self, s, first, last ):
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return ''

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/tRight.history', prefix='tRight', depth=1)
    def tRight(self, string):
        s0 = str('{:.200}'.format(str(string)))
        #now pad 10 chars on each side
        s1 = str('{:>10}'.format(s0))
        return s1

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/tLeft.history', prefix='tLeft', depth=1)
    def tLeft(self, string):
        #first 10 chars only
        s0 = str('{:.200}'.format(str(string)))
        #now pad 10 chars on each side
        s1 = str('{:<10}'.format(s0))
        return s1

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/tCenter.history', prefix='tCenter', depth=1)
    def tCenter(self, string):
        #first 10 chars only
        s0 = str('{:.200}'.format(str(string)))
        #now pad 10 chars on each side
        s1 = str('{:^10}'.format(s0))
        return s1

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/displayThree.history', prefix='displayThree', depth=1)
    def displayThree(self, left, center, right):
        string = str(WebTools.tLeft(self, left) + " " + WebTools.tCenter(self, center) + " " + WebTools.tLeft(self, right))
        #self.debuginfo(string)
        return string

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/find_between.history', prefix='find_between', depth=1)
    def find_between(self, s, first, last ):
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return ''

    def get_list_from_file(self, filepath):
        listFromFile = []
        listFromFile.clear()
        working = True
        with open(str(filepath)) as fh:
            while working == True:
                for line in fh:
                    listFromFile.append(line.rstrip())
                working = False
        return listFromFile

    def check_for_duplicate_string_in_list(self, list, string):
        searching = True
        found = False
        while searching == True:
            for item in list:
                if len(item) == len(string):
                    if item == string:
                        found = True
                        searching = False
            searching = False
        return found


    def append_url_target(self, url, job_name):
        global _URL_TARGETS
        global _OLD_DOMAINS
        if not os.path.exists(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/old_domains_list.csv')):
            with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/old_domains_list.csv'), 'a') as f:
                f.close()
        #self.list = WebTools.get_list_from_file(self, str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/url_targets.csv'))
        if WebTools.check_for_duplicate_string_in_list(self, _URL_TARGETS, url) == False:
            if Tools.verify_hyperlink(self, url, job_name) == True:
                self.domain = ''
                self.domain = str(DatabaseTools.find_between(self, url, '//', '/'))
                searching_for_old_domain = True
                old_domain_found = False

                #self.old_domains_list = WebTools.get_list_from_file(self, str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/old_domains_list.csv'))
                searching_for_old_domain = True
                old_domain_found = False
                while searching_for_old_domain == True:
                    for old_domain in _OLD_DOMAINS:
                        if len(old_domain) == len(self.domain):
                            if old_domain == self.domain:
                                old_domain_found = True
                                searching_for_old_domain = False
                    searching_for_old_domain = False
                self.domain_count = 0
                if old_domain_found == False:
                    self.domain_count = 0
                else:
                    self.domain_count = 48
                self.include = True
                '''
                try:
                '''

                self.searching = True
                while self.searching == True:
                    for target_url in _URL_TARGETS:
                        if target_url.find(self.domain) != -1:
                            self.domain_count += 1
                        if self.domain_count > 48:
                            #self.old_domains_list = WebTools.get_list_from_file(self, str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/old_domains_list.csv'))
                            searching_for_old_domain = True
                            old_domain_found = False
                            while searching_for_old_domain == True:
                                for old_domain in _OLD_DOMAINS:
                                    if len(old_domain) == len(self.domain):
                                        if old_domain == self.domain:
                                            old_domain_found = True
                                            searching_for_old_domain = False
                                searching_for_old_domain = False

                            if old_domain_found == False:
                                '''
                                with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/old_domains_list.csv'), 'a') as iwrite:
                                    iwrite.write(self.domain)
                                    iwrite.write(str('\n'))
                                '''
                                _OLD_DOMAINS.append(self.domain)

                            self.include = False
                            self.searching = False
                    self.searching = False
                '''
                except:
                    self.include = False
                    eventlog('EXCEPTION: APPEND URL TARGET - ' + str(self.domain_count) + str(url))
                    pass
                '''
                if self.include == True:
                    #eventlog('|            NEW| ' + str(self.domain_count) + ' ' + str(url))
                    #eventlog('|            new| ' + str(url))
                    _URL_TARGETS.append(url)
                    '''
                    with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/url_targets.csv'), 'a') as iwrite:
                        iwrite.write(url)
                        iwrite.write(str('\n'))
                    '''
                '''
                else:
                    eventlog('|            OLD| ' + str(self.domain_count) + ' ' + str(url))
                '''
    '''
    def get_url_targets(self, job_name):
        
        def get_list_from_file():
            listFromFile = []
            listFromFile.clear()
            working = True
            with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/url_targets.csv')) as fh:
                while working == True:
                    for line in fh:
                        if Tools.verify_hyperlink(self, line, job_name) == True:
                            listFromFile.append(line.rstrip())
                    working = False
                #fh.close()
            return listFromFile

        url_targets = get_list_from_file()
        
        #with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/email_heap_full.csv'), 'a+')
            #iwrite.write(url)
            #iwrite.write(str('\n'))
        
        #with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/url_targets.csv'), 'w') as iwrite:
            #iwrite.close()
        return url_targets
    '''
    
    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/get_parsed_html.history', prefix='get_parsed_html', depth=1)
    def get_parsed_html(self, job_name, harvest_search_filepath, current_url, raw, path_directory, iresult, iFileIO):
        #sleep(3)
        #self.clear_screen()

        eventlog('def get_parsed_html')
        #sleep(3)
        self.search_links = []
        #import spacy
        #self.a_nlp = spacy.load('en_core_web_sm')
        #self.a_matcher = Matcher(self.a_nlp.vocab)
        
        self.soup = BeautifulSoup(str(raw), 'html.parser')
        self.pretty_sourceFP = str(path_directory + str(iresult) + '_pretty_index.html')
        self.prettify_soup = ''
        self.prettify_soup = self.soup.prettify()
        list_pretty = []
        #with open(self.pretty_sourceFP, 'w+') as iwrite:
            #eventlog('\n\nPRETTIFY\n\n' + str(self.prettify_soup) +'\n\nPRETTIFY\n\n')
            #iwrite.write(str(self.prettify_soup))
            #iwrite.write(str('\n'))
        list_pretty = self.prettify_soup.split('\n')


        #list_pretty = Tools.get_list_from_file(self, str(path_directory + str(iresult) + '_pretty_index.html'))
        self.matrix_name = 'parsed'
        eventlog('harvest_search_filepath: ' + str(harvest_search_filepath))
        if current_url.find('.google.') != -1:
            self.matrix_name = 'google_search_results'
            self.temporary_list = []
            if len(list_pretty) > 160 and len(list_pretty)  < 32200:
                for i in range(160, len(list_pretty)):
                    eventlog('list_pretty[' + str(i) +'] = ' + str(list_pretty[i]))
                    #sleep(0.001)
                    self.temporary_list.append( str(list_pretty[i]))
                list_pretty = []
                list_pretty = self.temporary_list
        self.englishFP = str(path_directory + str(iresult) + '_english.txt')
        self.hrefFP = str(path_directory + str(iresult) + '_href.html')
        with open(self.hrefFP, 'w+') as fhref:
            with open(self.englishFP, 'w+') as flang:
                #self.fhref = open(self.hrefFP, 'w+')
                #self.flang = open(self.englishFP, 'w+')

                #MATRIX
                #self.nlp = spacy.load("en_core_web_sm")
                self.sourcecode_line = 0
                self.href_index = 0
                self.lang_index = 0
                self.ent_index = 0

                list_pretty_index = []

                self.list_href = []
                self.list_href_index = []

                self.list_lang = []
                self.list_lang_index = []

                self.list_entity_index = []
                self.list_entity_text = []
                self.list_entity_label = []
                self.list_entity_start_char = []
                self.list_entity_end_char = []

                self.list_current_url = []
                self.list_date_recorded = []
                self.list_time_recorded = []
                self.list_html_filepath = []

                for line in list_pretty:
                    self.set_time = datetime.datetime.now()
                    self.entity_text = 'entity_text'
                    self.entity_label = 'entity_label'
                    self.entity_start_char = 'entity_start'
                    self.entity_end_char = 'entity_end_char'
                    self.lang = 'lang'
                    self.href = 'href'
                    self.b_found_href = False
                    self.b_found_lang = False
                    self.b_found_http_between = False
                    self.foundHttpBetween = ''
                    if line.find('http') != -1:
                        # eventlog('line with http: ' + str(line) )
                        try:
                            self.foundHttpBetween = WebTools.find_between(self, str(line), 'http', '"')
                            self.b_found_http_between = True
                        except:
                            self.b_found_http_between = False
                        #self.href = line
                        #self.b_found_href = True

                    if self.b_found_http_between == True:
                        if self.foundHttpBetween.find('w3.org') != -1:
                            self.b_found_http_between = False
                        if self.foundHttpBetween.find('googleusercontent') != -1:
                            self.b_found_http_between = False
                        if self.foundHttpBetween.find(';') != -1:
                            self.b_found_http_between = False
                        if self.foundHttpBetween.find(' ') != -1:
                            self.b_found_http_between = False

                    if self.b_found_http_between == True:
                        self.href = str('http' + str(self.foundHttpBetween))
                        self.b_found_href = True
                        self.left = str('|' + self.matrix_name + '|')
                        self.center = str('|href|')
                        self.right =  str(self.href)
                        terminal_string = WebTools.displayThree(self, self.left, self.center, self.right)
                        #eventlog(terminal_string)
                        #sleep(2)
                        fhref.write(self.href)
                        # eventlog('self.href = ' + str(self.href) )
                        fhref.write('\n')

                    #find language
                    if len(line) < 1500 and len(line) > 3:
                        if line.find('[') == -1 and line.find('<') == -1:
                            if line.find('{') == -1:
                                self.lang = line
                                if line.find(',') != -1:
                                    self.lang.replace(",", "")
                                self.b_found_lang = True
                                self.lang = line.replace(",", "")
                                self.lang = str(self.lang.lstrip())
                                self.lang = ' '.join(self.lang.split())
                                #eventlog(str(line))
                                self.left = str('|' + self.matrix_name + '|')
                                self.center = str('|lang| ')
                                self.right =  str(self.lang)
                                terminal_string = WebTools.displayThree(self, self.left, self.center, self.right)
                                #eventlog(terminal_string)
                                #self.lang = str(line)
                                flang.write(str(self.lang))
                                flang.write('\n')

                                #self.doc = self.a_nlp(str(self.lang))
                                words = self.lang.split()
                                for word in words:
                                    #eventlog(ent.text, ent.start_char, ent.end_char, ent.label_)
                                    self.left = str('\n|' + self.matrix_name + '| ')
                                    self.center = str('|entity_text| ' + str(word))
                                    self.right =  str('|entity_label| ' + str('ent.label_') + '|' )
                                    terminal_string = WebTools.displayThree(self, self.left, self.center, self.right)
                                    #eventlog(terminal_string)
                                    list_pretty_index.append(self.sourcecode_line)

                                    self.list_href_index.append(str(self.href_index))
                                    self.list_href.append(str(self.href))
                                    if Tools.verify_hyperlink(self, str(self.href), job_name) == True:
                                        WebTools.append_url_target(self, str(self.href), job_name)
                                        self.search_links.append(self.href)
                                        with open(harvest_search_filepath, 'a') as f:
                                            f.write(str(self.href))
                                            f.write('\n')

                                    self.list_lang_index.append(str(self.lang_index))
                                    self.list_lang.append(str(self.lang))

                                    #self.list_entity_index.append(str(self.ent_index))
                                    self.list_entity_index.append(str('self.ent_index'))
                                    
                                    #self.list_entity_text.append(str(ent.text))
                                    self.list_entity_text.append(str(word))
                                    
                                    #self.list_entity_label.append(str(ent.label_))
                                    self.list_entity_label.append(str('ent.label_'))
                                    
                                    #self.list_entity_start_char.append(str(ent.start_char))
                                    self.list_entity_start_char.append(str('ent.start_char'))
                                    
                                    #self.list_entity_end_char.append(str(ent.end_char))
                                    self.list_entity_end_char.append(str('ent.end_char'))
                                    
                                    self.list_current_url.append(str(current_url))
                                    self.list_date_recorded.append(str(self.set_time.strftime("%y_%m_%d")))
                                    self.list_time_recorded.append(str(self.set_time.strftime("%H_%M_%S")))
                                    self.list_html_filepath.append(str(path_directory + str(iresult) + '_pretty_index.html'))
                                    self.ent_index += 1
                                self.lang_index += 1

                    if self.b_found_href == True:
                        if self.b_found_lang == False:
                            list_pretty_index.append(self.sourcecode_line)
                            self.list_href_index.append(str(self.href_index))
                            self.list_href.append(str(self.href))
                            if Tools.verify_hyperlink(self, str(self.href), job_name) == True:
                                WebTools.append_url_target(self, str(self.href), job_name)
                                self.search_links.append(self.href)
                                with open(harvest_search_filepath, 'a') as f:
                                    # eventlog('Writing: ' + str(self.href))
                                    # self.charlotte.job_results.append_message(str(self.href))
                                    # self.charlotte.alice.send_message(str('Writing: ' + self.href), 'print')
                                    # eventlog('to: ' + str(harvest_search_filepath))
                                    f.write(str(self.href))
                                    f.write('\n')

                            self.list_lang_index.append(str(self.lang_index))
                            self.list_lang.append(str(self.lang))
                            
                            self.list_entity_index.append(str(self.ent_index))
                            self.list_entity_text.append(str(self.entity_text))
                            self.list_entity_label.append(str(self.entity_label))
                            self.list_entity_start_char.append(str(self.entity_start_char))
                            self.list_entity_end_char.append(str(self.entity_end_char))


                            self.list_current_url.append(str(current_url))
                            self.list_date_recorded.append(str(self.set_time.strftime("%y_%m_%d")))
                            self.list_time_recorded.append(str(self.set_time.strftime("%H_%M_%S")))
                            self.list_html_filepath.append(str(path_directory + str(iresult) + '_pretty_index.html'))
                        self.href_index += 1
                        #list_pretty_index.append(self.sourcecode_line)
                    self.sourcecode_line += 1


                self.columns = []
                self.columns.append(list_pretty_index)
                self.columns.append(self.list_href_index)
                self.columns.append(self.list_href)
                self.columns.append(self.list_lang_index)
                self.columns.append(self.list_lang)
                self.columns.append(self.list_entity_index)
                self.columns.append(self.list_entity_text)
                self.columns.append(self.list_entity_label)
                self.columns.append(self.list_entity_start_char)
                self.columns.append(self.list_entity_end_char)
                self.columns.append(self.list_current_url)
                self.columns.append(self.list_date_recorded)
                self.columns.append(self.list_time_recorded)
                self.columns.append(self.list_html_filepath)

                self.fields = [
                    'pretty_index', 'href_index', 'href', 'lang_index', 'lang', 'entity_index', 'entity_text', 'entity_label', 'entity_start', 'entity_end', 
                    'current_url', 'date_recorded', 'time_recorded', 'html_filepath']

                iFileIO.csv.write_list_of_lists_to_csv_file(self.columns, self.fields, self.matrix_name, path_directory, iresult)
                
                self.search_links = Tools.deduplicate_list(self, self.search_links)
                
                verified_links = []
                for link in self.search_links:
                    if Tools.verify_hyperlink(self, link, job_name) == True:
                        verified_links.append(str(link))
                        
                verified_links = Tools.shuffle_list(self, verified_links)
                verified_links = Tools.deduplicate_list(self, verified_links)
                with open(harvest_search_filepath, 'w') as f:
                    f.write(str(''))
                    f.close()
                    
                for link in verified_links:
                    with open(harvest_search_filepath, 'a') as f:
                        f.write(str(link))
                        f.write('\n')
                        f.close()
                return verified_links

    

    def make_web_browser(self):
        LOGGER.setLevel(logging.WARNING)
        logging.getLogger("urllib3").setLevel(logging.WARNING)
        chrome_options = webdriver.ChromeOptions()
        #https://cs.chromium.org/chromium/src/chrome/common/pref_names.cc
        prefs = {
            "profile.managed_default_content_settings.images":2,
            "download.default_directory": "NUL", 
            "download.prompt_for_download": False,
            "download_restrictions":3,
            
        }
        
        chrome_options.accept_untrusted_certs = True
        chrome_options.assume_untrusted_cert_issuer = True
        chrome_options.add_argument('--headless')
        #chrome_options.add_argument("--window-size=800,1200")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--disable-impl-side-painting")
        chrome_options.add_argument("--disable-setuid-sandbox")
        chrome_options.add_argument("--disable-seccomp-filter-sandbox")
        chrome_options.add_argument("--disable-breakpad")
        chrome_options.add_argument("--disable-client-side-phishing-detection")
        chrome_options.add_argument("--disable-cast")
        chrome_options.add_argument("--disable-cast-streaming-hw-encoding")
        chrome_options.add_argument("--disable-cloud-import")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-session-crashed-bubble")
        chrome_options.add_argument("--disable-ipv6")
        chrome_options.add_argument("--allow-http-screen-capture")
        chrome_options.add_argument("--start-maximized")
        

        ua = UserAgent()
        userAgent = ua.random
        chrome_options.add_argument(f'user-agent={userAgent}')
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(str(Path.home()) + '/p3env/alice/alice/spiders/chromedriver', chrome_options=chrome_options)
        sleep(1)
        return self.driver

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/job_search_results.history', prefix='job_search_results', depth=1)
    def job_search_results(self, job_name, searchKey, maxPages, maxLoops, job_path, iFileIO):
        eventlog('def job_search_results    ')
        # self.charlotte.alice.send_message('Building a list of websites related to: ' + str(searchKey), 'print')
        def get_list_from_file(filepath):
            listFromFile = []
            listFromFile.clear()
            working = True
            with open(str(filepath)) as fh:
                while working == True:
                    for line in fh:
                        #eventlog('INPUT: ' + str(line.rstrip()))
                        listFromFile.append(line.rstrip())
                    working = False
            return listFromFile
        
        eventlog(str(searchKey))
        self.driver = None
        search_form = None
        
        tryingSearch = True
        while tryingSearch:
            try:
                self.driver = WebTools.make_web_browser(self)
                WebTools.check_internet_connection(self)
                self.driver.get("https://duckduckgo.com")
                sleep(0.5)
                self.charlotte.alice.send_message('Loading search engine... ', 'print')
                search_form = self.driver.find_element_by_xpath('//*[@id="search_form_input_homepage"]')
                #search_form = self.driver.find_element_by_id('search_form_input_homepage')
                tryingSearch = False
            except:
                self.driver.quit()
                eventlog('SEARCH FORM FAILED FOR DUCK DUCK GO')
                sleep(15)

        #search_form = self.driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[1]/div/div[1]/input")
        results = []
        search_form.send_keys(searchKey)
        hyperlink_trigger_keys_filepath = str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/hyperlink_trigger_keys.csv'
        hyperlink_ignore_keys_filepath = str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/hyperlink_ignore_keys.csv'
        if os.path.exists(hyperlink_trigger_keys_filepath):
            pass
        else:
            iwrite = open(hyperlink_trigger_keys_filepath, 'a+')
            iwrite.write('trigger_key')
            iwrite.write('\n')
            iwrite.close()

        if os.path.exists(hyperlink_ignore_keys_filepath):
            pass
        else:
            iwrite = open(hyperlink_ignore_keys_filepath, 'a+')
            iwrite.write('ignore_key')
            iwrite.write('\n')
            iwrite.close()

        trigger_keys = get_list_from_file(hyperlink_trigger_keys_filepath)
        list_search_key = searchKey.split()

        for key in list_search_key:
            searching = True
            found = False
            while searching == True:
                for line in trigger_keys:
                    if line.find(str(key)) != -1:
                        found = True
                        searching = False
                searching = False
            if found == False:
                with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/hyperlink_trigger_keys.csv'), 'a') as f:
                    f.write(str(key))
                    f.write('\n')
        
        harvest_filename = ''
        previous_ch = ''
        for ch in str(searchKey):
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:;],.')
            if regex.search(ch) == None and ch != ' ':
                if ch.isdigit() == True:
                    harvest_filename += ch
                elif ch.isalpha() == True:
                    harvest_filename += ch
            previous_ch = ch
        
        #harvest_filename = searchKey.replace(' ', '_')
        
        search_phrase = searchKey
        harvest_search_filepath = str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + job_name + '/harvest/duck_duck_go/' + harvest_filename + '.csv')
        harvest_search_dir_path = str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + job_name + '/harvest/duck_duck_go')
        if not os.path.exists(harvest_search_dir_path):
            os.makedirs(harvest_search_dir_path)
        
        if not os.path.exists(harvest_search_filepath):
            iwrite = open(harvest_search_filepath, 'a+')
            # iwrite.write('trigger_key')
            iwrite.write('\n')
            iwrite.close()

        sleep(0.5)
        search_form_success = False
        try:
            search_form.submit()
            search_form_success = True
        except:
            search_form_success = False
            return False
        
        if search_form_success:


            sleep(0.5)
            searchKey = str("google_") + searchKey
            directory_key = None
            eventlog('job_name: ' + str(job_name))
            #sleep(2)
            website_root_path = DatabaseTools.make_job_paths(self, job_name)
            eventlog('website_root_path: ' + str(website_root_path))
            #sleep(2)
            #fp_url = "".join([c for c in website_target if c.isalpha() or c.isdigit() or c==' ']).rstrip()
            fp_url = ''
            previous_ch = ''
            for ch in str(self.driver.current_url):
                regex = re.compile('[@_!#$%^&*()<>?/\|}{~:;],.')
                if regex.search(ch) == None and ch != ' ':
                    if ch == '/' and previous_ch != '/':
                        fp_url += ch
                    elif ch.isdigit() == True:
                        fp_url += ch
                    elif ch.isalpha() == True:
                        fp_url += ch
                previous_ch = ch

            eventlog('fp_url: ' + str(fp_url))
            temp_string = "".join([c for c in str(self.driver.current_url) if c.isalpha() or c.isdigit() or c==' ']).rstrip()
            string = temp_string.replace(" ", "")
            eventlog('string: ' + str(string))

            if len(string) > 60:
                directory_key = str('{:.60}'.format(str(string)))
            else:
                directory_key = string

            eventlog('directory_key: ' + str(directory_key))

            if not os.path.exists( str( str(website_root_path) + 'web/' + str(fp_url) + '/')):
                os.makedirs( str( str(website_root_path) + 'web/' + str(fp_url) + '/'))

            iresult = 0
            dp_google_results =  str( str(website_root_path) + 'web/' + str(fp_url) + '/')
            matrix_name = str(directory_key)

            pathStart =  str( str(website_root_path) + 'web/' + str(fp_url)  + '/')
            pathEnd = "_index.html"
            raw = self.driver.page_source
            #WebTools.get_parsed_html(self, harvest_search_filepath, str(self.driver.current_url), raw, dp_google_results, iresult, iFileIO)
            iresult += 1
            loops = 0
            working = True
            self.newlinks = []
            while working == True:
                for i in range(1, maxPages):
                    loops += 1
                    if loops > maxLoops:
                        working = False
                        break
                    try:
                        eventlog(str( str(pathStart + str(iresult) + '_index.html')))
                        morePagesXpath = str("//*[@id='rld-" + str(i) + "']/a")
                        self.driver.find_element_by_xpath(morePagesXpath).click()
                        sleep(0.5)
                        # icount = iresult
                        # total = icount * 12
                        # self.charlotte.alice.send_message(str('Found ' + str(total) + ' websites...'))
                        raw = self.driver.page_source

                        #WebTools.get_parsed_html(self, harvest_search_filepath, str(self.driver.current_url), raw, dp_google_results, iresult, iFileIO)
                        iresult += 1
                    except Exception as e:
                        eventlog('EXCEPTION: ' + str(e))
                        eventlog(str('\n\n Processing fully extended duck duck go search page. \n\n ' + str(pathStart + str(iresult) + '_index.html' + '\nEXCEPTION\n\n ')))
                        #eventlog(str('\nEXCEPTION\n\n ' + str(pathStart + str(iresult) + '_index.html' + '\nEXCEPTION\n\n ')))
                        break
                working = False

            raw = self.driver.page_source

            self.newlinks = WebTools.get_parsed_html(self, job_name, harvest_search_filepath, str(self.driver.current_url), raw, dp_google_results, iresult, iFileIO)
            # for link in self.newlinks:
                # eventlog(str(WebTools.lineno(self) + ' SEARCHRESULT: ' + str(link)))

            self.driver.quit()
            b_success = True

            job_phrases_list = get_list_from_file(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_phrases.csv'))
            
            # write job phrase complete re-write job_phrases without the completed job phrase
            if len(self.newlinks) > 8:
                with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_phrases.csv'), 'w') as f:
                    with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_phrases_complete.csv'), 'a') as f_append:
                        for item in job_phrases_list:
                            if item != search_phrase:
                                f.write(str(item))
                                f.write('\n')
                            else:
                                f_append.write(str(item))
                                f_append.write('\n')

            return b_success, dp_google_results, directory_key, self.newlinks
        
        

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/navigate_url_queue.history', prefix='navigate_url_queue', depth=1)
    def navigate_url_queue(self, _Alice, job_name, iFileIO, website_targets):
        eventlog('navigate_url_queue')
        global _FINISH
        _FINISH = False
        global _HARVEST_COUNT
        _HARVEST_COUNT = 0
        self.charlotte.alice.send_message(' |  ---------------------------   ')
        self.charlotte.alice.send_message(' | DEMO RUNNING FOR LIMITED TIME  ')
        self.charlotte.alice.send_message(' | DEMO MAXIMUM THREADS = 4       ')
        self.charlotte.alice.send_message(' |  ---------------------------   ')

        class myThread (threading.Thread):
            def __init__(self, threadID, name, q, charlotte):
                threading.Thread.__init__(self)
                self.threadID = threadID
                self.name = name
                self.q = q
                self.list_debug_strings = []
                self.job_number = 0
                self.driver = None
                self.found_hyperlinks = []
                self.completed_hyperlinks = []
                self.known_chars = []
                self.exitFlag = 0
                self.living = True
                self.charlotte = charlotte
                '''
                self.read_page_source = None
                self.write_page_source = None
                self.write_english = None
                self.write_emails = None
                self.write_hyperlinks = None
                self.write_pretty_source = None
                self.f = None
                self.iwrite = None
                '''
                self.activated = True
                #self.processing = True

            def run(self):
                eventlog ("Starting " + self.name)

                thread = Thread(target = self.process_data, args = (self.name, self.q))
                thread.start()
                counting = True
                count = 0

                while counting and self.exitFlag == 0:
                    # eventlog(str(self.name) + ' count is ' + str(count) + ' search_key is ' + self.charlotte.search_key)
                    # eventlog(str(self.name) + ' count is ' + str(count) + ' command is ' + self.charlotte.state)
                    if count > 60:
                        counting = False
                    sleep(1)
                    count += 1
                    if str(self.charlotte.manager_state.value) == 'stop_search':
                        self.exitFlag = 1
                self.charlotte.state = 'shutting_down_webcrawler_threads'


                eventlog("thread finished...exiting")
                self.exitFlag = 1
                # exit()
                # self.process_data(self.name, self.q)

                eventlog("Exiting " + self.name)

            def t_history(self, string):
                pass

            def process_data(self, threadName, q):
                global _HARVEST_COUNT
                global _FINISH
                while True and self.exitFlag == 0:
                    if _FINISH:
                        eventlog(str(self.name) + ' IS FINISHED')
                        break
                    while self.activated == True:
                        self.exitFlag = 0
                        moreUrls = False
                        url = ''
                        try:
                            url = q.get()
                            if url == None:
                                #eventlog('url is None.')
                                self.exitFlag = 1
                            if len(url) < 15:
                                eventlog('url too short.')
                                self.exitFlag = 1
                        except:
                            self.exitFlag = 1

                        if self.exitFlag == 0:
                            self.known_chars.clear()
                            named_tuple = time.localtime() # get struct_time
                            time_string = time.strftime("%Y-%m-%d-%H:%M", named_tuple)
                            urlfront = ''
                            urlback = ''
                            self.urlshort = ''
                            if len(url) > 50:
                                urlfront = url[:25]
                                urlback = url [-25:]
                                self.urlshort = str('||' + str(urlfront) + '...' + str(urlback) + '||=- ')
                            else:
                                self.urlshort = '||'
                                for ch in url:
                                    self.urlshort += ch
                                missingCharsCount = 53 - len(url)

                                if missingCharsCount > 0:
                                    for i in range(0, missingCharsCount):
                                        self.urlshort += ' '
                                    self.urlshort += '||=- '

                            ##_THREADLOCK.release()
                            self.job_number += 1
                            #eventlog ("%s processing %s" % (threadName, url))

                            def verify_chars(chars):
                                valid = True
                                reason = ''
                                if len(chars) < 5:
                                    valid = False
                                    reason = 'length below 5'
                                elif chars.find('=') != -1:
                                    valid = False
                                    reason = '='
                                elif chars.find('-') != -1:
                                    valid = False
                                    reason = '-'
                                elif chars.find('</') != -1:
                                    valid = False
                                    reason = '</'
                                elif chars.find(';') != -1:
                                    valid = False
                                    reason = ';'
                                elif chars.find('widget') != -1:
                                    valid = False
                                    reason = 'widget'
                                elif chars.find('bottom') != -1:
                                    valid = False
                                    reason = 'bottom'
                                elif chars.find('copyright') != -1:
                                    valid = False
                                    reason = 'copyright'
                                elif chars.find('navigation') != -1:
                                    valid = False
                                    reason = 'navigation'
                                elif chars.find('header') != -1:
                                    valid = False
                                    reason = 'header'
                                elif chars.find('footer') != -1:
                                    valid = False
                                    reason = 'footer'
                                elif chars.find('linkedin') != -1:
                                    valid = False
                                    reason = 'linkedin'
                                elif chars.find('facebook') != -1:
                                    valid = False
                                    reason = 'facebook'
                                elif chars.find('youtube') != -1:
                                    valid = False
                                    reason = 'youtube'
                                elif chars.find('subscribe') != -1:
                                    valid = False
                                    reason = 'subscribe'
                                elif chars.find('text/') != -1:
                                    valid = False
                                    reason = 'text/'
                                elif chars.find('stylesheet') != -1:
                                    valid = False
                                    reason = 'stylesheet'
                                elif chars.find('_') != -1:
                                    valid = False
                                    reason = '_'
                                elif chars.find('dropdown') != -1:
                                    valid = False
                                    reason = 'dropdown'
                                elif chars.find('button') != -1:
                                    valid = False
                                    reason = 'button'
                                elif chars.find('search') != -1:
                                    valid = False
                                    reason = 'search'
                                elif chars.find('title') != -1:
                                    valid = False
                                    reason = 'title'
                                elif chars.find('view') != -1:
                                    valid = False
                                    reason = 'view'
                                elif chars.find('advert') != -1:
                                    valid = False
                                    reason = 'advert'
                                elif chars.find('instagram') != -1:
                                    valid = False
                                    reason = 'instagram'
                                elif chars.find('twitter') != -1:
                                    valid = False
                                    reason = 'twitter'
                                elif chars.find('clearfix') != -1:
                                    valid = False
                                    reason = 'clearfix'
                                elif chars.find('.edu') != -1:
                                    valid = False
                                    reason = '.edu'
                                elif chars.find('http') != -1:
                                    valid = False
                                    reason = 'http'
                                elif chars.find('px') != -1:
                                    valid = False
                                    reason = 'px'
                                elif chars.find('logo') != -1:
                                    valid = False
                                    reason = 'hidden'
                                elif chars.find('hidden') != -1:
                                    valid = False
                                    reason = 'hidden'
                                elif chars.find('icons') != -1:
                                    valid = False
                                    reason = 'icons'
                                elif chars.find('toggle') != -1:
                                    valid = False
                                    reason = 'toggle'
                                elif chars.find('checkbox') != -1:
                                    valid = False
                                    reason = 'checkbox'
                                elif chars.find('option') != -1:
                                    valid = False
                                    reason = 'option'
                                elif chars.find('wrapper') != -1:
                                    valid = False
                                    reason = 'wrapper'
                                elif chars.find('close') != -1:
                                    valid = False
                                    reason = 'close'
                                elif chars.find('click') != -1:
                                    valid = False
                                    reason = 'click'
                                elif chars.find('menu') != -1:
                                    valid = False
                                    reason = 'menu'
                                elif chars.find('nofollow') != -1:
                                    valid = False
                                    reason = 'nofollow'
                                elif chars.find('required') != -1:
                                    valid = False
                                    reason = 'required'
                                elif chars.find('<') != -1:
                                    valid = False
                                    reason = '<'
                                elif chars.find('submit') != -1:
                                    valid = False
                                    reason = '.edu'
                                elif chars.find('bullet') != -1:
                                    valid = False
                                    reason = 'bullet'
                                elif chars.find('map') != -1:
                                    valid = False
                                    reason = 'map'
                                elif chars.find('//') != -1:
                                    valid = False
                                    reason = '//'
                                elif chars.find('cookie') != -1:
                                    valid = False
                                    reason = 'cookie'
                                elif chars.find('noopener') != -1:
                                    valid = False
                                    reason = 'noopener'
                                elif chars.find('separator') != -1:
                                    valid = False
                                    reason = 'separator'
                                elif chars.find('.html') != -1:
                                    valid = False
                                    reason = '.html'
                                elif chars.find('scroll') != -1:
                                    valid = False
                                    reason = 'scroll'
                                elif chars.find('table') != -1:
                                    valid = False
                                    reason = 'table'
                                elif chars.find('tweet') != -1:
                                    valid = False
                                    reason = 'tweet'
                                elif chars.find('tooltip') != -1:
                                    valid = False
                                    reason = 'tooltip'
                                elif chars.find('privacy') != -1:
                                    valid = False
                                    reason = 'privacy'
                                elif chars.find('color') != -1:
                                    valid = False
                                    reason = 'color'
                                elif chars.find('container') != -1:
                                    valid = False
                                    reason = 'container'

                                for item in self.known_chars:
                                    if len(chars) == len(item):
                                        if chars == item:
                                            valid = False
                                            reason = 'DUPLICATE'
                                            break


                                return valid, reason

                            #@pysnooper.snoop(str(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/' + name + 'download_webpage_sourcecode.history'), prefix='download_webpage_sourcecode', depth=1)
                            def parse_url(url):
                                global _HARVEST_COUNT
                                #url = webQueue.get()
                                self.t_history('download_webpage_sourcecode: ' + str(url))

                                b_valid_url = True
                                raw = ''

                                if len(url) < 11:
                                    b_valid_url = False

                                if b_valid_url == True:
                                    try:
                                        pysnooper_url = ''
                                        pysnooper_url = url
                                        self.driver = WebTools.make_web_browser(self)
                                        WebTools.check_internet_connection(self)
                                        self.driver.get(url)
                                        self.driver.set_page_load_timeout(15)
                                        raw = self.driver.page_source
                                        b_valid_url = True
                                    except:
                                        self.t_history('failed get operation')
                                        b_valid_url = False

                                if b_valid_url == True:
                                    #website_directory = DatabaseTools.get_website_directory_filepath(self, job_name, str(self.name))
                                    #filepath_page_source = str(website_directory + 'pretty_source.html')
                                    #self.t_history(str(str('filepath_page_source:') + ' ' + str(filepath_page_source)))
                                    #self.soup = BeautifulSoup(str(raw), 'html.parser')
                                    #with open(filepath_page_source, 'w') as write_page_source:
                                        #write_page_source.write(str(raw))
                                    # self.charlotte.alice.send_message('Reading: ' + str(url), 'print')

                                    soup = None
                                    prettify_soup = ''
                                    list_pretty = []
                                    #with open(filepath_page_source) as read_page_source:
                                    soup = BeautifulSoup(str(raw), 'html.parser')
                                    prettify_soup = soup.prettify()
                                    list_pretty = prettify_soup.split('\n')

                                    list_english = []

                                    downloaded_and_wrote_english = False

                                    #self.t_history('ABOUT TO RUN FOR LINE IN LIST_PRETTY')
                                    ignored_toggle = False

                                    for dater in list_pretty:
                                        string = str(dater.strip())
                                        if string.find('<script') != -1 or string.find('<style') != -1:
                                            ignored_toggle = True
                                        if string == '</script>' or string == '</style>':
                                            ignored_toggle = False

                                        if ignored_toggle == False and len(string.strip()) < 750 and len(string.strip()) > 10:
                                            triggers = str('",:|/}{)(][')
                                            triggers += str("'")
                                            groups = []
                                            def tsplit(s, sep):
                                                stack = [s]
                                                for char in sep:
                                                    pieces = []
                                                    for substr in stack:
                                                        pieces.extend(substr.split(char))
                                                    stack = pieces
                                                return stack
                                            groups_prep = tsplit(string, triggers)
                                            for val in groups_prep:
                                                if len(val) > 4 and len(val) < 60:
                                                    groups.append(val)

                                            #with open(fp_webpage_english_ignored, 'a+')
                                            for item in groups:
                                                chars = str(item).strip().lower()
                                                b_english, reason = verify_chars(chars)

                                                if b_english == True:
                                                    self.known_chars.append(chars)
                                                    #write_english.write(chars)
                                                    #write_english.write('\n')
                                                    list_english.append(chars)
                                                    #self.t_history('included ' + str("| " + reason + " | ") + ' ' + str(chars) )
                                                    #eventlog(str(self.name) + str(self.urlshort) + str(chars))
                                                    downloaded_and_wrote_english = True
                                                else:
                                                    pass
                                                    #iwrite.write('ignored ' + str(" | " + reason + " | ") + ' ' + str(chars) )
                                                    #iwrite.write(str('\n'))
                                            #iwrite.close()


                                    #eventlog(str(self.name) + str(self.urlshort) + str('finished writing english'))

                                    #fp_webpage_hyperlinks = str(website_directory + 'pretty_hyperlinks.csv')
                                    #with open(fp_webpage_hyperlinks, 'w') as write_hyperlinks:
                                    #self.write_hyperlinks = open(fp_webpage_hyperlinks, 'w+')

                                    # record current url
                                    #write_hyperlinks.write(url)
                                    #write_hyperlinks.write('\n')

                                    for item in list_pretty:
                                        hyperlink = ''
                                        string = str(item)
                                        try:
                                            start = string.index( 'http' ) + len( 'http' )
                                            end = string.index( '"', start )
                                            hyperlink = str('http' + str(string[start:end]))
                                            valid_hyperlink = True

                                            if Tools.verify_hyperlink(self, item, job_name) == False:
                                                valid_hyperlink = False

                                            if valid_hyperlink == True:
                                                WebTools.append_url_target(self, str(hyperlink), job_name)
                                                #write_hyperlinks.write(str(hyperlink))
                                                #write_hyperlinks.write('\n')
                                                #self.t_history(str(hyperlink))
                                                #webQueue.put(item)
                                                self.found_hyperlinks.append(hyperlink)

                                        except:
                                            self.t_history('FAILED HYPERLINK ' + str(hyperlink))
                                            pass

                                    #self.write_hyperlinks.close()

                                    #fp_webpage_emails = str(website_directory + 'pretty_emails.csv')
                                    #self.write_emails = open(fp_webpage_emails, 'w+')
                                    list_webpage_emails = []
                                    #make emails
                                    english_list_index = 0

                                    for item in list_english:
                                        emails = []
                                        emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", str(item))
                                        if emails:
                                            for email in emails:
                                                valid_email = True
                                                if valid_email == True:
                                                    valid_email, reason = Tools.verify_email(self, job_name, email)
                                                    if valid_email == False:
                                                        self.t_history('INVALID EMAIL, REASON: ' + str(reason))

                                                if valid_email == True:
                                                    if os.path.exists(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/email_heap.csv')):
                                                        if valid_email == True:
                                                            with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/email_heap.csv')) as f:
                                                                while True:
                                                                    line = f.readline()
                                                                    if line == '':
                                                                        break
                                                                    #if str(line.rstrip()).find(email) != -1:
                                                                    if str(line.rstrip()) == str(email):
                                                                        valid_email = False
                                                                        break
                                                                    #website_targets.append(line.rstrip())

                                                if valid_email == True:
                                                    is_valid = pyisemail.is_email(str(email), check_dns=True)
                                                    if is_valid == True:
                                                        #self.t_history(content)
                                                        emailcount = WebTools.file_len(self, str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/email_heap.csv'))
                                                        #_THREADLOCK.acquire()
                                                        with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/email_heap.csv'), 'a') as iwrite:
                                                            iwrite.write(str(email))
                                                            iwrite.write(str('\n'))
                                                            _HARVEST_COUNT += 1
                                                        #_THREADLOCK.release()
                                                        #self.iwrite.close()
                                                        #WebTools.clear_screen(self)
                                                        eventlog('FOUND EMAIL: ' + str(email) + ' Total: ' + str(emailcount))
                                                        # self.charlotte.spider_log('FOUND EMAIL: ' + str(email))
                                                        # self.charlotte.job_results.append_email(str(email))
                                                        self.charlotte.alice.send_message(' | FOUND EMAIL | >> ' + str(email) + ' <<', 'print')
                                                        
                                                        english_above_email_index = english_list_index - 25
                                                        if english_above_email_index < 0:
                                                            english_above_email_index = 0
                                                        english_below_email_index = english_list_index + 25
                                                        if english_below_email_index > len(list_english):
                                                            english_below_email_index = len(list_english)

                                                        for i in range(english_above_email_index, english_below_email_index):
                                                            #self.doc = self.nlp(str(list_english[i]))
                                                            #content = str(str(email) + ',' + str(list_english[i]) + ',' + str(url) + ',' + str(fp_webpage_pretty_index))
                                                            content = str(str(email) + ',' + str(list_english[i]) + ',' + str(url))
                                                            #write_emails.write(str(email) + ',' + str(list_english[i] + ' ' +  str(self.doc.ents.label_)) + ',' + url + ',' + str(fp_webpage_pretty_index))
                                                            list_webpage_emails.append(content)
                                                            #write_emails.write(content)
                                                            #write_emails.write('\n')
                                                            #self.t_history(str(email) + ',' + str(list_english[i]) + ',' + url + ',' + str(fp_webpage_pretty_index))
                                                            named_tuple = time.localtime() # get struct_time
                                                            time_string = time.strftime("%Y-%m-%d", named_tuple)
                                                            if not os.path.exists(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/contacts/emails/daily/')):
                                                                os.makedirs( str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/contacts/emails/daily/'))
                                                            with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/contacts/emails/daily/email_heap_full_' + time_string + '.csv'), 'a') as iwrite:
                                                                iwrite.write(content)
                                                                iwrite.write(str('\n'))
                                                            #self.iwrite.close()
                                        english_list_index += 1

                                    #self.write_emails.close()

                                    if downloaded_and_wrote_english == True:
                                        named_tuple = time.localtime() # get struct_time
                                        time_string = time.strftime("%Y-%m-%d", named_tuple)
                                        if not os.path.exists(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/url_queue_complete/daily/')):
                                            os.makedirs( str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/url_queue_complete/daily/'))

                                        #self.t_history(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/url_queue_complete/daily/' + str(time_string) +  '_url_queue_complete.csv'))
                                        #self.t_history(url)
                                        #_THREADLOCK.acquire()
                                        with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/url_queue_complete/daily/' + str(time_string) +  '_url_queue_complete.csv'), 'a') as iwrite:
                                            iwrite.write(url)
                                            iwrite.write(str('\n'))
                                            _HARVEST_COUNT += 1
                                        #_THREADLOCK.release()
                                        self.completed_hyperlinks.append(str(url))
                                        eventlog(str('| COMPLETED URL | ' + str(url)))
                                        dater = (url[:50] + '...') if len(url) > 50 else url
                                        self.charlotte.alice.send_message('reading: ' + str(dater), 'print')
                                        if str(self.charlotte.manager_state.value) == 'shutting_down_webcrawler_threads':
                                            self.exitFlag = 1

                                    #self.write_pretty_source.close()
                                    #self.read_page_source.close()
                                    #read_pretty_index.close()
                                    ##WebTools.clear_screen(self)
                                    #q.task_done()
                                else:
                                    self.t_history('INVALID URL ' + str(url) )
                                    if not os.path.exists(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name))):
                                        os.makedirs( str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/'))
                                    '''
                                    self.f = open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/url_FAILED.csv'), 'a+')
                                    self.f.write(str(url))
                                    self.f.write('\n')
                                    self.f.close()
                                    '''
                                    self.exitFlag = 1
                                    #self.driver.get('https://www.google.com/')
                                    #q.task_done()

                            parse_url(url)
                            try:
                                self.driver.quit()
                            except:
                                eventlog('self.driver.quit failed: ' + str(self.name) + ' ' +  str(WebTools.lineno(self)))
                            ##WebTools.clear_screen(self)
                        


        if not os.path.exists( str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/')):
            os.makedirs( str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/'))

        webQueue = queue.Queue()


        # Fill the queue
        ##_THREADLOCK.acquire()
        maxSearchLoops = 0
        for item in website_targets:
            webQueue.put(item)


        threadID = 1

        # Create new self.threads
        threadcount = len(website_targets)
        if threadcount > 8:
            threadcount = 8

        self.threads = []
        self.pool = ThreadPool(processes=threadcount)

        for i in range(0, threadcount):
            prefix = ''
            if i < 10:
                prefix = 'T00'
            elif i < 100:
                prefix = 'T0'
            else:
                prefix = 'T'

            tName = (str(prefix) + str(i))
            thread = myThread(threadID, tName, webQueue, self.charlotte)
            self.pool.apply_async(thread)
            try:
                thread.daemon = True
                
                self.threads.append(thread)
                thread.start()
                threadID += 1
            except:
                sleep(0.05)
                try:
                    thread.daemon = True
                    self.threads.append(thread)
                    thread.start()
                    
                    threadID += 1
                except:
                    eventlog('could not start thread, thread deleted.')
                    del thread
            sleep(0.05)

        # Wait for queue to empty
        searchingloop = 0
        notifyloop = 0
        self.activeThreads = True
        #while searchingloop < maxSearchLoops and not webQueue.empty():
        new_links = []
        completed_links = []
        def get_list_from_file(filepath):
            listFromFile = []
            listFromFile.clear()
            working = True
            with open(str(filepath)) as fh:
                while working == True:
                    for line in fh:
                        #eventlog('INPUT: ' + str(line.rstrip()))
                        listFromFile.append(line.rstrip())
                    working = False
                fh.close()
            return listFromFile
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%Y-%m-%d", named_tuple)
        if not os.path.exists(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/url_queue_complete/daily/' + str(time_string) +  '_url_queue_complete.csv')):
            with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/url_queue_complete/daily/' + str(time_string) +  '_url_queue_complete.csv'), 'a+') as f:
                #f = open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/url_queue_complete/daily/' + str(time_string) +  '_url_queue_complete.csv'), 'a+')
                f.write('')
                f.write('\n')
                f.close()

        #previous_list_completed_urls = get_list_from_file(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/url_queue_complete/daily/' + str(time_string) +  '_url_queue_complete.csv'))
        #previous_list_completed_emails = get_list_from_file(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/email_heap.csv'))
        previous_harvest = _HARVEST_COUNT

        harvest_timer = 0
        eventlog('active threads loop begin')
        while self.activeThreads == True:
            
            finished = True
            searching = True
            t_count_processing = 0
            t_count_total = 0
            if str(self.charlotte.manager_state.value) == 'shutting_down_webcrawler_threads':
                for t in self.threads:
                    eventlog('webtools is setting ' + str(t.name) + ' exitFlag to 1.')
                    t.exitFlag = 1


            while searching == True:
                for t in self.threads:
                    t_count_total += 1
                    if t.exitFlag == 0:
                        t_count_processing += 1

                for t in self.threads:
                    #eventlog(str(t.name) + ' ||| exitFlag = -------  ' + str(t.exitFlag) + '  -------   |||')
                    if t.exitFlag == 0:
                        finished = False
                        searching = False
                searching = False

            named_tuple = time.localtime() # get struct_time
            time_string = time.strftime("%Y-%m-%d", named_tuple)
            #current_list_completed_urls = get_list_from_file(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/url_queue_complete/daily/' + str(time_string) +  '_url_queue_complete.csv'))
            #current_list_completed_emails = get_list_from_file(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/email_heap.csv'))
            current_harvest = _HARVEST_COUNT
            WebTools.check_internet_connection(self)

            harvest_timer += 5
            if harvest_timer >= 30:
                harvest_timer = 0
                change = current_harvest - previous_harvest
                poor_harvest = False
                if change < 5:
                    poor_harvest = True
                if finished == True or poor_harvest == True or str(self.charlotte.manager_state.value) == 'stop_search' or str(self.charlotte.state) == 'shutting_down_webcrawler_threads':
                    #WebTools.clear_screen(self)
                    eventlog('finished = ' + str(finished))
                    eventlog('poor_harvest = ' + str(poor_harvest))
                    eventlog('str(self.charlotte.manager_state.value): ' +str(self.charlotte.manager_state.value))
                    eventlog(' ------  CLOSING BROWSERS. --------')
                    self.activeThreads = False
                else:
                    change = current_harvest - previous_harvest
                    eventlog('| Harvest/secs  | ' + str(change) + ' harvests / 30 seconds.')
                    if not os.path.exists(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/daily/')):
                        os.makedirs( str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/daily/'))

                    if not os.path.exists(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/daily/' + str(time_string) +  '_HARVEST_COUNT.csv')):
                        with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/daily/' + str(time_string) +  '_HARVEST_COUNT.csv'), 'a') as f:
                            f.close()

                    named_tuple = time.localtime() # get struct_time
                    timestamp = time.strftime("%Y-%m-%d-%H-%M-%S", named_tuple)
                    with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/daily/' + str(time_string) +  '_HARVEST_COUNT.csv'), 'a') as f:
                        f.write(str(change) + ','+ str(timestamp))
                        f.write('\n')

                    previous_harvest = _HARVEST_COUNT
            else:
                # for t in self.threads:
                #     if t.exitFlag == 1:
                #         t.processing = True
                # eventlog('| working/total | ' + str(t_count_processing) + '/' + str(t_count_total))
                eventlog(str('Working internet browsers: ' + str(t_count_processing) + ' of ' + str(t_count_total)))
                self.charlotte.alice.send_message(str('Working Internet Browsers: ' + str(t_count_processing) + ' of ' + str(t_count_total)))
                sleep(5)

        eventlog('active threads loop end')

        eventlog('ACTIVE threads IS FAlSE')

        clearing_queue = True
        while clearing_queue == True: 
            eventlog('clearing_queue')
            try:
                url = q.get()
                eventlog('CLEARING ' + str(url))
                if url == None:
                    #eventlog('url is None.')
                    clearing_queue = False
            except:
                eventlog('EXCEPTION:   q.get() of clearing_queue failed')
                clearing_queue = False

        for t in self.threads:
            t.activated = False
            eventlog(str(t.name) + ' activated: ' + str(t.activated))

        sleep(1)

        with webQueue.mutex:
            webQueue.queue.clear()
            eventlog('with webQueue.mutex: clear complete')

        for t in self.threads:
            threadname = str(t.name)
            eventlog(threadname + ' for t in self.threads:')
            with t.q.mutex:
                t.q.queue.clear()
                eventlog(threadname + ' with webQueue.mutex: clear complete')

        _FINISH = True
        sleep(1)
        eventlog('closing pool')
        self.pool.close()
        eventlog('joining pool')
        self.pool.join()
        sleep(1)
        del self.threads
        del self.pool
        eventlog('webQueue.task_done()')
        webQueue.task_done()
        sleep(1)
        del webQueue
        eventlog ("Finished browsing hyperlinks")
        self.charlotte.update_state('finished_browsing_hyperlinks')
        self.charlotte.alice.update_state('finished_browsing_hyperlinks')
        # self.charlotte.alice.alive = False
        self.charlotte.alice.send_message(str('Internet browsers have finished working...'))
        self.charlotte.update_state('stop_search')
        self.charlotte.alice.send_message(message='initialized', command='update_state')

        sleep(1)

        return new_links, completed_links

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/getNewLinks.history', prefix='getNewLinks', depth=1)
    def getNewLinks(self, inlinks, completed_hyperlinks, job_name, _Alice):
        global _URL_TARGETS
        eventlog('PROCESSING URL NEW TARGETS')
        #f = open(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/getNewLinks.history', 'w+')
        #f.write('')
        #f.write('\n')
        #f.close()
        ##WebTools.clear_screen(self)
        # for link in inlinks:
        #     eventlog('inlinks: ' + str(link))
        
        
        def get_list_from_file(filepath):
            listFromFile = []
            listFromFile.clear()
            working = True
            fh = open(str(filepath))
            while working == True:
                for line in fh:
                    #eventlog('INPUT: ' + str(line.rstrip()))
                    listFromFile.append(line.rstrip())
                working = False
            fh.close()
            return listFromFile

        #remove duplicates from links passed to this function and save them to input list
        inputlist = []
        #load url targets written from self.threads from file into memory
        #inurl_targets = []
        #inurl_targets = WebTools.get_url_targets(self, job_name)
        _URL_TARGETS = DatabaseTools.getListWithoutDuplicates(self, _URL_TARGETS)
        for target in _URL_TARGETS:
            inlinks.append(str(target))
        inlinks = DatabaseTools.getListWithoutDuplicates(self, inlinks)
        for somelink in inlinks:
            if Tools.verify_hyperlink(self, somelink, job_name) == True:
                #eventlog('from memory INLINKS = ' + str(somelink))
                inputlist.append(somelink)
        _URL_TARGETS.clear()
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%Y-%m-%d", named_tuple)

        if not os.path.exists(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/url_queue_complete/daily/')):
            os.makedirs( str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/url_queue_complete/daily/'))

        if not os.path.exists(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/url_queue_complete/daily/' + str(time_string) +  '_url_queue_complete.csv')):
            f = open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/url_queue_complete/daily/' + str(time_string) +  '_url_queue_complete.csv'), 'a+')
            f.close()


        list_completed_hyperlinks = get_list_from_file(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/url_queue_complete/daily/' + str(time_string) +  '_url_queue_complete.csv'))
        #update count of visited domains and create a blacklist
        updated_known_domains = []

        list_completed_domains = []

        for somelink in list_completed_hyperlinks:
            domain = str(DatabaseTools.find_between(self, somelink, '//', '/'))
            list_completed_domains.append(domain)

        list_unique_domains = []
        for domain in list_completed_domains:
            append_domain = True
            searching = True
            while searching == True:
                for unique_domain in list_unique_domains:
                    if len(domain) == len(unique_domain):
                        if domain == unique_domain:
                            append_domain = False
                            searching = False
                searching = False
            if append_domain == True:
                list_unique_domains.append(domain)


        new_dict_domain_count = Counter(list_completed_domains)
        f = open(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + job_name + '/new_dict_domain_counts.csv', 'w+')
        for key, value in new_dict_domain_count.items():
            f.write(str(str(key) + ',' + str(value) ))
            f.write('\n')
        f.close()

        inputlist = DatabaseTools.getListWithoutDuplicates(self, inputlist)
        new_input_list = []
        for incoming_hyperlink in inputlist:
            i_domain = str(DatabaseTools.find_between(self, incoming_hyperlink, '//', '/'))
            searching = True
            found = False
            while searching == True:
                for key, value in new_dict_domain_count.items():
                    domain = key
                    count = value
                    if len(domain) == len(i_domain):
                        if domain == i_domain:
                            if count < 64:
                                new_input_list.append(incoming_hyperlink)
                                found = True
                                searching = False
                                break
                searching = False

            if found == False:
                new_input_list.append(incoming_hyperlink)
            # else:
            #     eventlog('Visited too many times: ' + str(incoming_hyperlink))

        inputlist = new_input_list
        #clean duplicates from newlinks passed into this function - shuffle them too
        for i in range(len(inputlist)):
            swap = randint(0,len(inputlist)-1)
            temp = inputlist[swap]
            inputlist[swap] = inputlist[i]
            inputlist[i] = temp
        f.close()
        completed_hyperlinks = DatabaseTools.getListWithoutDuplicates(self, completed_hyperlinks)

        # for item in inputlist:
        #     eventlog('INPUT LIST: ' + str(item))

        return inputlist

    def harvest_newLinks_given_explicit_keys(self, newLinks, job_name):
        #explicit_keys = ['medical', 'about', 'health', 'ceo', 'critical', 'cfo', 'financial', 'director', 'chief', 'contact', 'staff', 'member' ]
        eventlog('DEF HARVEST NEW LINKS GIVEN EXPLICIT KEYS')
        def get_list_from_file(filepath):
            listFromFile = []
            listFromFile.clear()
            working = True
            fh = open(str(filepath))
            while working == True:
                for line in fh:
                    #eventlog('INPUT: ' + str(line.rstrip()))
                    listFromFile.append(line.rstrip())
                working = False
            fh.close()
            return listFromFile

        hyperlink_trigger_keys = get_list_from_file(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/hyperlink_trigger_keys.csv')
        goodLinks = []
        hyperlink_ignore_keys = get_list_from_file(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/hyperlink_ignore_keys.csv')
        good_domains = []
        # for item in newLinks:
        #     eventlog('harvest newLinks: ' + str(item) )

        for item in newLinks:
            searching = True
            good = True
            '''
            while searching == True:
                for trigger in hyperlink_trigger_keys:
                    if str(item).find(str(trigger)) != -1:
                        good = True
                        searching = False
                        break
                searching = False
            '''
            searching = True
            while searching == True:
                for trigger in hyperlink_ignore_keys:
                    if len(trigger) > 0:
                        if str(item).find(str(trigger)) != -1:
                            good = False
                            searching = False
                            break
                searching = False

            if good == True:
                goodLinks.append(str(item))
                d = str(DatabaseTools.find_between(self, item, '//', '/'))
                good_domains.append(d)
                # eventlog('goodLink: ' + str(item))
                # eventlog('good_domain: ' + d)


        for i in range(len(goodLinks)):
            swap = randint(0,len(goodLinks)-1)
            temp = goodLinks[swap]
            goodLinks[swap] = goodLinks[i]
            goodLinks[i] = temp

        good_clean_filtered_links = []
        new_dict_domain_count = Counter(good_domains)
        f = open(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/goodLinks.csv', 'w+')
        for incoming_hyperlink in goodLinks:
            i_domain = str(DatabaseTools.find_between(self, incoming_hyperlink, '//', '/'))
            searching = True
            #self.found = False
            while searching == True:
                for key, value in new_dict_domain_count.items():
                    domain = key
                    count = value
                    if len(domain) == len(i_domain):
                        if domain == i_domain:
                            if count < 64:
                                good_clean_filtered_links.append(incoming_hyperlink)
                                # eventlog('GOOD LINK: ' + str(incoming_hyperlink))
                                #self.found = True
                                f.write(str(incoming_hyperlink))
                                f.write('\n')
                                searching = False
                            else:
                                eventlog('BAD LINK: ' + str(incoming_hyperlink))
                                break
                searching = False
        f.close()
        return good_clean_filtered_links

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


    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/job_navigate_results.history', prefix='job_navigate_results', depth=1)
    def job_navigate_results(self, _Alice, job_name, website_targets, iFileIO):


        
        if not os.path.exists(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/email_heap.csv')):
            with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/email_heap.csv'), 'a') as f:
                f.close()

        # for item in website_targets:
        #     eventlog('website_target = ' + str(item))

        completed_hyperlinks = []
        links = website_targets

        # for link in links:
        #     eventlog(str(WebTools.lineno(self)) + ' link: ' + str(link))

        newLinks = WebTools.getNewLinks(self, links, completed_hyperlinks, job_name, _Alice)
        goodLinks = WebTools.harvest_newLinks_given_explicit_keys(self, newLinks, job_name)
        
        #level 1
        if len(goodLinks) > 0:
            #WebTools.clear_screen(self)
            eventlog('++++++++++++++ LEVEL 1 ++++++++++++++')
            self.charlotte.alice.send_message('++++++++++++++ LEVEL 1 ++++++++++++++')
            WebTools.check_internet_connection(self)
            links, completed_hyperlinks = WebTools.navigate_url_queue(self, _Alice, job_name, iFileIO, goodLinks)
            newLinks = WebTools.getNewLinks(self, links, completed_hyperlinks, job_name, _Alice)
            goodLinks = WebTools.harvest_newLinks_given_explicit_keys(self, newLinks, job_name)
            # self.charlotte.state = 'search'

            #level 2
            if len(goodLinks) > 0 and str(self.charlotte.manager_state.value) == 'search':
                #WebTools.clear_screen(self)
                eventlog('++++++++++++++ LEVEL 2 ++++++++++++++')
                self.charlotte.alice.send_message('++++++++++++++ LEVEL 2 ++++++++++++++')
                WebTools.check_internet_connection(self)
                links, completed_hyperlinks = WebTools.navigate_url_queue(self, _Alice, job_name, iFileIO, goodLinks)
                newLinks = WebTools.getNewLinks(self, links, completed_hyperlinks, job_name, _Alice)
                goodLinks = WebTools.harvest_newLinks_given_explicit_keys(self, newLinks, job_name)
                # self.charlotte.state = 'search'

        self.charlotte.state = 'finished_browsing_hyperlinks'
        

            

#####################################################################################################################################

#################################################################################################################################################
#################################################################################################################################################
#  `|```````````\````````````````````|````````````````````|``````````````\````````/```````````````````````````````
#  `o````````````\__________________`o`__________________`|```````````````\````/`/````````````````````````````````
#  `|````````````/\``````````````````|``````````````````/\```````````````````/````````````````````````````````````
#  `|```````````/``\`````````````````|`````````````````/``\`````````````````/`````````````````````````````````````
#  `o``````````/````\````````````````o``````````````o`/````\`````````````/`/``````````````````````````````````````
#  `|``````/`````````\```````````````|``````````````|```````\``````````/``````````````````````````````````````````
#  `|`````/```````````\``````````````|``````````````|````````\````````/```````````````````````````````````````````
#  `o````/`````````````\`````````````o``````````````|`````````\````/`/````````````````````````````````````````````
#  `|```/```````````````\````````````|``````````````|````````````/````````````````````````````````````````````````
#  `|``/`````````````````\```````````|``````````````|```````````/`````````````````````````````````````````````````
#  `o`/```````````````````\_________`o`____________`|````````/`/``````````````````````````````````````````````````
#  `|``````````````````/```\`````````|``````````\|/\```````/``````````````````````````````````````````````````````
#  `|`````````````````/`````\````````|``````````-*-`\`````/```````````````````````````````````````````````````````
#  `o````````````````/```````\```___`o`______```/|\``\`/`/````````````````````````````````````````````````````````
#  `|``````````````|``````````\``````|```````\```````/````````````````````````````````````````````````````````````
#  `|``````````````|```````````\`````|````````\`````/`````````````````````````````````````````````````````````````
#  `o``````````````o````````````\````o`````````\`/`/``````````````````````````````````````````````````````````````
#  `|``````````````|````````|````\```|`````````/``````````````````````````````````````````````````````````````````
#  `|``````````````|````````|`````\``|````````/```````````````````````````````````````````````````````````````````
#  `o``````````````o````````|``````\`o`````/`/````````````````````````````````````````````````````````````````````
#  `|``````````````````````````````/``````````````````````````````````````````````````````````````````````````````
#  `|`-------------------------------|/``/````````````````````````````````````````````````````````````````````````
#  `o````````````````````````````````|\`/`````````````````````````````````````````````````````````````````````````
#  `|``````````````|````````|`````````/`|`````````````````````````````````````````````````````````````````````````
#  `|``````````````|````````|````````/``|`````````````````````````````````````````````````````````````````````````
#  `o``````````````o`````/``o```````/```|`````````````````````````````````````````````````````````````````````````
#  `|``````````````|```/```````````/````|`````````````````````````````````````````````````````````````````````````
#  `|``````````````|``/```````````/`````|`````````````````````````````````````````````````````````````````````````
#  `o``````````````o`/```````````/``````|`````````````````````````````````````````````````````````````````````````
#  `|````````````/```\``````````/```````|`````````````````````````````````````````````````````````````````````````
#  `|```````````/`````\````````/````````|`````````````````````````````````````````````````````````````````````````
#  `o``````````/```````\``````/`````````|`````````````````````````````````````````````````````````````````````````
#  `|`\```````/`````````\````/``````````|`````````````````````````````````````````````````````````````````````````
#  `|``\`````/```````````\``/```````````|`````````````````````````````````````````````````````````````````````````
#  `o```\`o`/`````````````\/````````````|`````````````````````````````````````````````````````````````````````````
#  `|```/\````````````````/`````````````|`````````````````````````````````````````````````````````````````````````
#  `|``/``\``````````````/``````````````|`````````````````````````````````````````````````````````````````````````
#  `o`/````\````````````/```````````````|`````````````````````````````````````````````````````````````````````````
#  `|```````\``````````/``````````````````````````````````````````````````````````````````````````````````````````
#  `|````````\````````/`````````````````_`````````````````````````````````````````````````````````````````````````
#  `o`````````\``````/```````````````o`(_)`o``````````````````````````````````````````````````````````````````````
#  `|``````````\````/````````````````o``_``o``````````````````````````````````````````````````````````````````````
#  `|```````````\``/```````````````````/`\````````````````````````````````````````````````````````````````````````
#  `o````````````\/``````````````````o`\_/`o``````````````````````````````````````````````````````````````````````
#  `|````````````/`````````````````````|`|````````````````````````````````````````````````````````````````````````
#  `|```````````/`````````````````````````````````````````````````````````````````````````````````````````````````



    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='getCleanurls', depth=1)
    def getCleanurls(self, theList, list_ignore):
        validurlList = []
        duplicateLessList = DatabaseTools.getListWithoutDuplicates(self, theList)
        for item in duplicateLessList:
            if WebTools.validate_url(self, item, list_ignore):
                #self.debuginfo(" VALID unique url: " + item)
                validurlList.append(item)
            else:
                self.debuginfo(" INVALID unique url: " + item)
        return validurlList

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='getHrefList', depth=1)
    def getHrefList(self, raw):
        self.soupyhrefs = BeautifulSoup(raw, "lxml")
        self.hrefList = []
        self.xpaths = []
        for a in self.soupyhrefs.find_all('a', href=True):
            #self.debuginfo(str("Found the url:" + a['href']))
            self.hrefList.append(a['href'])
        for link in self.hrefList:
            if link[0] == '/':
                self.xpaths.append(link)
        return self.hrefList, self.xpaths

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='soupGetTitle', depth=1)
    def soupGetTitle(self, data, siteLink):
        if data.find("title") != -1:
            #self.debuginfo(str(siteLink))
            #self.debuginfo("\n +++++ FOUND ++++ " + data + " +++++ FOUND ++++ \n")
            #sleep(0.01)
            if str(DatabaseTools.find_between(self, data, '"', '"')) != '':
                data = str(DatabaseTools.find_between(self, data, '"', '"'))
            if str(data).find(",") != -1:
                data = str(data).replace(",", "")
            if str(DatabaseTools.find_between(self, data, '>', '<')) != '':
                data = str(DatabaseTools.find_between(self, data, '>', '<'))
            if str(data).find("&amp;") != -1:
                data = str(data).replace("&amp;", "")
            #if self.soupGetPhone(data, siteLink):
                ##self.debuginfo("soupGetPhone() " + self.soupGetPhone(data, siteLink))
                #sleep(0.01)
            return True, data
        else:
            return False, data
