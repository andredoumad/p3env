import os, sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
print('SCRIPT_DIR: ' + str(SCRIPT_DIR))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
LOOP = None
WS = None
SWITCHBOARD = None
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
# import ALICEINWONDERLAND
# from .ALICEINWONDERLAND import ALICEINWONDERLAND
from AliceRequiredModules import *
from ALICEINWONDERLAND import AliceInWonderland
from chronos import Chronos
from databasetools import DatabaseTools
from fileio import FileIO
from webtools import WebTools
from standalone_tools import *

# from .chronos import Chronos
# from .databasetools import DatabaseTools
# from .fileio import FileIO
# from .webtools import WebTools
# from .standalone_tools import *


if os.path.exists( str(os.getcwd() + '/pysnooper')):
    shutil.rmtree( str(os.getcwd() + '/pysnooper'))
os.makedirs( str(os.getcwd() + '/pysnooper'))

if os.path.exists( str(os.getcwd() + '/auto_cleared_history')):
    shutil.rmtree( str(os.getcwd() + '/auto_cleared_history'))
os.makedirs( str(os.getcwd() + '/auto_cleared_history'))

Reportfilepath  = str(os.getcwd() + '/DATABASE/memories/Report.xlsx')
if not os.path.exists( os.getcwd() + '/DATABASE/memories/history'):
    os.makedirs( str(os.getcwd() + '/DATABASE/memories/history'))
#Report = xlsxwriter.Workbook(Reportfilepath)
cwd=spidersDirectoryPath=spidersParentDirectoryPath=dataPath=chromedriverFilePath = None
sourceCodeFileName = str(str(getframeinfo(currentframe()).filename))


def makeFilePaths(sourceCodeFileName):
    global cwd, spidersDirectoryPath, spidersParentDirectoryPath, dataPath, chromedriverFilePath, trackPath, memoriesPath
    eventlog(sys.path)
    eventlog(os.getcwd())
    cwd = os.getcwd()
    
    eventlog(str("current working directory is: " + cwd))
    spidersDirectoryPath = str(os.path.abspath(os.path.join(os.path.dirname(sourceCodeFileName))))
    eventlog(str("target spidersDirectoryPath is: " + spidersDirectoryPath))
    spidersParentDirectoryPath = str(os.path.abspath(os.path.join(os.path.dirname(sourceCodeFileName),"..")))
    eventlog(str("target spidersParentDirectoryPath is: " + spidersParentDirectoryPath))
    dataPath = str(str(os.path.abspath(os.path.join(os.path.dirname(sourceCodeFileName),"..",".."))) + "/data/")
    set_time = datetime.datetime.now()
    time = set_time.strftime("%y_%m_%d")
    memoriesPath = str(str(dataPath + time + "/"))
    eventlog(str("target memoriesPath is: " + memoriesPath))
    if not os.path.exists(memoriesPath):
        eventlog(str("target memoriesPath does not exist, creating path: " + memoriesPath))
        os.makedirs(memoriesPath)
        eventlog(str("target memoriesPath has been created! \n Find it here: " + memoriesPath))

    trackPath = str(str(dataPath + "track/"))
    eventlog(str("target trackPath is: " + trackPath))
    if not os.path.exists(trackPath):
        eventlog(str("target trackPath does not exist, creating path: " + trackPath))
        os.makedirs(trackPath)
        eventlog(str("target trackPath has been created! \n Find it here: " + trackPath))
    #dataPath = str(spidersParentDirectoryPath )
    eventlog(str("target dataPath is: " + dataPath))
    if not os.path.exists(dataPath):
        eventlog(str("target dataPath does not exist, creating path: " + dataPath))
        os.makedirs(dataPath)
        eventlog(str("target dataPath has been created! \n Find it here: " + dataPath))
    chromedriverFilePath = str( cwd + "/chromedriver")
    eventlog(str("target chromedriverFilePath is: " + chromedriverFilePath))
    return str(cwd), str(spidersDirectoryPath), str(spidersParentDirectoryPath), str(dataPath), str(chromedriverFilePath)

cwd=spidersDirectoryPath=spidersParentDirectoryPath=dataPath=chromedriverFilePath = makeFilePaths(sourceCodeFileName)
#session = Session(webdriver_path=str(Path.home()) + '/p3env/alice/alice/spiders/chromedriver', browser='chrome', default_timeout=3, webdriver_options={'arguments': ['headless']})
path = 0
linkhistory = []
root =  str(os.getcwd() + '/DATABASE')
linkhistory = []
linkstack = []
urlSuccess = False


class GraceClarke :
    def __init__(self, name):
        name = name
        #self.networker = grace_worker()
        #self.ispider = Charlotte()
        self.ifileio = FileIO()
        self.b_dp = None
        self.b_fp = None
        self.l_dp = []
        self.l_fps = []
        self.terminal = self.createTerminal()

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/createTerminal.history', prefix='createTerminal', depth=1)
    def createTerminal(self):
        return GraceClarke.Terminal(self)

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/process_web.history', prefix='process_web', depth=1)
    def process_web(self):
        history = self.ifileio.get_list_of_filepaths_containing_string('.history', os.getcwd() )

        Gracehistory = self.ifileio.get_list_of_filepaths_containing_string('.history', os.getcwd())
        self.terminal.displayTwoLists(history, Gracehistory)
        self.b_dp, self.b_fp, self.l_dp, self.l_fps = self.ifileio.get_list_files_folders_in_path( str(Path.home()) + '/p3env/alice/alice/spiders/')
        eventlog("status b_dp " + str(self.b_dp))
        eventlog("status b_fp " + str(self.b_fp))
        self.terminal.displayTwoLists( self.l_dp,  self.l_fps)
        self.map_db_l_dp_fp( self.l_dp, self.l_fps)
        self.l_fps = self.map_db_get_grace_l_fp()

        '''

        file_contents_unique_lines = self.get_get_list_of_unique_lines_from_files(self.l_fps)

        f= open('charlotteMonitor.txt','a+')
        for line in file_contents_unique_lines:
            f.write(str(line))
            eventlog(str(line))
            f.write(str('\n'))
        f.close
        '''
    '''
    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/map_db_l_dp_fp.history', prefix='map_db_l_dp_fp', depth=1)
    def make_report_from_phrase(self, phrase, columns, maxLoops):
        columns = ['Directory_path', 'File_path']
        listOfLists = []


        listOfLists.append(list_dp)
        listOfLists.append(list_fp)
        #filepath = 'GraceClarke'
        #self.ifileio.csv.write_list_of_lists_to_csv_file(listOfLists, columns, str(Path.home()) + '/p3env/alice/alice/spiders/databasePaths.csv' )
        self.ifileio.csv.write_list_of_lists_to_csv_file(listOfLists, columns, 'databasePaths' )
        
        #for 
        #nValue = dict(zip(list_dp, list_fp))
        #ecords  = 
       # self.ifileio.write_dict_file( dictZip, columns, str(Path.home()) + '/p3env/alice/alice/spiders/paired_directorypaths_filepaths.map' )
    '''
    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/map_db_l_dp_fp.history', prefix='map_db_l_dp_fp', depth=1)
    def map_db_l_dp_fp(self, list_dp, list_fp):
        columns = ['Directory_path', 'File_path']
        listOfLists = []
        listOfLists.append(list_dp)
        listOfLists.append(list_fp)
        #filepath = 'GraceClarke'
        #self.ifileio.csv.write_list_of_lists_to_csv_file(listOfLists, columns, str(Path.home()) + '/p3env/alice/alice/spiders/databasePaths.csv' )
        self.ifileio.csv.write_list_of_lists_to_csv_file(listOfLists, columns, 'databasePaths', list_dp )
        
        #for 
        #nValue = dict(zip(list_dp, list_fp))
        #ecords  = 
       # self.ifileio.write_dict_file( dictZip, columns, str(Path.home()) + '/p3env/alice/alice/spiders/paired_directorypaths_filepaths.map' )

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/map_db_get_grace_l_fp.history', prefix='map_db_get_grace_l_fp', depth=1)
    def map_db_get_grace_l_fp(self):
        l_fps = self.ifileio.get_list_of_filepaths_containing_string( 'grace', str(Path.home()) + '/p3env/alice/alice/spiders')
        return l_fps

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/get_get_list_of_unique_lines_from_files.history', prefix='get_get_list_of_unique_lines_from_files', depth=1)
    def get_get_list_of_unique_lines_from_files(self, l_fps):
        unique_content_lines = self.ifileio.get_l_fp_contents_unique_lines( l_fps)
        return unique_content_lines

    class Terminal:
        #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/__init__.history', prefix='__init__', depth=1)
        def __init__(self, terminalParent):
            self.name = 'initConsole'
            self.terminalParent = terminalParent
            self.run_test()

        #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/debuginfo.history', prefix='debuginfo', depth=1)
        def debuginfo(self, message):
            caller = getframeinfo(stack()[1][0])
            frame = inspect.currentframe()
            self.debugMessageList = []
            if message is not list:
                self.debugMessageList.append(message)
            else:
                self.debugMessageList = message
            self.f = open("nodes.txt", "a+")
            if message is list:
                for i in range(0, len(self.debugMessageList)):
                    eventlog(str("\n Terminal|debuginfo|" + str(caller.lineno) + "|START|\n " + str(self.debugMessageList[i]) + " " + str(caller.lineno) + "|" + "\n|END|\n\n"))
                    #self.f.write(str("\n Terminal|debuginfo|" + str(caller.lineno) + "|START|\n " + str(self.debugMessageList[i]) + "  " + str(caller.lineno) +" \n|END|\n\n"))
            else:
                eventlog(str("\n Terminal|debuginfo|" + str(caller.lineno) + "|START|\n " + str(self.debugMessageList[0])  + "  " + str(caller.lineno) +" \n|END|\n\n"))
                #self.f.write(str("\n Terminal|debuginfo|" + str(caller.lineno) + "|START|\n " + str(self.debugMessageList[0])  + "  " + str(caller.lineno) +" \n|END|\n\n"))

            self.f.close()

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
            string = str(self.tLeft(left) + " " + self.tCenter(center) + " " + self.tLeft(right))
            #self.debuginfo(string)
            return string

        #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/displayTwoLists.history', prefix='displayTwoLists', depth=1)
        def displayTwoLists(self, center, right):
            eventlog('center Length is: ' + str(len(center)))
            eventlog('right Length is: ' + str(len(right)))
            sleep(3)
            self.length = 0
            if len(center) != len(right):
                eventlog('\n\nWARNING LINE LENGTHS DO NOT MATCH!\n\nWARNING LINE LENGTHS DO NOT MATCH!\n\nWARNING LINE LENGTHS DO NOT MATCH!\n\nWARNING LINE LENGTHS DO NOT MATCH!\n\nWARNING LINE LENGTHS DO NOT MATCH!')
                sleep(3)
                if len(center) > len(right):
                    self.length = len(right)
                    for i in range(self.length, len(center)):
                        right.append('- ---- -')
                    self.length = len(center)
                else:
                    self.length = len(center)
                    for i in range(self.length, len(right)):
                        center.append('- ---- -')
                    self.length = len(right)
            else:
                eventlog('\n\n SUCCESS THE LENGTHS MATCH  \n\n')

            for i in range(0, self.length):
                string = str(self.tLeft(str(i)) + " " + self.tCenter(center[i]) + " " + self.tRight(right[i]))
                eventlog(string)

        #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/run_test.history', prefix='run_test', depth=1)
        def run_test(self):
            result = self.displayThree( "Left", "Center", "Right")
            result = self.displayThree("1", "2", "3")
            #sleep(3)

        #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/render_parent_globals.history', prefix='render_parent_globals', depth=1)
        def render_parent_globals(self):
            for i in range(0, self.terminalParent.global_index):
                self.displayThree(self.terminalParent.global_index[i],self.terminalParent.global_list_keys[i], self.terminalParent.global_list_values[i])

        #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/get_parent.history', prefix='get_parent', depth=1)
        def get_parent(self):
            return self.name, str(' is a child of  ') , self.terminalParent.name
    #classes end



class JobResults:
    def init(self):
        self.name = None
        self.alice = None
        self.website_urls = []
        self.emails = []
        self.messages = []

    def append_url(self, url):
        self.alice.printer.append(str(url))
        try:
            self.website_urls.append(str(url))
        except:
            eventlog('we got an issue with: self.website_urls.append(str(url))')

    def append_email(self, email):
        self.alice.printer.append(str(email))
        try:
            self.emails.append(str(email))
        except:
            eventlog('we got an issue with: self.emails.append(str(email))')

    def append_message(self, message):
        self.alice.printer.append(str(message))
        try:
            self.messages.append(str(message))
        except:
            eventlog('we got an issue with: self.messages.append(str(message))')


class Charlotte(scrapy.Spider):
    #session = Session(webdriver_path=str(Path.home()) + '/p3env/alice/alice/spiders/chromedriver', browser='chrome', default_timeout=3, webdriver_options={'arguments': ['headless']})

    def __init__(self, alice):

        self.alice = alice
        self.alice.charlotte = self
        print('Charlotte has met Alice. ')
        print('self.alice.name =  ', self.alice.name)
        self.alice.send_message('Charlotte has connected to Alice.', 'print')

        self.state = 'search'
        self.charlotte = self
        self.webtools = WebTools(self.charlotte)
        self.job_names = []
        self.alive = True
        self.current_job_name = None
        self.implicit_keys = ['PERSON', 'FAC', 'LOC', 'GPE', 'ORG', 'NORP', 'CARDINAL']
        self.explicit_keys = ['medical', 'fqhc', 'health', 'ceo', 'critical access', 'cfo', 'financial', 'director', 'chief' ]
        self.maxLoops = 100000000
        self.tools = Tools()
        self.iFileIO = FileIO()
        self.search_key = ''
        self.name = 'Charlotte'
        self.job_results = None

    def write_job_keys(self, keys):
        eventlog('Charlotte is writing job keys: ' + str(keys))
        self.alice.send_message(str('Charlotte is writing job keys: ' + str(keys)), 'print')
        jobs_filepath = str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/job_list.csv')
        iwrite = open(jobs_filepath, 'w')
        iwrite.write(str(keys))
        iwrite.write('\n')
        iwrite.close()
        self.clear_spider_log()

    def stop_search(self):
        eventlog('Charlotte has recieved the signal stop search')
        self.alice.send_message('Charlotte has recieved the signal stop search', 'print')

    def spider_log(self, message):
        eventlog('Charlotte spider_log: ' + str(message))
        if self.current_job_name != None:
            filepath = str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(self.current_job_name) + '/spider_log.log')
        else:
            filepath = str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/spider_log.log')
        iwrite = open(filepath, 'a+')
        iwrite.write(str(message))
        iwrite.write('\n')
        iwrite.close()
        # self.alice.send_message(str(message), 'print')

    def clear_spider_log(self):
        if self.current_job_name != None:
            filepath = str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(self.current_job_name) + '/spider_log.log')
        else:
            filepath = str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/spider_log.log')
        iwrite = open(filepath, 'w+')
        iwrite.write('')
        iwrite.close()
        # self.alice.send_message(str(message), 'print')

    loop_value = 1
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%Y-%m-%d-%H:%M", named_tuple)
    while loop_value == 1:
        #eventlog('|  network test | ' + str(loop_value))
        try:
            urllib.request.urlopen("http://www.google.com")
            loop_value = 0
            eventlog('|    ONLINE     | ' + str(time_string))
        except urllib.error.URLError as e:

            eventlog('|    OFFLINE    | ' + str(time_string))
            eventlog(e.reason)
            #eventlog('|network offline| ' )
        sleep(3)

    name = 'charlotte'
    start_urls = ["https://duckduckgo.com/"]
    custom_settings = {
    #'SOME_SETTING': 'some value',
        }
    ignoredList = []
    ignoredEmails = []

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/online_navigate_critical_access_hospitals.history', prefix='online_navigate_critical_access_hospitals', depth=1)
    def online_navigate_critical_access_hospitals(self, _Alice, maxLoops):
        m_critical_access_hospitals = _Alice.get_memory("m_critical_access_hospitals", maxLoops)
        self.list_critical_access_hospital_names = m_critical_access_hospitals.get_list_field("Name")

        self.dp_db_web = ''
        self.fixedName = ''
        for name in self.list_critical_access_hospital_names:
            human_time, system_time = Chronos.getProperTime(self)
            self.m_web_cache = self._Alice.get_memory(name, maxLoops)
            self.m_web_cache.dev_record("Date", human_time, True)
            b_success, self.dp_db_web, self.fixedName = self.map_url_by_phrase(str(Path.home()) + "/p3env/alice/alice/spiders/criticalAccessHospitalMiner/", _Alice, name, maxLoops)
            self.m_web_cache.dev_record("map_url_by_phrase_success", b_success, True)
            self.m_web_cache.dev_record("dp_db_web", self.dp_db_web, True)

    def lineno(self):
        """Returns the current line number in our program."""
        return str('line: ' + str(inspect.currentframe().f_back.f_lineno))

    def clear_screen(self):
        
        pass
        # # Clear command as function of OS
        # command = "cls" if platform.system().lower()=="windows" else "clear"

        # # Action
        # return subprocess.call(command) == 0
        
    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/quit_session_get_new_google_search.history', prefix='quit_session_get_new_google_search', depth=1)
    def quit_session_get_new_google_search(self, oldSession, searchKey):
        oldSession.driver.quit()
        sleep(1.5)
        self.session = None
        self.search_form = None
        try:
            self.session = Session(webdriver_path=str(Path.home()) + '/p3env/alice/alice/spiders/chromedriver', browser='chrome', default_timeout=3)
            self.session.driver.set_window_size(1000, 2000)
            sleep(1.5)
            eventlog(str("\n\n driver.page_source\n\n " + str('{:.500}'.format(str(self.session.driver.page_source))) + "\n\n driver.page_source\n\n "))
            self.session.driver.get("https://www.google.com/")
            sleep(1.5)
            self.search_form = self.session.driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[1]/div/div[1]/input")
            sleep(1.5)
            self.search_form.send_keys(searchKey)
            sleep(1.5)
            self.search_form.submit()
            sleep(1.5)
            self.b_success = True
            return self.b_success, self.session
        except:
            self.b_success = False
            self.session.driver.quit()
            return self.b_success, self.session

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/selenium_download_page_source.history', prefix='selenium_download_page_source', depth=1)
    def selenium_download_page_source(self, session, url, dp_db_web):
        session.driver.get(url)
        sleep(1.5)
        self.directory_key = None
        self.fp_url = "".join([c for c in url if c.isalpha() or c.isdigit() or c==' ']).rstrip()
        string = self.fp_url.replace(" ", "")
        fixedName = ''
        if len(string) > 60:
            self.directory_key = str('{:.60}'.format(str(string)))
        else:
            self.directory_key = string
        self.htmlsourcepath = str(dp_db_web + self.directory_key  + '/' + self.directory_key + "index.html")
        if not os.path.exists(str(dp_db_web + self.directory_key  )):
            os.makedirs( str(dp_db_web + self.directory_key  ))
        self.raw = session.driver.page_source
        f = open(self.htmlsourcepath, 'w+')
        f.write(self.raw)
        f.close()
        return self.b_success, self.raw, self.htmlsourcepath, self.directory_key

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/writeFileAs.history', prefix='writeFileAs', depth=1)
    def writeFileAs(self, filepath, suffix, contents, operand):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        suffixlessFilepath = FileIO.getFilePathWithoutsuffix(self, filepath)
        newFilepath = str( suffixlessFilepath + "." + suffix)
        os.makedirs(os.path.dirname(newFilepath), exist_ok=True)
        f = open(newFilepath, operand)
        #f = open(newFilepath, operand)
        f.write(contents)
        f.close()
        return filepath

    '''
    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/map_url_by_phrase.history', prefix='map_url_by_phrase', depth=1)
    def map_url_by_phrase(self, filepathRoot, _Alice, phrase, maxLoops):
        self.fp_google_search = ''
        self.time_system = ''
        self.time_human = ''
        self.list_accesshistory = []
        self.alice_nlp= spacy.load('en_core_web_sm')
        self.a_matcher = Matcher(self.alice_nlp.vocab)
        self.b_success = None
        self.dp_root = filepathRoot
        self.session = Session(webdriver_path=str(Path.home()) + '/p3env/alice/alice/spiders/chromedriver', browser='chrome', default_timeout=3)
        self.session.driver.set_window_size(1000, 2000)
        path0 = "".join([c for c in phrase if c.isalpha() or c.isdigit() or c==' ']).rstrip()
        path1 = path0.replace(" ", "")
        self.fixedName = ''
        if len(path1) > 60:
            self.fixedName = str('{:.60}'.format(str(path1)))
        else:
            self.fixedName = path1

        #self.debuginfo(path1)
        self.fp_google_search = str( self.dp_root + "database/google/" + self.fixedName  + '/' + self.fixedName + "google.html")
        if not os.path.exists( str( self.dp_root + "database/google/" + self.fixedName)):
            os.makedirs( str(self.dp_root + "database/google/" + self.fixedName))
        self.fp_db_web =  str(self.dp_root + "database/google/" + self.fixedName)
        self.raw = self.session.driver.page_source
        eventlog(str("\n\n driver.page_source\n\n " + str('{:.500}'.format(str(self.session.driver.page_source))) + "\n\n driver.page_source\n\n "))
        f = open(self.fp_google_search, 'w+')
        f.write(self.raw)
        f.close()
        self.loops = 0
        self.working = True
        while self.working == True:
            for i in range(1, 3):
                self.loops += 1
                if self.loops > maxLoops:
                    self.working = False
                    break
                try:
                    morePagesXpath = str("//*[@id='rld-" + str(i) + "']/a")
                    self.session.driver.find_element_by_xpath(morePagesXpath).click()
                except:
                    break
            self.raw = self.session.driver.page_source
            f = open(self.fp_google_search, 'a+')
            f.write(self.raw)
            f.close()
            self.working = False
        f = open(self.fp_google_search, 'r')
        self.raw = f.read()
        f.close()
        self.max_tries = 4
        self.try_count = 0
        self.b_success = False
        self.skip_this_search_phrase = False
        while self.b_success == False and self.skip_this_search_phrase == False:
            self.b_success, self.session = self.quit_session_get_new_google_search(self.session, phrase)
            self.try_count += 1
            if self.try_count > self.max_tries:
                self.skip_this_search_phrase = True
        if self.skip_this_search_phrase == False:
            self.b_success = self.webtools.click_first_google_result(self, self.session)
            if self.b_success == False:
                self.flag_failed_error(_Alice, self.fp_db_web, phrase, self.session, maxLoops)
                self.skip_this_search_phrase = True
        if self.skip_this_search_phrase == False:
            self.url_landingPage = self.session.driver.current_url
            self.b_new_db = False
            self.b_new_db, self.htmlsourcepath, self.dp_db_web, self.navigation_targets, self.fp_db_archive, self.fp_db_realtime, self.fp_db_queue, self.fp_db_dev_report, self.fp_db_user_report, self.nlp_targets = FileIO.bot_db_initialize_filepaths(self, self.url_landingPage, self.dp_root)
            self.b_success, self.raw, self.htmlsourcepath, self.directory_key = self.selenium_download_page_source(self.session, self.session.driver.current_url, self.dp_db_web)
            self.b_filepath_exists, self.b_new, self.dp, fp, self.fp_access_history = FileIO.getPathsAndTime(self, self.dp_root)
            self.URL = ''
            self.URL = str(self.session.driver.current_url)
            self.map_url_by_phrase_cache = self.get_url_memory(_Alice, str(self.session.driver.current_url), maxLoops)
            self.map_url_by_phrase_cache.dev_record( "URL", self.URL, True)
            self.time_human, self.systemTime = Chronos.getProperTime(self)
            self.map_url_by_phrase_cache.dev_record( "Date", self.time_human, True)
            self.fp_db_map_index, self.dp_db_page = FileIO.io_get_filepath_as(self, self.htmlsourcepath, 'csv')
            self.map_url_by_phrase_cache.dev_record( "fp_db_map_index", self.fp_db_map_index, True)
            self.map_url_by_phrase_cache.dev_record( "dp_db_page", self.dp_db_page, True)
            self.list_uniqueLinks = []
            self.fp_uniqueLinks = ''
            self.xpaths = []
            self.xpathsFP = ''
            self.raw = self.session.driver.page_source
            eventlog(str("\n\n driver.page_source\n\n " + str('{:.500}'.format(str(self.session.driver.page_source))) + "\n\n driver.page_source\n\n "))
            try:
                self.list_uniqueLinks, self.fp_uniqueLinks, self.xpaths, self.xpathsFP = self.writeHrefCsv(self.htmlsourcepath)
                self.mapUniqueLinks(_Alice, self.session, self.URL, self.dp_db_page, self.uniqueLinks, maxLoops)
                self.session.driver.quit()
                sleep(1.5)
                b_success = True
                return b_success, self.fp_db_web, self.fixedName
            except:
                eventlog(str("\n\n driver.page_source\n\n " + str('{:.500}'.format(str(self.session.driver.page_source))) + "\n\n driver.page_source\n\n "))
                self.flag_failed_error(_Alice, self.fp_db_web, phrase, self.session, maxLoops)
                b_success = False
                self.session.driver.quit()
                return b_success, self.fp_db_web, self.fixedName
    '''

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/navigate_web_search_key.history', prefix='navigate_web_search_key', depth=1)
    def navigate_web_search_key(self, dp_root, _Alice, phrase, maxLoops, job_name, search_results_max_depth, iFileIO):
        self.fp_google_search = ''
        self.time_system = ''
        self.time_human = ''
        self.list_accesshistory = []
        #self.a_nlp= spacy.load('en_core_web_sm')
        #self.a_matcher = Matcher(self.a_nlp.vocab)
        self.b_success = None
        self.dp_google_results = None
        self.directory_key = None
        self.b_success, self.dp_google_results, self.directory_key, self.newlinks = self.webtools.job_search_results(job_name, phrase, search_results_max_depth, maxLoops, dp_root, iFileIO)
        return self.b_success, self.dp_google_results, self.directory_key, self.newlinks

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/online_search_job.history', prefix='online_search_job', depth=1)
    def online_search_job(self, job_name, search_key, implicit_keys, explicit_keys, maxLoops, search_results_max_depth, iFileIO):
        try:
            dirs = os.listdir( str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/') + str(job_name) + '/web/http/' )
            for item in dirs:
                os.remove(str(item))
        except:
            pass

        try:
            dirs = os.listdir( str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/') + str(job_name) + '/web/https/' )
            for item in dirs:
                os.remove(str(item))
        except:
            pass

        eventlog('def online_search_job')
        #sleep(3)
        #make_job_paths
        #instantiate job instance
        self.dp_db_web = ''
        self.fixedName = ''
        path = DatabaseTools.make_job_paths(self, job_name)
        human_time, system_time = Chronos.getProperTime(self)
        self.memKeys = list(explicit_keys + implicit_keys)
        self.memVals = []
        for i in range(0, len(self.memKeys)):
            self.memVals.append(i)
        self.memIndex = 0
        self._Alice = AliceInWonderland(self.memIndex, self.memKeys,self.memVals, maxLoops, self.charlotte)
        self.job_memory = self._Alice.get_memory(job_name, maxLoops)
        #self.job_search_keys =self.job_memory.get_list_field("search_keys")
        self.b_success, self.dp_google_results, self.directory_key, self.newlinks = self.navigate_web_search_key(path, self._Alice, search_key, maxLoops, job_name, search_results_max_depth, iFileIO)
        self.job_memory.dev_record("Date", human_time, True)
        self.job_memory.dev_record("map_url_by_phrase_success", self.b_success, True)
        self.job_memory.dev_record("dp_db_web", self.dp_db_web, True)
        return self.newlinks


    def remove_duplicate_rows_from_file_A_given_file_B_and_given_fields(self, iFileIO, file_A_path, file_B_path, file_A_list_compare_fields, file_B_list_compare_fields):
        f = open(str(file_A_path + str('-UNIQUE-TAIL')), 'w+')
        f.write(str(''))
        f.close()
        f = open(str(file_A_path + str('-DUPLICATE-TAIL')), 'w+')
        f.write(str(''))
        f.close()
        self.file_A_list_fields = []
        self.file_A_current_field_name = ''
        self.file_A_previous_field_name = ''
        self.file_A_current_value = ''
        self.file_A_current_list_values = []
        self.file_A_current_field_index = 0
        self.file_A_list_field_index_triggers = []
        self.file_B_list_current_values = []

        self.b_set_fields = False
        self.file_A_rows = iFileIO.getListFromFile(file_A_path, 9999999)

        self.file_A_row_index = 0
        self.file_B_row_index = 0
        self.file_B_rows = iFileIO.getListFromFile(file_B_path, 9999999)

        for line in self.file_A_rows:
            #self.clear_screen()
            #eventlog('File_A_current_field_index: ' + str(self.file_A_current_field_index))
            if self.b_set_fields == False:
                self.file_A_list_fields = line.split(',')
                eventlog('length of str(self.file_A_list_fields): ' + str(len(self.file_A_list_fields)))
                sleep(0.1337)

                for i in range (0, len(self.file_A_list_fields)):
                    eventlog('ITEM FIELDS: ' + str(self.file_A_list_fields[i]))
                    #self.file_A_list_fields.append(str(item))
                    sleep(0.1337)
                self.b_set_fields = True
                eventlog('DONE WITH FIELDS')
                eventlog(str(self.file_A_list_fields))
                sleep(0.1337)
                for i in range(0, len(self.file_A_list_fields)):
                    for compare_field in file_A_list_compare_fields:
                        eventlog('self.file_A_list_fields[i]: ' + self.file_A_list_fields[i])
                        eventlog('compare_field: ' + compare_field)
                        if self.file_A_list_fields[i].find(compare_field) != -1:
                            self.file_A_list_field_index_triggers.append(i)
                            eventlog('Triggering on FIELDINDEX: ' + str(i) + ' FIELDNAME: ' + self.file_A_list_fields[i] )
                            sleep(0.1337)
                sleep(0.1337)
            else:
                self.file_A_current_field_index = 0
                self.file_A_current_list_values = []
                self.file_A_current_trigger_values = []
                self.file_A_current_value = ''
                self.file_A_current_list_values = line.split(',')
                eventlog('length of str(self.file_A_current_list_values): ' + str(len(self.file_A_current_list_values)))
                eventlog('values of str(self.file_A_current_list_values): ' + str(self.file_A_current_list_values))
                eventlog('length of str(self.file_A_list_fields): ' + str(len(self.file_A_list_fields)))
                eventlog('fields of str(self.file_A_list_fields): ' + str(self.file_A_list_fields))
                sleep(0.1337)
                for i in range(0, len(self.file_A_current_list_values)):
                    self.file_A_current_field_index = i
                    eventlog('ITEM VALUE: ' + str(self.file_A_current_list_values[i]) + ' Field: ' + str(self.file_A_list_fields[self.file_A_current_field_index]) + ' File_A_current_field_index: ' + str(self.file_A_current_field_index))
                    #eventlog (str(item))
                    self.file_A_current_list_values.append(str(self.file_A_current_list_values[i]))
                    sleep(0.1337)

                    #for ch in self.file_A_current_list_values[i]:
                    self.inside_trigger_fields = False
                    for trigger_index in self.file_A_list_field_index_triggers:
                        if self.file_A_current_field_index == trigger_index:
                            self.inside_trigger_fields = True
                            eventlog('triggers on: ' + str(self.file_A_list_field_index_triggers))
                            eventlog(str('inside trigger field! '))
                            self.file_A_current_value = self.file_A_current_list_values[i]
                            eventlog('file_A_current_value: ' + str(self.file_A_current_value) )
                            '''
                            if self.inside_trigger_fields == True:
                                self.file_A_current_list_values.append(str(self.file_A_current_value))
                                eventlog('file_A_current_value: ' + str(self.file_A_current_value) )
                                self.file_A_current_value = ''
                            elif ch.find(' ') != -1 and self.inside_trigger_fields == True and self.file_A_previous_field_name == self.file_A_current_field_name:
                                self.file_A_current_list_values.append(str(self.file_A_current_value))
                                eventlog('file_A_current_value: ' + str(self.file_A_current_value) )
                                self.file_A_current_value = ''
                            elif self.inside_trigger_fields == True:
                                self.file_A_current_value += ch
                            '''
                            self.file_A_current_trigger_values.append(str(self.file_A_current_value))
                            eventlog('file_A_current_trigger_value: ' + str(self.file_A_current_value) )

                for item in self.file_A_current_trigger_values:
                    eventlog('TRIGGER VALUES FOR ROW: ' + str(self.file_A_row_index) + ' ' + str(item))
                    sleep(0.5)

                self.file_B_row_index = 0
                self.b_searching = True
                self.b_found_duplicate = False
                
                while self.b_searching == True:
                    self.number_of_triggers = 0
                    self.triggered_items = []
                    eventlog('self.file_A_row_index: ' + str(self.file_A_row_index))
                    eventlog('self.file_B_row_index: ' + str(self.file_B_row_index))
                    for i in range(0, len(self.file_A_current_trigger_values)):
                        eventlog('current_value: ' + "'" + str(self.file_A_current_trigger_values[i]) + "'")
                        if self.file_B_rows[self.file_B_row_index].find(self.file_A_current_trigger_values[i]) != -1:
                            self.b_found_duplicate = True
                            self.b_searching = False
                    if self.file_B_row_index < len(self.file_B_rows) - 1:
                        self.file_B_row_index += 1
                    else:
                        self.b_searching = False

                if self.b_found_duplicate == True:
                    f = open(str(file_A_path + str('-DUPLICATE-TAIL')), 'a+')
                    f.write(str(line))
                    f.write('\n')
                    f.close()
                else:
                    f = open(str(file_A_path + str('-UNIQUE-TAIL')), 'a+')
                    f.write(str(line))
                    f.write('\n')
                    f.close()

                self.file_A_row_index += 1

    def validate_emails_given_field(self, iFileIO, file_A_path, file_A_list_compare_fields):
        f = open(str(file_A_path + str('-VALID_EMAIL-TAIL')), 'w+')
        f.write(str(''))
        f.close()
        f = open(str(file_A_path + str('-INVALID_EMAIL-TAIL')), 'w+')
        f.write(str(''))
        f.close()
        f = open(str(file_A_path + str('-full-report')), 'a+')
        ##f.write(str(line) + ',' + )
        #f.write('\n')
        f.write(str(''))
        f.close()
        self.file_A_list_fields = []
        self.file_A_current_field_name = ''
        self.file_A_previous_field_name = ''
        self.file_A_current_value = ''
        self.file_A_current_list_values = []
        self.file_A_current_field_index = 0
        self.file_A_list_field_index_triggers = []


        self.b_set_fields = False
        self.file_A_rows = iFileIO.getListFromFile(file_A_path, 9999999)

        self.file_A_row_index = 0

        for line in self.file_A_rows:
            #self.clear_screen()
            #eventlog('File_A_current_field_index: ' + str(self.file_A_current_field_index))
            if self.b_set_fields == False:
                self.file_A_list_fields = line.split(',')
                eventlog('length of str(self.file_A_list_fields): ' + str(len(self.file_A_list_fields)))
                sleep(0.1337)

                for i in range (0, len(self.file_A_list_fields)):
                    eventlog('ITEM FIELDS: ' + str(self.file_A_list_fields[i]))
                    #self.file_A_list_fields.append(str(item))
                    sleep(0.1337)
                self.b_set_fields = True
                eventlog('DONE WITH FIELDS')
                eventlog(str(self.file_A_list_fields))
                sleep(0.1337)
                for i in range(0, len(self.file_A_list_fields)):
                    for compare_field in file_A_list_compare_fields:
                        eventlog('self.file_A_list_fields[i]: ' + self.file_A_list_fields[i])
                        eventlog('compare_field: ' + compare_field)
                        if self.file_A_list_fields[i].find(compare_field) != -1:
                            self.file_A_list_field_index_triggers.append(i)
                            eventlog('Triggering on FIELDINDEX: ' + str(i) + ' FIELDNAME: ' + self.file_A_list_fields[i] )
                            sleep(0.1337)
                sleep(0.1337)
            else:
                self.file_A_current_field_index = 0
                self.file_A_current_list_values = []
                self.file_A_current_trigger_values = []
                self.file_A_current_value = ''
                self.file_A_current_list_values = line.split(',')
                eventlog('length of str(self.file_A_current_list_values): ' + str(len(self.file_A_current_list_values)))
                eventlog('values of str(self.file_A_current_list_values): ' + str(self.file_A_current_list_values))
                eventlog('length of str(self.file_A_list_fields): ' + str(len(self.file_A_list_fields)))
                eventlog('fields of str(self.file_A_list_fields): ' + str(self.file_A_list_fields))
                sleep(0.1337)
                for i in range(0, len(self.file_A_current_list_values)):
                    self.file_A_current_field_index = i
                    eventlog('ITEM VALUE: ' + str(self.file_A_current_list_values[i]) + ' Field: ' + str(self.file_A_list_fields[self.file_A_current_field_index]) + ' File_A_current_field_index: ' + str(self.file_A_current_field_index))
                    #eventlog (str(item))
                    self.file_A_current_list_values.append(str(self.file_A_current_list_values[i]))
                    sleep(0.1337)

                    self.inside_trigger_fields = False
                    self.valid_email = False
                    for trigger_index in self.file_A_list_field_index_triggers:
                        if self.file_A_current_field_index == trigger_index:
                            self.inside_trigger_fields = True
                            eventlog('triggers on: ' + str(self.file_A_list_field_index_triggers))
                            eventlog(str('inside trigger field! '))
                            self.file_A_current_value = self.file_A_current_list_values[i]
                            eventlog('file_A_current_value: ' + str(self.file_A_current_value) )


                            is_valid = pyisemail.is_email(str(self.file_A_current_value), check_dns=True)
                            eventlog( str(self.file_A_current_value) + ' is valid: ' + str(is_valid))
                            detailed_result_with_dns = pyisemail.is_email(str(self.file_A_current_value), check_dns=True, diagnose=True)
                            eventlog( str(self.file_A_current_value) + ' is detailed_result_with_dns: ' + str(detailed_result_with_dns ))
                            sleep(1)

                            if is_valid == True:
                                #if validate_email(email_address=str(self.file_A_current_value), check_regex=True, check_mx=True, from_address='info@ahapinc.com', helo_host='mx1.emailsrvr.com', smtp_timeout=5, dns_timeout=5, use_blacklist=False):
                                f = open(str(file_A_path + str('-VALID_EMAIL-TAIL')), 'a+')
                                f.write(str(line))
                                f.write('\n')
                                f.close()
                            else:
                                f = open(str(file_A_path + str('-INVALID_EMAIL-TAIL')), 'a+')
                                f.write(str(line))
                                f.write('\n')
                                f.close()

                            f = open(str(file_A_path + str('-full-report')), 'a+')
                            f.write(str(line) + ',' + str(detailed_result_with_dns) + ',' + str(is_valid))
                            f.write('\n')
                            f.close()
                self.file_A_row_index += 1

    def get_list_values_given_field(self, iFileIO, file_A_path, file_A_list_compare_fields):

        f = open(str(file_A_path + str('-full-report')), 'w+')
        ##f.write(str(line) + ',' + )
        #f.write('\n')
        f.write(str('2nd Contact,2nd Last Reach,2nd Phone,2nd Phone Ext-,2nd Title,3rd Contact,3rd Last Reach,3rd Phone,3rd Phone Ext-,3rd Title,Address 1,Address 2,Address 3,AEM Bounce Back,AEM Opt Out,Alt Phone,Alt Phone Ext-,Assistant,Asst- Phone,Asst- Phone Ext-,Asst- Title,Birth Date,City,Company,Contact,Country,Create Date,Department,Edit Date,E-mail,E-Mail 2,E-Mail 3 E-mail,E-Mail 4 E-mail,Favorite,Fax,Fax Ext-,First Name,Home Address 1,Home Address 2,Home Address 3,Home City,Home Country,Home Extension,Home Phone,Home State,Home Zip,ID/Status,Last Attempt,Last Edited By,Last E-mail,Last Meeting,Last Name,Last Reach,Last Results,Latitude,Letter Date,Longitude,Messenger ID,Middle Name,Mobile Extension,Mobile Phone,Name Prefix,Name Suffix,Owner,Pager,Pager Extension,Personal E-mail,Phone,Phone Ext-,Private Contact,Record Creator,Record Manager,Referred By,Salutation,Spouse,State,Ticker Symbol,Title,User 1,User 10,User 11,User 12,User 13,User 14,User 15,User 2,User 3,User 4,User 5,User 6,User 7,User 8,User 9,Web Site,Zip'))
        f.write('\n')
        f.close()
        file_A_list_fields = []
        file_A_current_field_name = ''
        #file_A_previous_field_name = ''
        file_A_current_value = ''
        file_A_current_list_values = []
        file_A_current_field_index = 0
        file_A_list_field_index_triggers = []



        b_set_fields = False
        file_A_rows = iFileIO.getListFromFile(file_A_path, 9999999)

        file_A_row_index = 0
        list_values = []
        for line in file_A_rows:
            #clear_screen()
            #eventlog('File_A_current_field_index: ' + str(file_A_current_field_index))
            if b_set_fields == False:
                file_A_list_fields = line.split(',')
                eventlog('length of str(file_A_list_fields): ' + str(len(file_A_list_fields)))
                #sleep(0.1337)

                for i in range (0, len(file_A_list_fields)):
                    eventlog('ITEM FIELDS: ' + str(file_A_list_fields[i]))
                    #file_A_list_fields.append(str(item))
                    #sleep(0.1337)
                b_set_fields = True
                eventlog('DONE WITH FIELDS')
                eventlog(str(file_A_list_fields))
                #sleep(0.1337)
                for i in range(0, len(file_A_list_fields)):
                    for compare_field in file_A_list_compare_fields:
                        eventlog('file_A_list_fields[i]: ' + file_A_list_fields[i])
                        eventlog('compare_field: ' + compare_field)
                        if file_A_list_fields[i].find(compare_field) != -1:
                            file_A_list_field_index_triggers.append(i)
                            eventlog('Triggering on FIELDINDEX: ' + str(i) + ' FIELDNAME: ' + file_A_list_fields[i] )
                            #sleep(0.1337)
                #sleep(0.1337)
            else:
                file_A_current_field_index = 0
                file_A_current_list_values = []
                file_A_current_trigger_values = []
                file_A_current_value = ''
                file_A_current_list_values = line.split(',')
                eventlog('length of str(file_A_current_list_values): ' + str(len(file_A_current_list_values)))
                eventlog('values of str(file_A_current_list_values): ' + str(file_A_current_list_values))
                eventlog('length of str(file_A_list_fields): ' + str(len(file_A_list_fields)))
                eventlog('fields of str(file_A_list_fields): ' + str(file_A_list_fields))
                #sleep(0.1337)
                #modified_line_value_list = []
                #modValue = ''
                for i in range(0, len(file_A_current_list_values)):
                    file_A_current_field_index = i
                    eventlog('ITEM VALUE: ' + str(file_A_current_list_values[i]) + ' Field: ' + str(file_A_list_fields[file_A_current_field_index]) + ' File_A_current_field_index: ' + str(file_A_current_field_index))
                    #eventlog (str(item))
                    file_A_current_list_values.append(str(file_A_current_list_values[i]))
                    #sleep(0.1337)

                    inside_trigger_fields = False

                    for trigger_index in file_A_list_field_index_triggers:
                        if file_A_current_field_index == trigger_index:
                            inside_trigger_fields = True
                            eventlog('triggers on: ' + str(file_A_list_field_index_triggers))
                            eventlog(str('inside trigger field! '))
                            file_A_current_value = file_A_current_list_values[i]
                            eventlog('file_A_current_value: ' + str(file_A_current_value) )
                            #modValue = '+++TARGET+++'
                            #modified_line_value_list.append(str(modValue))
                            list_values.append(str(file_A_current_value))


                file_A_row_index += 1
        for item in list_values:
            eventlog('item: ' + str(item))
        
        #exit()
        return list_values

    def update_bounce_status_given_field(self, iFileIO, file_A_path, file_A_list_compare_fields, bounce_file, bounce_field_email, bounce_field_status):
        f = open(str(file_A_path + str('-full-report')), 'w+')
        ##f.write(str(line) + ',' + )
        #f.write('\n')
        f.write(str('2nd Contact,2nd Last Reach,2nd Phone,2nd Phone Ext-,2nd Title,3rd Contact,3rd Last Reach,3rd Phone,3rd Phone Ext-,3rd Title,Address 1,Address 2,Address 3,AEM Bounce Back,AEM Opt Out,Alt Phone,Alt Phone Ext-,Assistant,Asst- Phone,Asst- Phone Ext-,Asst- Title,Birth Date,City,Company,Contact,Country,Create Date,Department,Edit Date,E-mail,E-Mail 2,E-Mail 3 E-mail,E-Mail 4 E-mail,Favorite,Fax,Fax Ext-,First Name,Home Address 1,Home Address 2,Home Address 3,Home City,Home Country,Home Extension,Home Phone,Home State,Home Zip,ID/Status,Last Attempt,Last Edited By,Last E-mail,Last Meeting,Last Name,Last Reach,Last Results,Latitude,Letter Date,Longitude,Messenger ID,Middle Name,Mobile Extension,Mobile Phone,Name Prefix,Name Suffix,Owner,Pager,Pager Extension,Personal E-mail,Phone,Phone Ext-,Private Contact,Record Creator,Record Manager,Referred By,Salutation,Spouse,State,Ticker Symbol,Title,User 1,User 10,User 11,User 12,User 13,User 14,User 15,User 2,User 3,User 4,User 5,User 6,User 7,User 8,User 9,Web Site,Zip'))
        f.write('\n')
        f.close()
        self.file_A_list_fields = []
        self.file_A_current_field_name = ''
        #self.file_A_previous_field_name = ''
        self.file_A_current_value = ''
        self.file_A_current_list_values = []
        self.file_A_current_field_index = 0
        self.file_A_list_field_index_triggers = []
        self.list_bounce_emails = self.get_list_values_given_field(iFileIO, bounce_file, bounce_field_email)
        self.list_bounce_status = self.get_list_values_given_field(iFileIO, bounce_file, bounce_field_status)

        for i in range(0, len(self.list_bounce_emails)):
            eventlog( str(i) + ' DEBOUNCE DATA - EMAIL: ' + str(self.list_bounce_emails[i]) + ' STATUS: ' +  str(self.list_bounce_status[i]))

        self.b_set_fields = False
        self.file_A_rows = iFileIO.getListFromFile(file_A_path, 9999999)

        self.file_A_row_index = 0

        for line in self.file_A_rows:
            #self.clear_screen()
            #eventlog('File_A_current_field_index: ' + str(self.file_A_current_field_index))
            if self.b_set_fields == False:
                self.file_A_list_fields = line.split(',')
                eventlog('length of str(self.file_A_list_fields): ' + str(len(self.file_A_list_fields)))
                #sleep(0.1337)

                for i in range (0, len(self.file_A_list_fields)):
                    eventlog('ITEM FIELDS: ' + str(self.file_A_list_fields[i]))
                    #self.file_A_list_fields.append(str(item))
                    #sleep(0.1337)
                self.b_set_fields = True
                eventlog('DONE WITH FIELDS')
                eventlog(str(self.file_A_list_fields))
                #sleep(0.1337)
                for i in range(0, len(self.file_A_list_fields)):
                    for compare_field in file_A_list_compare_fields:
                        eventlog('self.file_A_list_fields[i]: ' + self.file_A_list_fields[i])
                        eventlog('compare_field: ' + compare_field)
                        if self.file_A_list_fields[i].find(compare_field) != -1:
                            self.file_A_list_field_index_triggers.append(i)
                            eventlog('Triggering on FIELDINDEX: ' + str(i) + ' FIELDNAME: ' + self.file_A_list_fields[i] )
                            #sleep(0.1337)
                #sleep(0.1337)
            else:
                self.file_A_current_field_index = 0
                self.file_A_current_list_values = []
                self.file_A_current_trigger_values = []
                self.file_A_current_value = ''
                self.file_A_current_list_values = line.split(',')
                eventlog('length of str(self.file_A_current_list_values): ' + str(len(self.file_A_current_list_values)))
                eventlog('values of str(self.file_A_current_list_values): ' + str(self.file_A_current_list_values))
                eventlog('length of str(self.file_A_list_fields): ' + str(len(self.file_A_list_fields)))
                eventlog('fields of str(self.file_A_list_fields): ' + str(self.file_A_list_fields))
                #sleep(0.1337)
                modified_line_value_list = []
                modValue = ''
                for i in range(0, len(self.file_A_current_list_values)):
                    self.file_A_current_field_index = i
                    eventlog('ITEM VALUE: ' + str(self.file_A_current_list_values[i]) + ' Field: ' + str(self.file_A_list_fields[self.file_A_current_field_index]) + ' File_A_current_field_index: ' + str(self.file_A_current_field_index))
                    #eventlog (str(item))
                    self.file_A_current_list_values.append(str(self.file_A_current_list_values[i]))
                    #sleep(0.1337)

                    self.inside_trigger_fields = False
                    self.valid_email = False
                    self.triggered = False
                    for trigger_index in self.file_A_list_field_index_triggers:
                        if self.file_A_current_field_index == trigger_index:
                            self.inside_trigger_fields = True
                            eventlog('triggers on: ' + str(self.file_A_list_field_index_triggers))
                            eventlog(str('inside trigger field! '))
                            self.file_A_current_value = self.file_A_current_list_values[i]
                            eventlog('file_A_current_value: ' + str(self.file_A_current_value) )
                            #modValue = '+++TARGET+++'
                            #modified_line_value_list.append(str(modValue))
                            searching = True
                            while searching == True:
                                for i in range(0, len(self.list_bounce_emails)):
                                    eventlog( str(i) + ' DEBOUNCE DATA - EMAIL: ' + str(self.list_bounce_emails[i]) + ' STATUS: ' +  str(self.list_bounce_status[i]))
                                    if line.find(str(self.list_bounce_emails[i])) != -1:
                                        self.triggered = True
                                        modified_line_value_list.append(str(self.list_bounce_status[i]))
                                        searching = False
                                searching = False
                            if self.triggered == False:
                                modified_line_value_list.append(str(self.file_A_current_value))
                                self.triggered = True
                        #else:
                            #modified_line_value_list.append(str(self.file_A_current_list_values[i]))
                    if self.triggered == False:
                        modified_line_value_list.append(str(self.file_A_current_list_values[i]))

                modified_line = ''
                for i in range(0, len(modified_line_value_list)):
                    modified_line += str(modified_line_value_list[i])
                    if i < int(len(modified_line_value_list) - 1):
                        modified_line += ','

                f = open(str(file_A_path + str('-full-report')), 'a+')
                f.write(str(modified_line))
                f.write('\n')
                f.close()
                self.file_A_row_index += 1

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/online_threaded_navigation_job.history', prefix='online_threaded_navigation_job', depth=1)
    def online_threaded_navigation_job(self, _Alice, job_name, search_key, implicit_keys, explicit_keys, maxLoops, search_results_max_depth, iFileIO, newlinks):
        #self.clear_screen()
        #f = open(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/online_threaded_navigation_job.history', 'w+')
        #f.write('')
        #f.close()
        eventlog('def online_threaded_navigation_job')
        self.nav_depth = 5
        self.b_success = None
        self.dp_google_results = ''
        self.directory_key = ''
        self.href_target_list = []
        self.b_ignore_known = False
        self.fixedName = ''
        self.human_time, self.system_time = Chronos.getProperTime(self)
        self.list_href_nav, self.list_lang_nav, self.list_key_nav = _Alice.get_nav_queue()
        self.list_temp_href_nav = []
        for item in self.list_href_nav:
            self.cleanItem = ''
            for ch in item:
                if ch != ' ' and ch != ',':
                    self.cleanItem += ch
            cleanItem = self.cleanItem
            eventlog('self.cleanItem: ' + str(cleanItem))
            self.list_temp_href_nav.append(self.cleanItem)
        self.list_href_nav = self.list_temp_href_nav
        self.string_key_nav = ' '
        for item in self.list_key_nav:
            self.string_key_nav += str(str(item) + ' ')
        self.webtools.job_navigate_results(_Alice, job_name, newlinks, iFileIO)

    def autoclear_pysnooper(self, iFileIO):
        l_history = iFileIO.get_list_of_filepaths_containing_string(iFileIO, '.history', str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history')
        for history in l_history:
            os.remove(str(history))

    def shuffle_and_verify_email_file(self, job_name, filepath):
        def get_list_from_file():
            listFromFile = []
            listFromFile.clear()
            working = True
            fh = open(str(filepath))
            while working == True:
                for line in fh:
                    listFromFile.append(line.rstrip())
                working = False
            fh.close()
            return listFromFile

        list_harvested_emails = get_list_from_file()

        for i in range(len(list_harvested_emails)):
            swap = randint(0,len(list_harvested_emails)-1)
            temp = list_harvested_emails[swap]
            list_harvested_emails[swap] = list_harvested_emails[i]
            list_harvested_emails[i] = temp


        iwrite = open(str(str(filepath) + str('shuffled') ), 'w+')
        #iwrite.write(str('email,url,description,timestamp'))
        #iwrite.write(str('\n'))

        for item in list_harvested_emails:
            valid, reason = Tools.verify_email(self, str(item), job_name)
            if valid == True:
                eventlog('included: ' + str(item))
                iwrite.write(str(item))
                iwrite.write(str('\n'))
            else:
                eventlog('excluded: ' + str(item))
        iwrite.close()


    def compile_new_list_of_unique_emails(self, job_name, published_emails_filepath):
        filepath_b = str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/email_heap.csv'
        dedup_files = DatabaseTools.return_deduplicated_list_file_A_given_file_B(self, filepath_b, published_emails_filepath)
        output_path = str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/harvest/contacts/emails/unpublished/unpublished.csv'
        iwrite = open(output_path, 'w+')
        for item in dedup_files:
            valid, reason = Tools.verify_email(self, job_name, str(item))
            if valid == True:
                eventlog('WRITING UNIQUE: ' + str(item))
                iwrite.write(str(item))
                iwrite.write('\n')
        iwrite.close()


    def initialize_job_paths(self, job_name):
        job = str(job_name)
        eventlog('job_name: ' + job)
        


    def log_state(self):
        
        runtime = 0
        while self.alive:
            eventlog('WS.LOOP: ' + str(WS.LOOP))

            try:
                asyncio.set_event_loop_policy(AnyThreadEventLoopPolicy())
            except Exception as e:
                eventlog('EXCEPTION: ' + str(e))
            eventlog('SWITCHBOARD IS: ' + str(SWITCHBOARD))
            text = {
                'message': str('testing dawg testing dawg: ' + str(runtime)),
                'command': 'print',
                'From': self.alice.name,
                'human': self.alice.human
            }
            eventlog('RUNTIME SECONDS: ' + str(runtime) + ' job_name: ' + str(self.current_job_name) + ' STATE: ' + str(self.state))
            try:
                self.alice.switchboard.write_message(json.dumps(text))
            except Exception as e:
                eventlog('EXCEPTION: ' + str(e))

            try:
                IOLoop.add_callback_from_signal(json.dumps(text))
            except Exception as e:
                eventlog('EXCEPTION: ' + str(e))



            sleep(0.5)
            runtime += 0.5


    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='parse', depth=1)
    def parse(self, response):
        log_state_thread = Thread(target = self.log_state)
        log_state_thread.start()
        self.memKeys = list(self.explicit_keys + self.implicit_keys)
        self.memVals = []
        for i in range(0, len(self.memKeys)):
            self.memVals.append(i)
        self.memIndex = 0
        self._Alice = AliceInWonderland(self.memIndex, self.memKeys,self.memVals, self.maxLoops, self.charlotte)
        # while self.alive:
        self.state = 'idle'

        eventlog('PARSING LOOP BEGIN!!!')
        eventlog('PARSING LOOP BEGIN!!!')
        eventlog('PARSING LOOP BEGIN!!!')
        eventlog('PARSING LOOP BEGIN!!!')
        eventlog('PARSING LOOP BEGIN!!!')
        eventlog('PARSING LOOP BEGIN!!!')
        eventlog('PARSING LOOP BEGIN!!!')
        eventlog('PARSING LOOP BEGIN!!!')

        eventlog('os.cwd()' + str(os.getcwd()))
        home = str(Path.home())
        eventlog('home: ' + str(home))
        eventlog('Scrapy started parsing')
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%Y-%m-%d-%H:%M", named_tuple)

        with open(str(Path.home()) + '/p3env/alice/alice/spiders/ALICE.txt', 'a+') as f:
            f.write('ALICE WOKE: ' + str(time_string))
            f.write('\n')
            f.close()
        

        self.autoclear_pysnooper(self.iFileIO)


        eventlog('self.list_old_urls_filepaths')


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

        search_results_max_depth = 100
        # job_name = 'AHAP'
        # job_name = 'dante'

        jobs_filepath = str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/job_list.csv')
        if os.path.exists(jobs_filepath):
            pass
        else:
            iwrite = open(jobs_filepath, 'a+')
            iwrite.write('bernie_sanders')
            iwrite.write('\n')
            iwrite.write('andre_doumad')
            iwrite.write('\n')
            iwrite.write('glenn_lusk')
            iwrite.write('\n')
            iwrite.close()
        self.job_names = get_list_from_file(jobs_filepath)



        job_name = None
        self.current_job_name = job_name
        for name in self.job_names:
            eventlog('for name in self.job_names: ' + str(name))
            if len(name) > 1:
                job_name = name.replace(' ', '_')

        if job_name == None:
            self.command = 'waiting_for_job_name'
        else:
            self.command = 'search'

            self.current_job_name = job_name
        
        self.job_results = JobResults()
        self.job_results.name = self.current_job_name
        self.job_results.alice = self.alice
        # if job_name != None:
        iwrite = open(jobs_filepath, 'w')
        iwrite.write('\n')
        iwrite.close()

        for name in self.job_names:
            if name != job_name and len(name) > 1:
                iwrite = open(jobs_filepath, 'a+')
                iwrite.write(str(name))
                iwrite.write('\n')
                iwrite.close()

        self.initialize_job_paths(job_name)


        self.tools.create_job_search_phrase(job_name)


        job_search_phrases = []

        job_search_phrases = get_list_from_file(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_phrases.csv'))
        for phrase in job_search_phrases:
            eventlog('job_search_phrases: ' + str(phrase))

        def shuffle_list(inputlist):
            for i in range(len(inputlist)):
                swap = randint(0,len(inputlist)-1)
                temp = inputlist[swap]
                inputlist[swap] = inputlist[i]
                inputlist[i] = temp
            return inputlist

        # job_search_phrases = shuffle_list(job_search_phrases)
        # initial_search_phrases = get_list_from_file(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/' + str(job_name) + '/job_phrases.csv'))
        # initial_search_phrases = shuffle_list(initial_search_phrases)

        self.autoclear_pysnooper(self.iFileIO)

        # search_key = str(initial_search_phrases[0])
        # self.newlinks = self.online_search_job(job_name, search_key, implicit_keys, explicit_keys, maxLoops, search_results_max_depth, iFileIO)
        path, b_exists = DatabaseTools.get_job_paths(self, job_name)
        self.b_success = False
        if b_exists == False:
            eventlog('WARNING -- path does not exist -- do job first!')
            exit()
        else:
            self.b_success = True

        def process_job_phrases(job_search_phrases):
            # for search_phrase in job_search_phrases:
            #     eventlog('STARTING ONLINE_THREADED_NAVIGATION_JOB')
            #     self.state = 'search'
            #     self.autoclear_pysnooper(self.iFileIO)
            #     search_key = str(search_phrase)
            #     self.newlinks = self.online_search_job(job_name, search_key, self.implicit_keys, self.explicit_keys, self.maxLoops, search_results_max_depth, self.iFileIO)
            #     self.search_key = search_key

            #     self.job_memory = self._Alice.get_memory(job_name, self.maxLoops)
            #     self.list_google_matrix, self.list_website_matrix = DatabaseTools.explore_matrix(self, path, self._Alice)
            #     self.online_threaded_navigation_job(self._Alice, job_name, search_key, self.implicit_keys, self.explicit_keys, self.maxLoops, search_results_max_depth, self.iFileIO, self.newlinks)
            #     eventlog('COMPLETED ONLINE_THREADED_NAVIGATION_JOB')

            # for search_phrase in job_search_phrases:
            eventlog('STARTING ONLINE_THREADED_NAVIGATION_JOB')
            self.state = 'search'
            self.autoclear_pysnooper(self.iFileIO)
            search_key = str(job_search_phrases[0])
            self.newlinks = self.online_search_job(job_name, search_key, self.implicit_keys, self.explicit_keys, self.maxLoops, search_results_max_depth, self.iFileIO)
            self.search_key = search_key

            self.job_memory = self._Alice.get_memory(job_name, self.maxLoops)
            self.list_google_matrix, self.list_website_matrix = DatabaseTools.explore_matrix(self, path, self._Alice)
            self.online_threaded_navigation_job(self._Alice, job_name, search_key, self.implicit_keys, self.explicit_keys, self.maxLoops, search_results_max_depth, self.iFileIO, self.newlinks)
            eventlog('COMPLETED ONLINE_THREADED_NAVIGATION_JOB')


            self.charlotte.state = 'halting_web_crawler'

        self.webtools.check_internet_connection()

        try:
            thread = Thread(target = process_job_phrases, args = (job_search_phrases, ))
            thread.start()
            while self.state != 'halting_web_crawler':
                eventlog("charllote")
                sleep(0.5)
                eventlog("is")
                sleep(0.5)
                eventlog('crawling')
                sleep(0.5)
                eventlog('the')
                sleep(0.5)
                eventlog('web')
                sleep(0.5)
                # process_job_phrases(job_search_phrases)

        except:
            eventlog('EXCEPTION')
            eventlog('process_job_phrases(job_search_phrases)')
            sleep(3)


        # re-write text files so that the current job name is placed in job_list_parsed list, the rest re-write to job_list
        with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/job_list.csv'), 'w') as f:
            with open(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/job_list_parsed.csv'), 'a') as f_append:
                for job in self.job_names:

                    if job_name.find(' ') != -1:
                        job_name = job_name.replace(' ', '_')

                    if job.find(' ') != -1:
                        job = job.replace(' ', '_')

                    eventlog('for job in self.job_names:')
                    if job != job_name:
                        eventlog(job + ' not equal to ' + job_name)
                        f.write(str(job))
                        f.write('\n')
                    else:
                        eventlog(job + ' is equal to ' + job_name)
                        f_append.write(str(job))
                        f_append.write('\n')

                if len(self.job_names) <= 1:
                    job_parsed_list = get_list_from_file(str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/job_list_parsed.csv'))
                    searching = True
                    while searching:
                        for item in job_parsed_list:
                            if item.find(' ') != -1:
                                item = item.replace(' ', '_')

                            if job_name.find(' ') != -1:
                                job_name = job_name.replace(' ', '_')

                            if item == job_name:
                                searching = False

                        f_append.write(str(job_name))
                        f_append.write('\n')
                        searching = False

        # exit()

        self.state = 'idle'

        eventlog('PARSING LOOP END!!!')
        eventlog('PARSING LOOP END!!!')
        eventlog('PARSING LOOP END!!!')
        eventlog('PARSING LOOP END!!!')
        eventlog('PARSING LOOP END!!!')
        eventlog('PARSING LOOP END!!!')
        sleep(3)

        log_state_thread.join()

        exit()
        # else:
        #     eventlog('waiting for job name!')
        #     sleep(3)









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

    #-----------------------                INACTIVE FUNCTIONS

    #-----------------------                INACTIVE FUNCTIONS

    #-----------------------                INACTIVE FUNCTIONS

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='debuginfo', depth=1)
    def debuginfo(self, message):
        caller = getframeinfo(stack()[1][0])
        #frame = inspect.previ
        #eventlog( "%s:%d - %s" % (caller.filename, caller.lineno, message))
        #eventlog("\n | ")
        #eventlog("|Charlotte line| " + str(caller.lineno) + " start.")
        #eventlog("\n | ")
        self.debugMessageList = []
        if message is not list:
            self.debugMessageList.append(message)
        else:
            self.debugMessageList = message
        self.f = open("parse.txt", "a+")
        #self.f.write(str("|Charlotte line| " + str(caller.lineno) + "| "))
        if message is list:
            for i in range(0, len(self.debugMessageList)):
                eventlog(str("debuginfo|" + str(caller.lineno) + "|START| " + str(self.debugMessageList[i]) + "  " + str(caller.lineno) +" |END|"))
                #self.f.write(str("" + str(caller.lineno) + "|START| " + str(self.debugMessageList[i]) + "  " + str(caller.lineno) +" |END|"))
        else:
            eventlog(str("debuginfo|" + str(caller.lineno) + "|START| " + str(self.debugMessageList[0])  + "  " + str(caller.lineno) +" |END|"))
            #self.f.write(str("debuginfo|" + str(caller.lineno) + "|START| " + str(self.debugMessageList[0])  + "  " + str(caller.lineno) +" |END|"))
        #eventlog("\n | ")
        #eventlog("\n | ")
        self.f.close()

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='getAccesshistoryData', depth=1)
    def getAccesshistoryData(self, filepath, maxLoops):
        b_filepath_exists, b_new, dp, fp, fp_access_history = FileIO.getPathsAndTime(self, filepath)
        if b_filepath_exists:
            filepath = str(dp + "getAccesshistoryData.csv")
            time_human, time_system = Chronos.getProperTime(self)
            f = open(filepath, "a+")
            f.write((time_human))
            f.write("\n")
            f.write(str(time_system))
            f.write("\n")
            f.close()

        list_accesshistory = FileIO.getListFromFile(self, filepath, maxLoops)
        for i in range(len(list_accesshistory), 1):
            if len(list_accesshistory) > 1 and time_human != '' and time_system != '':
                break

            if str(list_accesshistory[i]).find("-") != -1:
                time_human = list_accesshistory[i]
                #self.debuginfo("Last accessed: \n " + str(time_human) )
            else:
                time_system = list_accesshistory[i]
                #self.debuginfo("Last accessed: \n " + str(time_system) )
            if i == 0:
                break
            i -= 1
        return time_human, time_system, list_accesshistory


        time_human, time_system = Chronos.getProperTime(self)
        fp_access_history = self.writeFileAs(fp, "access_history", str(str(time_human) + "\n"), 'a+')
        fp_access_history = self.writeFileAs(fp, "access_history", str(str(time_system) + "\n"), 'a+')
        return b_filepath_exists, b_new, dp, fp, fp_access_history

    '''
    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='compileVisitedAndFailedLists', depth=1)
    def compileVisitedAndFailedLists(self, ignoreExisting, maxLoops):
        linksFP =  str( os.getcwd() + '/DATABASE/combined/totalLinks.csv')
        self.csvFP =  str( os.getcwd() + '/DATABASE/visited/visitedindex.csv')
        self.fields = ["Filepath", "date", "url"]
        #self.field = "testfield"
        #self.value = "testvalue"
        #self.values = ["filepathtest", "datetest", "urltest"]
        #self.my_dictionary = {1: {'Filepath': '', 'date': '', 'url': ''}}
        combineMinedurls(self, ignoreExisting, maxLoops)
        self.removeDuplicatesFromFile(linksFP, maxLoops)
        failedLinksListFP = str( os.getcwd() + '/DATABASE/visited/failedLinksList.csv')
        self.removeDuplicatesFromFile(failedLinksListFP, maxLoops)
        if not os.path.exists( str( os.getcwd() + '/DATABASE/visited/')):
            os.makedirs( str( os.getcwd() + '/DATABASE/visited/'))
            makeCsv(self, self.csvFP, self.fields)
        elif not os.path.isfile( str( os.getcwd() + '/DATABASE/visited/visitedindex.csv')):
            makeCsv(self, self.csvFP, self.fields)
        self.listOfurls = []
        self.listOfurls = getListFromFile(self, linksFP, maxLoops)
        self.listIndex = 0
        self.visitedurlsList = []
        self.failedLinksList = []
        if ignoreExisting:
            #self.debuginfo(" IGNORING EXISTING FILES = \n")
           #sleep(0.001)
            self.missingfp_urls = []
            for item in self.listOfurls:
                exists, fp_url = self.getindexFilepathFromUrl(item)
                if exists == False:
                    self.debuginfo(" targeting url " + item)
                   #sleep(0.001)
                    self.missingfp_urls.append(item)
                else:
                    self.debuginfo(" skipping url " + item)
            self.listOfurls = self.missingfp_urls
        for link in self.listOfurls:
            try:
                #create a directory tree representing the web index html file
                #update the csv index of all known web
                successBool, filepath, date, url = self.geturlMappedToDirectory(link)
                if successBool == True:
                    self.debuginfo("able to visit: " + url)
                self.my_dictionary[self.listIndex] = {}
                self.my_dictionary[self.listIndex]['Filepath'] = filepath
                self.my_dictionary[self.listIndex]['date'] = date
                self.my_dictionary[self.listIndex]['url'] = url
                self.writeDictToCsv(self.csvFP, self.my_dictionary, self.fields, self.listIndex)
                self.listIndex += 1
                self.visitedurlsList.append(link)
                appendToFile(self, str( os.getcwd() + '/DATABASE/visited/visitedurlsList.csv'), link)
            except:
                #self.debuginfo("\n\n - - - - - - - - - EXCEPTION - - - - - - - - - \n\n")
                #update the csv index of all known web
                #self.debuginfo(" UNABLE TO MAP url ")
                self.failedLinksList.append(link)
                appendToFile(self, str( os.getcwd() + '/DATABASE/visited/failedLinksList.csv'), link)
                #sleep(0.001)
    '''

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='getEmailList', depth=1)
    def getEmailList(self, filepath, maxLoops):
        #raw = session.driver.page_source
        f = open(filepath, 'r')
        self.raw = f.read()
        '''
        soup = BeautifulSoup(raw, "lxml")
        hrefList = []
        for a in soup.find_all('a', href=True):
            #self.debuginfo("Found the url:", a['href'])
            hrefList.append(a['href'])
        '''
        emails = []
        emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", self.raw)
        duplicateLessEmails = []
        duplicateLessEmails = DatabaseTools.getListWithoutDuplicates(self, emails)
        self.cleanedEmails = []
        self.list_ignore_emails = FileIO.get_list_from_file(self, str( os.getcwd() + '/list_ignore_emails.csv'), maxLoops)
        for item in duplicateLessEmails:
            if self.validateItemBasedOnList(item, self.list_ignore_emails):
                self.cleanedEmails.append(item)
        f.close()
        return self.cleanedEmails

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='soupGetPhone', depth=1)
    def soupGetPhone(self, data, siteLink):
        phone = re.findall(re.compile(r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|suffix)\s*(\d+))?'), data)

        if phone:
            number = ''.join(phone[0])
            if len(number) < 10:
                #self.debuginfo(str(siteLink))
                #self.debuginfo("\n +++++ FOUND ++++ " + str(number) + " +++++ FOUND ++++ \n")
                return True, str('+' + number)
            else:
                #self.debuginfo(str(siteLink))
                #self.debuginfo("\n +++++ FOUND ++++ " + str(number) + " +++++ FOUND ++++ \n")
                return True, str(number)
        else:
            return False, ''

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='soupGetHarvest', depth=1)
    def soupGetHarvest(self, filepath, siteLink, alice_nlp, a_matcher):
        #raw = session.driver.page_source
        readIt = open(filepath, 'r')
        soup = BeautifulSoup(readIt, 'html.parser')
        #links = [a['href'] for a in soup.select('a[href]')]
        head_tag = soup.head
        head_tag
        head_tag.contents
        siteContents = head_tag.contents
        #self.debuginfo("\n")
        #self.debuginfo("+++++ SITE CONTENT BEGIN ++++")
        #self.debuginfo(str(filepath))
        #self.debuginfo("\n")
        #self.debuginfo(str(siteLink))
        #self.debuginfo("\n")
        #self.debuginfo("+++++ SITE CONTENT BEGIN ++++")
        #self.debuginfo("\n")
        self.Title = ''
        self.TitleBool = False
        self.WebPagePhoneNumber = ''
        self.WebPagePhoneBool = False
        self.alice_entity_bool = False
        self.soupResult = ''
        for content in siteContents:
            if content != '':
                if len(content) < 500:
                    data = self.csvFormat(content)
                    #self.debuginfo("STANDARD PARSING: " + data)

                    if self.TitleBool == False:
                        self.TitleBool, self.soupResult = self.webtools.soupGetTitle( str(data), siteLink)
                        if self.TitleBool == True:
                            self.Title = self.soupResult

                    if self.WebPagePhoneBool == False:
                        self.WebPagePhoneBool, self.soupResult = self.soupGetPhone(str(data), siteLink)
                        if self.WebPagePhoneBool == True:
                            self.WebPagePhoneNumber = self.soupResult
        page = soup.find_all('p')
        for content in page:
            if content != '':
                if len(content) < 500:
                    data = self.csvFormat(content)
                    #self.debuginfo("NLP PARSING: " + data)
                    data = str(page)
                    #self.debuginfo(data)
                    if self.alice_entity_bool == False:
                        temp_a = []
                        temp_b= []
                        temp_c = []
                        temp_d = []
                        self.alice_entity_bool, temp_a, temp_b, temp_c, temp_d = self.Alice_Get_Entity(str(data), alice_nlp, a_matcher)
                        if self.alice_entity_bool == True:
                            self.a_entity_texts = temp_a
                            self.a_entity_start_char = temp_b
                            self.a_entity_end_char = temp_c
                            self.a_entity_label = temp_d
        #self.debuginfo("\n")
        #self.debuginfo("+++++ SITE CONTENT END ++++")
        #self.debuginfo("+++++ SITE CONTENT END ++++")
        #self.debuginfo("\n")
        #sleep(0.001)
        return self.Title, self.WebPagePhoneNumber, self.a_entity_texts, self.a_entity_start_char, self.a_entity_end_char, self.a_entity_label

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='Alice_Get_Entity', depth=1)
    def Alice_Get_Entity(self, data, alice_nlp, a_matcher):
        try:
            nlp = spacy.load("en_core_web_sm")
            doc = nlp(data)
            self.a_entity_texts = []
            self.a_entity_start_char = []
            self.a_entity_end_char = []
            self.a_entity_label = []
            for ent in doc.ents:
                ##self.debuginfo(ent.text, ent.start_char, ent.end_char, ent.label_)
                #self.debuginfo("ent.text = = " + str(ent.text))
                #self.debuginfo("ent.start_char = = " + str(ent.start_char))
                #self.debuginfo("ent.end_char = = " + str(ent.end_char))
                #self.debuginfo("ent.label_ = = " + str(ent.label_))
                #sleep(0.001)
                self.a_entity_texts.append(str(ent.text))
                self.a_entity_start_char.append(str(ent.start_char))
                self.a_entity_end_char.append(str(ent.end_char))
                self.a_entity_label.append(str(ent.label_))
            return True, self.a_entity_texts, self.a_entity_start_char, self.a_entity_end_char, self.a_entity_label
        except:
            #self.debuginfo("\n\n - - - - - - - - - EXCEPTION - - - - - - - - - \n\n")
            #self.debuginfo("Alice_Get_Entity FAILED")
           #sleep(1.5)
            return False, '', '', '', ''

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='getHarvest', depth=1)
    def getHarvest(self, filepath, siteLink, maxLoops, alice_nlp, a_matcher):
        self.date = ''
        self.emails = ''
        self.Title = ''
        self.WebPagePhoneNumber = ''
        self.a_entity_texts = []
        self.a_entity_start_char = []
        self.a_entity_end_char = []
        self.a_entity_label = []
        self.date = Chronos.getProperTime(self)
        self.emails = self.getEmailList(filepath, maxLoops)
        #use soup
        self.Title, self.WebPagePhoneNumber,  self.a_entity_texts, self.a_entity_start_char, self.a_entity_end_char, self.a_entity_label = self.soupGetHarvest(filepath, siteLink, alice_nlp, a_matcher)

        #self.debuginfo("\n")
        #self.debuginfo("| -- + -- -- + -- -- + -- -- -- + -- -- + -- -- + -- -- + -- | ")
        #self.debuginfo("| -- -- -- -- -- -- -- -- -- HARVEST -- -- -- -- -- -- -- -- | ")
        #self.debuginfo("| -- + -- -- + -- -- + -- -- -- + -- -- + -- -- + -- -- + -- | ")
        #self.debuginfo("\n")

        #self.debuginfo("DATE: " + self.date)
        for email in self.emails:
            self.debuginfo("EMAIL: " + email)
        #self.debuginfo("TITLE: " + self.Title)
        #self.debuginfo("Phone: " + self.WebPagePhoneNumber)
        for entity in self.a_entity_texts:
            self.debuginfo("Entities: " + entity)
            #sleep(0.001)
        #self.debuginfo("\n")
        #self.debuginfo("| -- + -- -- + -- -- + -- -- -- + -- -- + -- -- + -- -- + -- | ")
        #self.debuginfo("| -- -- -- -- -- -- -- -- -- HARVEST -- -- -- -- -- -- -- -- | ")
        #self.debuginfo("| -- + -- -- + -- -- + -- -- -- + -- -- + -- -- + -- -- + -- | ")
        #self.debuginfo("\n")
        #sleep(0.001)
        return self.date, self.emails, self.Title, self.WebPagePhoneNumber, self.a_entity_texts, self.a_entity_start_char, self.a_entity_end_char, self.a_entity_label




    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='validateItemBasedOnList', depth=1)
    def validateItemBasedOnList(self, item, list_ignore):
        boolValid = True
        complete = False
        while complete == False:
            for ignored in list_ignore:
                if str(item).lower().find(str(ignored).lower()) != -1:
                    boolValid = False
                    complete = True
            #self.debuginfo(" " + item + " " + " is " + str(boolValid) )
            complete = True
        return boolValid

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='csvFormat', depth=1)
    def csvFormat(self, string):
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
       ##sleep(0.001)
        return self.s0

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='removeDuplicatesFromFile', depth=1)
    def removeDuplicatesFromFile(self, filepath, maxLoops):
        #self.debuginfo("def removeDuplicatesFromFile(self, filepath):")
        if os.path.isfile(filepath):
            lines = FileIO.getListFromFile(self, filepath, maxLoops)
            duplicatelessList = []
            duplicatelessList = DatabaseTools.getListWithoutDuplicates(self, lines)
            FileIO.clear_file(self, filepath)
            FileIO.writelistOfStuff(self, duplicatelessList, filepath)
            return True, filepath
        else:
            return False, filepath

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='dictionary_eventlog_keys_recursively', depth=1)
    def dictionary_eventlog_keys_recursively(self, theDict):
          #self.debuginfo("dictionary_eventlog_keys_recursively")
        for job in theDict.keys():
            self.debuginfo(str(job) + str(":"))
            for info in theDict[job].values():
                self.debuginfo(info)
               ##sleep(0.001)
        #self.debuginfo("\n")

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='dictionary_eventlog', depth=1)
    def dictionary_eventlog(self):
        self.debuginfo(self.my_dictionary)
        #self.debuginfo("\n")
       #sleep(0.11)

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='dictionary_find_value', depth=1)
    def dictionary_find_value(self, value):
        self.debuginfo("dictionary_eventlog_keys_recursively")
        for job in self.my_dictionary.keys():
            self.debuginfo(str(job) + str(":"))
            for info in self.my_dictionary[job].values():
                self.debuginfo(info)
                #sleep(0.001)
                #self.debuginfo("\n")
                if info.find(value) != -1:
                    self.debuginfo(value)
                    #self.debuginfo("Alice found it in row " + job)

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='append_dictionary', depth=1)
    def append_dictionary(self, newDict):
        #self.debuginfo("append_dictionary")
        #self.debuginfo(self.my_dictionary)
        self.my_dictionary.update(newDict)
        #self.debuginfo(self.my_dictionary)
       #sleep(0.15)
    '''
    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='dictionary_merge', depth=1)
    def dictionary_merge(self, a,b):
        for key in b:
            if not key in a or type(a[key]) != dict or type(b[key])!=dict:
                a[key]=b[key]
            else:
                self.updatedict(a[key],b[key])
        return a
    '''
    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='get_dict_blank_memory', depth=1)
    def get_dict_blank_memory(self):
        memory = {'0': {'Date': 'Date', 'Filepath': 'Filepath', 'URL': 'URL', 'Email': 'Email', 'Title': 'Title', 'Phone': 'Phone', 'Text': 'Text', 'Start': 'Start', 'End': 'End', 'Label': 'Label'}}
        return memory

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='ahapPrototype', depth=1)
    def ahapPrototype(self):
        self.my_dictionary = self.get_dict_blank_memory()
        self.alice_nlp= spacy.load('en_core_web_sm')

        # initialize matcher with a vocab
        self.a_matcher = Matcher(self.alice_nlp.vocab)


        '''
        searchList = [
                    "revenue cycle management",
                    "director of patient financial servicd ",
                    "revenue management hospital",
                    "Federally Qualified Health",
                    "health director",
                    "fqhc",
                    "cfo health",
                    "ceo health",
                    "california health director",
                    "ceo health",
                    "california health director",
                    "Director California Federally Qualified Health Center Contact",
                    "email federally qualified health",
                    "health contacts federally qualified health center"]
        '''
        maxLoops = 1000000
        maxPages = 100
        searchList = ["Federally Qualified Health Center"]
        searchList = ["California Hospitals"]
        searchList = ["hospital director of financial"]
        #self.debuginfo("summon demons")

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='collect_dictionary_key_value', depth=1)
    def collect_dictionary_key_value(self, _Alice, keyData, valueData ):
        self.list_key_data = []
        self.list_value_data = []
        if keyData is not list:
            self.list_key_data.append(keyData)
        else:
            self.list_key_data = keyData

        if valueData is not list:
            self.list_value_data.append(valueData)
        else:
            self.list_value_data = valueData

        self.global_index, self.global_list_keys, self.global_list_values = _Alice.get_globals()
        self.refKeys = []
        self.refValues = []
        self.updatedKeys = []
        self.updatedValues = []
        if len(self.list_value_data) == len(self.list_key_data):
            for i in range(0, len(self.list_key_data)):
                self.refKeys.append(self.list_key_data[i])
                self.refValues.append(self.list_key_data[i])
        elif len(self.list_value_data) < len(self.list_key_data):
            for i in range(0, len(self.list_key_data)):
                self.refKeys.append(self.list_key_data[i])
                if len(self.list_value_data) < i:
                    self.refValues = str(self.refKeys[i] + ' value is none')
                else:
                    self.refValues = str(self.list_value_data[i])
        self.debuginfo(self.updatedKeys)
        self.debuginfo(self.updatedValues)
        self.zipDict  =  dict(zip(self.updatedKeys,self.updatedValues))
        self.debuginfo(self.zipDict)

        _Alice.set_globals(self.global_index, self.updatedKeys, self.updatedValues)
        return self.global_index, self.zipDict


    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='bot_Critical_Access_Hospital', depth=1)
    def online_bot_Critical_Access_Hospital(self, _Alice, maxLoops):
        self.m_Critical_Access_Hospital = _Alice.get_memory("m_Critical_Access_Hospital", maxLoops)
        self.time_system = ''
        self.time_human = ''
        self.list_accesshistory = []
        self.alice_nlp= spacy.load('en_core_web_sm')
        self.a_matcher = Matcher(self.alice_nlp.vocab)
        #self._Alice.show_globals()
        self.b_success = None
        #self.my_dictionary = self.get_dict_blank_memory()
        #self.alice_nlp= spacy.load('en_core_web_sm')
        self.dp_root = str(Path.home()) + "/p3env/alice/alice/spiders/criticalAccessHospitalMiner/"
        self.m_Critical_Access_Hospital.keys.append("dp_root")
        self.m_Critical_Access_Hospital.values.append(self.dp_root)
        self.b_filepath_exists, self.b_new, self.dp, fp, self.fp_access_history = FileIO.getPathsAndTime(self, self.dp_root)
        self.url_landingPage = "https://www.flexmonitoring.org/data/critical-access-hospital-locations/"
        self.m_Critical_Access_Hospital.keys.append("url_landingPage")
        self.m_Critical_Access_Hospital.values.append(self.url_landingPage)
        self.b_new_db = False
        self.b_new_db, self.htmlsourcepath, self.dp_db_web, self.navigation_targets, self.fp_db_archive, self.fp_db_realtime, self.fp_db_queue, self.fp_db_dev_report, self.fp_db_user_report, self.nlp_targets = FileIO.bot_db_initialize_filepaths(self, self.url_landingPage, self.dp_root)
        self.m_Critical_Access_Hospital.keys.append("htmlsourcepath")
        self.m_Critical_Access_Hospital.values.append(self.htmlsourcepath)

        #self.collect_dictionary_key_value(_Alice, "Filepath", self.htmlsourcepath)
        #self.collect_dictionary_key_value(_Alice,"Date", self.time_human)
        self.m_Critical_Access_Hospital.keys.append("time_human")
        self.time_human, self.systemTime = Chronos.getProperTime(self)
        self.m_Critical_Access_Hospital.values.append(self.time_human)
        #self.date = getProperTime(self)

        self.session = Session(webdriver_path=str(Path.home()) + '/p3env/alice/alice/spiders/chromedriver', browser='chrome', default_timeout=3)
        self.session.driver.set_window_size(1000, 2000)
        self.session.driver.get(self.url_landingPage)
        sleep(1.5)
        #download
        self.b_success, self.raw, self.htmlsourcepath, self.directory_key = self.selenium_download_page_source(self.session, self.session.driver.current_url, self.dp_db_web)
        sleep(1.5)
        #self.collect_dictionary_key_value(_Alice,"URL", self.session.driver.current_url)
        self.m_Critical_Access_Hospital.keys.append("URL")
        self.m_Critical_Access_Hospital.values.append(self.session.driver.current_url)
        sleep(1.5)
        #self.collect_dictionary_key_value(_Alice,"Text", "Connection Established.")
        self.m_Critical_Access_Hospital.keys.append("Message")
        self.m_Critical_Access_Hospital.values.append("Connection Established.")
        self.m_Critical_Access_Hospital.update(self.m_Critical_Access_Hospital.index, self.m_Critical_Access_Hospital.keys, self.m_Critical_Access_Hospital.values, maxLoops)
        self.m_Critical_Access_Hospital.index += 1

        self.b_success, self.raw, self.htmlsourcepath, self.directory_key = self.selenium_download_page_source(self.session, self.session.driver.current_url, self.dp_db_web)

        self.xpathTarget = str('//*[@id="cah-data"]/div/form/div/div/select')
        self.search_form = self.session.driver.find_element_by_xpath(self.xpathTarget)
        sleep(1.5)
        self.search_form.send_keys('-')
        sleep(1.5)
        self.search_form.submit()
        sleep(1.5)

        self.xpathTarget = str('//*[@id="result-list-table_length"]/label/select')
        self.search_form = self.session.driver.find_element_by_xpath(self.xpathTarget)
        sleep(1.5)
        self.search_form.send_keys('All')
        sleep(1.5)
        #self.search_form.submit()
        sleep(1.5)
        self.b_success, self.raw, self.htmlsourcepath, self.directory_key = self.selenium_download_page_source(self.session, self.session.driver.current_url, self.dp_db_web)
        
        self.m_web_directory_key = _Alice.get_memory(self.directory_key, maxLoops)
        self.m_web_directory_key.keys.append("htmlsourcepath")
        self.m_web_directory_key.values.append(self.htmlsourcepath)
        self.m_web_directory_key.keys.append("directory_key")
        self.m_web_directory_key.values.append(self.directory_key)

        self.m_web_directory_key.update(self.m_web_directory_key.index, self.m_web_directory_key.keys, self.m_web_directory_key.values, maxLoops)
        self.m_web_directory_key.index += 1

        readIt = open(self.htmlsourcepath, 'r')
        soup = BeautifulSoup(readIt, 'html.parser')
        head_tag = soup.head
        head_tag
        head_tag.contents
        siteContents = head_tag.contents
        self.Title = ''
        self.TitleBool = False
        self.WebPagePhoneNumber = ''
        self.WebPagePhoneBool = False
        self.alice_entity_bool = False
        self.soupResult = ''
        for content in siteContents:
            self.debuginfo(content)
            '''
            if content != '':
                if len(content) < 500:
                    data = self.csvFormat(content)
                    #self.debuginfo("STANDARD PARSING: " + data)

                    if self.TitleBool == False:
                        self.TitleBool, self.soupResult = soupGetTitle(self, str(data), self.session.driver.current_url)
                        if self.TitleBool == True:
                            self.Title = self.soupResult

                    if self.WebPagePhoneBool == False:
                        self.WebPagePhoneBool, self.soupResult = self.soupGetPhone(str(data),s elf.session.driver.current_url)
                        if self.WebPagePhoneBool == True:
                            self.WebPagePhoneNumber = self.soupResult
            '''
        page = soup.find_all('p')
        for content in page:
            self.debuginfo(content)
            '''
            if content != '':
                if len(content) < 500:
                    data = self.csvFormat(content)
                    #self.debuginfo("NLP PARSING: " + data)
                    data = str(page)
                    #self.debuginfo(data)
                    if self.alice_entity_bool == False:
                        temp_a = []
                        temp_b= []
                        temp_c = []
                        temp_d = []
                        self.alice_entity_bool, temp_a, temp_b, temp_c, temp_d = self.Alice_Get_Entity(str(data), self.alice_nlp, self.a_matcher)
                        if self.alice_entity_bool == True:
                            self.a_entity_texts = temp_a
                            self.a_entity_start_char = temp_b
                            self.a_entity_end_char = temp_c
                            self.a_entity_label = temp_d
            '''
        #self.debuginfo("\n")
        #self.debuginfo("+++++ SITE CONTENT END ++++")
        #self.debuginfo("+++++ SITE CONTENT END ++++")
        #self.debuginfo("\n")
        #sleep(0.001)



        self.session.driver.quit()
        sleep(1.5)

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='bot_Critical_Access_Hospital', depth=1)
    def offline_bot_Critical_Access_Hospital(self, _Alice, maxLoops):
        self.max = maxLoops
        self.m_url_targets_list = _Alice.get_memory("httpswwwflexmonitoringorgdatacriticalaccesshospitallocations", maxLoops)
        self.sourcePath_list = self.m_url_targets_list.get_list_field("htmlsourcepath")
        self.htmlsourcepath = self.sourcePath_list[0]
        eventlog(str("HTMLSOURCEPATH = ") + str(self.htmlsourcepath))

        self.htmlLines = FileIO.get_list_from_file(self, self.htmlsourcepath, self.max)
        self.m_critical_access_hospitals = _Alice.get_memory("m_critical_access_hospitals", maxLoops)
        self.m_critical_access_hospitals.keys.append("Name")
        self.m_critical_access_hospitals.keys.append("City")
        self.m_critical_access_hospitals.keys.append("State")
        self.m_critical_access_hospitals.keys.append("Zip")
        self.m_critical_access_hospitals.keys.append("Certified")
        self.m_critical_access_hospitals.keys.append("Beds")
        self.previousLine = ''
        self.loopsIndex = 0
        self.b_working = True
        self.max = maxLoops
        while self.b_working == True:
            for line in self.htmlLines:

                eventlog("maxLoops " + str(self.max))
                eventlog("self.loopsIndex " + str(self.loopsIndex))
                eventlog("LINE: " + str(line))
                if maxLoops > self.max:
                    self.b_working = False
                    break
                if line.find('<td class="report  sorting_1">') != -1:
                    string = str(DatabaseTools.find_between(self, str(line), ">", "<"))
                    eventlog(string)
                    self.m_critical_access_hospitals.values.append(DatabaseTools.find_between(self, str(line), ">", "<"))
                elif self.previousLine.find('<td class="city  sorting_2">') != -1:
                    string = str(DatabaseTools.find_between(self, str(line), "                                                ", "                                            </td>"))
                    eventlog(string)
                    self.m_critical_access_hospitals.values.append(string)
                elif self.previousLine.find('<td class="state  sorting_3">') != -1:
                    string = str(DatabaseTools.find_between(self, str(line), "                                                ", "                                            </td>"))
                    eventlog(string)
                    self.m_critical_access_hospitals.values.append(string)
                elif self.previousLine.find('<td class="zip  sorting_3">') != -1:
                    string = str(DatabaseTools.find_between(self, str(line), "                                                ", "                                            </td>"))
                    eventlog(string)
                    self.m_critical_access_hospitals.values.append(string)
                elif self.previousLine.find('<td class="eff  sorting_3">') != -1:
                    string = str(DatabaseTools.find_between(self, str(line), "                                                                                                ", "                                            </td>"))
                    eventlog(string)
                    self.m_critical_access_hospitals.values.append(string)
                elif self.previousLine.find('<td class="beds  sorting_3">') != -1:
                    string = str(DatabaseTools.find_between(self, str(line), "                                                ", "                                            </td>"))
                    eventlog(string)
                    self.m_critical_access_hospitals.values.append(string)
                    self.m_critical_access_hospitals.record(self.m_critical_access_hospitals.index, self.m_critical_access_hospitals.keys, self.m_critical_access_hospitals.values, maxLoops)

                    self.m_critical_access_hospitals.index += 1
                    self.loopsIndex += 1
                self.previousLine = line
            self.b_working = False
            self.m_critical_access_hospitals.write(maxLoops)

    def get_url_memory(self, _Alice, url, maxLoops):
        from urllib.parse import urlparse, urljoin
        parsed = urlparse(url)
        eventlog('scheme  :', parsed.scheme)
        eventlog('netloc  :', parsed.netloc)
        eventlog('path    :', parsed.path)
        eventlog('params  :', parsed.params)
        eventlog('query   :', parsed.query)
        eventlog('fragment:', parsed.fragment)
        eventlog('username:', parsed.username)
        eventlog('password:', parsed.password)
        eventlog('hostname:', parsed.hostname)
        eventlog('port    :', parsed.port)
        return _Alice.get_memory(str(str("m_") + str(parsed.netloc)), maxLoops)

    def get_phrase_memory(self, _Alice, phrase, maxLoops):
        memory_phrase = str(phrase.replace(" ", "_"))
        return _Alice.get_memory(str(str("m_") + memory_phrase), maxLoops)

    #@pysnooper.snoop(str(Path.home()) + '/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='flag_failed_error', depth=1)
    def flag_failed_error(self, _Alice, filepath, phrase, session, maxLoops):
            m_flag_failed_error = _Alice.get_memory("m_flag_failed_error", maxLoops)
            m_flag_failed_error.keys.append("data")
            m_flag_failed_error.values.append(phrase)
            m_flag_failed_error.keys.append("url")
            eventlog("URL " + str(session.driver.current_url))
            #session.driver.get(session.driver.current_url)
            sleep(2)
            eventlog(str("\n\n driver.page_source\n\n " + str('{:.500}'.format(str(session.driver.page_source))) + "\n\n driver.page_source\n\n "))
            self.raw = session.driver.page_source
            filepath = self.writeFileAs(self.fp_db_web, 'failed', self.raw, 'a+')
            m_flag_failed_error.values.append(filepath)
            m_flag_failed_error.keys.append("Date")
            human_time, system_time = Chronos.getProperTime(self)
            m_flag_failed_error.values.append(human_time)
            m_flag_failed_error.update(m_flag_failed_error.index, m_flag_failed_error.keys, m_flag_failed_error.values, maxLoops)
            m_flag_failed_error.index += 1



    def calculate_priorities(self, _Alice, name, maxLoops):
        
        #eventlog('path    :', parsed.path)
        self.m_web_cache = _Alice.get_memory(str('m_web_cache'), maxLoops)
        #self.m_web_cache.keys.append("name")
        #self.m_web_cache.values.append(str(name))
        list_name = self.m_web_cache.get_list_field("name")
        #self.m_web_cache.keys.append("date")
        human_time, system_time = Chronos.getProperTime(self)
        #self.m_web_cache.values.append(system_time)
        list_date = self.m_web_cache.get_list_field("date")
        list_priority = self.m_web_cache.get_list_field("priority")
        self.adjustment = 0
        if list_name:
            self.adjustment -= 1
            for item in list_name:
                self.adjustment -= 1
        else:
            self.adjustment += 1
        if list_date:
            self.adjustment -= 1
            for item in list_date:
                self.adjustment -= 1
        else:
            self.adjustment += 1

        self.priority = 0

        if list_priority:
            self.adjustment -= 1
            for item in list_priority:
                self.adjustment -= 1
                self.priority = int(item)
        else:
            self.priority = 0
        #self.m_web_cache.keys.append("priority")
        self.priority = int(self.priority + self.adjustment)
        #self.m_web_cache.values.append(self.priority)
        #self.m_web_cache.record(self.m_web_cache.index, #self.m_web_cache.keys, self.m_web_cache.values, maxLoops)
        #self.m_web_cache.index += 1
        #memory.write()
        #self.m_web_cache = _Alice.get_memory("m_web_cache", maxLoops)
        #self.m_web_cache.keys.append("name")
        #self.m_web_cache.keys.append("priority")
        #self.m_web_cache.values.append(str(name))
        #self.m_web_cache.values.append(self.priority)

        #self.m_web_cache.record(self.m_web_cache.index, #self.m_web_cache.keys, self.m_web_cache.values, maxLoops)
        #self.m_web_cache.index += 1
        #priorities.write()

        return self.m_web_cache, self.m_web_cache









ACTIVE_CRAWLERS_DICT = {}

def get_or_new_active_crawler(human):
    if ACTIVE_CRAWLERS_DICT.get(str(human)) == None:
        eventlog(str('user: ' + str(human) + ' is active and needs a spider!'))
        # self.assign_robot_to_user(str(human))
        ACTIVE_CRAWLERS_DICT[human] = CrawlerProcess()
    return ACTIVE_CRAWLERS_DICT.get(str(human))

ALICE_USER_ASSIGNMENT_DICT = {}


class Alice:
    def __init__(self, name, human):
        self.name = name
        self.alive = True
        self.human = human
        self.switchboard = None
        self.crawler = None
        self.charlotte = None
        self.initialized = False
        self.crawler_thread = None
        self.spider_log = []
        self.state = 'initialized'
        self.printer = []
        self.previous_printer_length = 0

    def print_printer(self):
        try:
            if self.previous_printer_length < len(self.printer):
                record = str(self.printer[-1])
                self.previous_printer_length = len(self.printer)
                eventlog('printer: ' + record)
                record = (record[:75] + '...') if len(record) > 75 else record
                self.send_message(str(record), 'print')
        except Exception as e:
            eventlog('ERROR: ' + str(e))
            pass

    def run(self):
        # log_state_thread = Thread(target = self.log_state)
        # log_state_thread.start()
        eventlog(str(self.name) + ' is alive.')
        eventlog('Alice LOOP = IOLoop.current(): ' + str(WS.LOOP))
        # eventlog('Switchboard SWITCHBOARD = ' + str(SWITCHBOARD))
        while self.alive:
            # jobs_filepath = str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/spider_log.log')
            # try:
            #     self.send_message('spider server: alice: state: ' + str(self.state), 'print')
            #     # self.spider_log = get_list_from_file(jobs_filepath)
            #     # for record in self.spider_log:
            #     #     eventlog('spider log: ' + str(record))
            #         # self.send_message('Charlotte log: ' + str(record), 'print')
            # except Exception as e:
            #     eventlog('EXCEPTION: ' + str(e))
            #     pass
            eventlog('spider server: alice: state: ' + str(self.state))
            # self.send_message('spider server: alice: state: ' + str(self.state), 'print')
            # eventlog('about to print printer')
            # self.print_printer()
            sleep(0.3)
            # SWITCHBOARD = self.switchboard
        eventlog(str(self.name) + ' is DEAD!')
        sleep(1)
        log_state_thread.join()
        exit()

    def spider_log(self):
        jobs_filepath = str(str(Path.home()) + '/p3env/alice/alice/spiders/DATABASE/JOBS/spider_log.log')
        try:
            self.spider_log = get_list_from_file(jobs_filepath)
            for record in self.spider_log:
                eventlog('spider log: ' + str(record))
                # self.send_message('Charlotte log: ' + str(record), 'print')
        except Exception as e:
            eventlog('spider log: ' + str(record))
            pass

    def on_message(self, message):
        loaded_dict_data = json.loads(message)
        command = loaded_dict_data.get('command', None)
        message = loaded_dict_data.get('message', None)
        robot_id = loaded_dict_data.get('robot_id', None)
        human = loaded_dict_data.get('human', None)
        username = loaded_dict_data.get('username', None)

        if command == 'search':
            eventlog('command IS SEARCH')
            self.search(message)

        if command == 'stop':
            eventlog('command IS STOP SEARCH')
            self.stop_search()


    def search(self, message):

        eventlog(self.name + ' search method activated.')
        self.send_message('I am initializing the webcrawler.', 'print')
        if self.initialized == False:
            self.crawler = get_or_new_active_crawler(self.human)
            self.crawler.crawl(Charlotte, alice=self)
            self.initialized = True
        sleep(0.5)
        self.charlotte.write_job_keys(message)
        sleep(0.5)
        self.send_message("Charlotte's crawling the web...", 'print')
        self.crawler_thread = threading.Thread(target=self.crawler.start)
        self.crawler_thread.daemon = True
        self.crawler_thread.start()

        self.state = 'searching'
        # while self.state == 'searching':
        #     # self.send_message("Charlotte is searching..." + get_date_and_time_string(), 'print')
        #     # sleep(3)

        #     try:
        #         if self.previous_printer_length < len(self.printer):
        #             record = str(self.printer[-1])
        #             self.previous_printer_length = len(self.printer)
        #             eventlog('printer: ' + record)
        #             record = (record[:75] + '..') if len(record) > 75 else record
        #             self.send_message(str(record), 'print')

        #     except Exception as e:
        #         eventlog('spider log: ' + str(record))
        #         pass

        if self.state == 'stop_search':
            self.stop_search()






        if self.state == 'stop_search':
            self.stop_search()




        eventlog("SEARCHING .....")

    def stop_search(self):
        self.state = 'initialized'
        eventlog(self.name + ' STOP_SEARCH')
        eventlog(self.name + ' STOP_SEARCH')
        eventlog(self.name + ' STOP_SEARCH')
        self.send_message("self.charlotte.stop_search()", 'print')
        self.charlotte.stop_search()
        self.send_message("self.crawler.stop()", 'print')
        sleep(2)
        self.crawler.stop()
        self.send_message(self.name + ' stop search method activated.', 'print')
        eventlog(self.name + ' stop search method activated.')

        # self.crawler_thread.join()
        self.send_message(str(self.name + ' stopped search.'), 'print')


    def send_message(self, message, command):
        text = {
            'message': message,
            'command': command,
            'From': self.name,
            'human': self.human
        }
        eventlog('SENDING MESSAGE TO WEBHARVEST: ' + str(text))

        self.switchboard.write_message(json.dumps(text))




class MainHandler(tornado.web.RequestHandler):
    def get(self):
        loader = tornado.template.Loader(".")
        self.write(loader.load("index.html").generate())

class Switchboard(tornado.websocket.WebSocketHandler):
    # def __init__(
    #     self,
    #     application: tornado.web.Application,
    #     # request: httputil.HTTPServerRequest,
    #     **kwargs
    #     ) -> None:
    #     super(WebSocketHandler, self).__init__(application, request, **kwargs)
    #     self.ws_connection = None  # type: Optional[WebSocketProtocol]
    #     self.close_code = None  # type: Optional[int]
    #     self.close_reason = None  # type: Optional[str]
    #     self.stream = None  # type: Optional[IOStream]
    #     self._on_close_called = False
    #     self.httputil = None

    def open(self):
        SWITCHBOARD = self
        eventlog ('connection opened...')
        eventlog('Switchboard LOOP = IOLoop.current(): ' + str(WS.LOOP))
        eventlog('Switchboard SWITCHBOARD = ' + str(SWITCHBOARD))
        # text = {
        #     "message": "The server says: 'Hello'. Connection was accepted.",
        # }
        # self.write_message(json.dumps(text))
        # self.write_message("The server says: 'Hello'. Connection was accepted.")

    # def write_message(self, message, binary=False):
    #         data = json.dumps(message)
    #         return super(Switchboard, self).write_message(data, binary)

    def on_message(self, message):
        eventlog("on_message: " + str(message))
        loaded_dict_data = json.loads(message)
        human = loaded_dict_data.get('human', None)
        command = loaded_dict_data.get('command', None)

        if ALICE_USER_ASSIGNMENT_DICT.get(str(human)) == None:
            eventlog(str('user: ' + str(human) + ' is active and needs a robot!'))
            self.assign_robot_to_user(str(human))
        
        if command == 'stop_search':
            eventlog('SWITCHBOARD STOP SEARCH FOR ' + human)
            eventlog('SWITCHBOARD STOP SEARCH FOR ' + human)
            eventlog('SWITCHBOARD STOP SEARCH FOR ' + human)
            ALICE_USER_ASSIGNMENT_DICT.get(str(human)).state = 'stop_search'
        else:
            eventlog('SWITCHBOARD SEND MESSAGE FOR ' + human)
            eventlog('SWITCHBOARD SEND MESSAGE FOR ' + human)
            eventlog('SWITCHBOARD SEND MESSAGE FOR ' + human)
            ALICE_USER_ASSIGNMENT_DICT.get(str(human)).on_message(message)

    def on_close(self):
        eventlog('connection closed...')


    def assign_robot_to_user(self, human):
        eventlog('assign_robot_to_user....')
        thread = ALICE_USER_ASSIGNMENT_DICT.get(human)
        eventlog('Alice robot thread: ' + str(thread))
        if thread == None:
            eventlog('human not found...')
            robot = Alice('Alice', str(human))
            robot_thread = threading.Thread(target=robot.run)    
            robot_thread.daemon = True
            robot_thread.start()
            robot.thread = robot_thread
            robot.switchboard = self
            ALICE_USER_ASSIGNMENT_DICT[human] = robot
        
        thread = ALICE_USER_ASSIGNMENT_DICT.get(human)
        eventlog('Alice thread: ' + str(thread))




class WebsocketServer(tornado.web.Application):

    def __init__(self):
        self.LOOP = IOLoop.current()
        eventlog('WebsocketServer LOOP = IOLoop.current(): ' + str(self.LOOP)) 
        # eventlog('Switchboard SWITCHBOARD = ' + str(SWITCHBOARD))
        # self.SWITCHBOARD = Switchboard()
        # handlers = [ (r"/", MainHandler), (r"/ws", self.SWITCHBOARD),  ]

        handlers = [ (r"/", MainHandler), (r"/ws", Switchboard),  ]
        eventlog('handlers: ' + str(handlers))
        settings = {'debug': True}
        super().__init__(handlers, **settings)

    def run(self):


        self.listen(port=9090)
        tornado.ioloop.IOLoop.instance().start()

    def stop(self):
        tornado.ioloop.IOLoop.instance().start()



if __name__ == "__main__":


    # eventlog("Charlotte is searching..." + get_date_and_time_string() + 'print')
    WS = WebsocketServer()
    # LOOP = asyncio.new_event_loop()
    WS.run()