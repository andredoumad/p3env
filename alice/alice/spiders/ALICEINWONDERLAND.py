from .AliceRequiredModules import *
from .fileio import FileIO
from .chronos import Chronos
from .csv_io import CSV_IO
from .databasetools import DatabaseTools
from .webtools import WebTools
from .standalone_tools import *

from pathlib import Path
class AliceInWonderland:
    #initialize start
    history_name = 'AliceInWonderland'
    directorypath = ( str( str(os.getcwd()) + '/DATABASE/history/' + history_name + '/'))
    if not os.path.exists( str( str(os.getcwd()) + '/DATABASE/history/' + history_name + '/')):
        os.makedirs( str( str(os.getcwd()) + '/DATABASE/history/' + history_name + '/'))
    history_filepath = str( str(os.getcwd()) + '/DATABASE/history/' + history_name + '.history')
    set_time = datetime.datetime.now()
    hour = str(set_time.strftime("%H"))
    minute = str(set_time.strftime("%M"))
    second = str(set_time.strftime("%S"))
    prefix = str('initialized-time-' + hour + minute + second)

    def set_history_filepath(self, history_filepath):
        history_filepath = history_filepath
        self.history_filepath = history_filepath

    def set_history_name(self, history_name):
        history_name = history_name
        self.history_name = history_name

    def set_directorypath(self, directorypath):
        directorypath = directorypath
        self.directorypath = directorypath

    def set_prefix(self, prefix):
        prefix = prefix
        self.prefix = prefix

    def get_FileIO(self):
        return self.iFileIO

    #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
    def __init__(self, global_index, global_list_keys, global_list_values, maxLoops, charlotte):
        self.iFileIO = FileIO()
        self.iDatabaseTools = DatabaseTools()
        self.charlotte = charlotte
        self.iWebTools = WebTools(self.charlotte)
        #self.a_nlp = spacy.load('en_core_web_sm') NOT COMPATIBLE WITH PYTHON 38
        #self.a_matcher = Matcher(self.a_nlp.vocab) NOT COMPATIBLE WITH PYTHON 38
        self.name = 'Alice'
        self.owner_name = str('Charlotte')
        self.history_name = str(str(self.owner_name) + "_" + str(self.name))
        self.history_period_name = 'init'
        self.directorypath = ( str( str(os.getcwd()) + '/DATABASE/history/' + self.owner_name + '/' + self.name + '/' ))
        if not os.path.exists(self.directorypath):
            os.makedirs(self.directorypath)

        self.global_list_keys = global_list_keys
        self.history_filepath = str( str( str(os.getcwd()) + '/DATABASE/history/' + self.owner_name + '/' + self.name + '/' ) + self.history_name + '.history')
        self.clock = self.start_clock()

        self.history_interval = self.clock.history_interval
        self.first_history_period = self.clock.first_history_period
        self.history_period = self.clock.history_period
        self.history_period_name = self.clock.history_period_name
        self.csvio = self.init_csv_io()

        #assign a csv file name to a path 
        self.dict_csv_filename_to_path = {}
        self.dict_csv_filepath_to_filename = {}
        self.n_dict_filename_filepath_list_fields = {}
        self.n_dict_filename_filepath_list_rows = {}
        #self.set_csv_filename_to_path(self.history_name, self.directorypath)
        #associate a field with a name
        self.dict_field_filename = {}
        #associate a phrase with a name
        self.dict_phrase_filename = {}
        #associate a value with a name
        self.dict_value_filename = {}
        #self.test_chronos_tables()

        ###
        self.list_memory = []
        self.node = self.i_node()
        self.map = {}
        self.map = self.i_map()
        self.web_nodes = {}
        self.filepath_nodes = {}
        self.client_report_nodes = {}
        self.dev_report_nodes = {}
        self.get_memory("MemoryFilepaths", maxLoops)
        self.terminal = self.createTerminal()
        #self.totalrecall = self.createMemory()
        self.memory_fp = ''
        self.memory_fp = self.load_previous_memories(maxLoops)
        self.defaultLoops = 10000000000
        self.MemoryFilePath = ''
        self.list_href_nav = []
        self.list_lang_nav = []
        self.list_key_nav = []
        self.visited_urls = []
        self.session_load_status = True
        self.url_queue = Queue()
        self.thread_count = 0
        self.url_branches_heap = []
        self.thread_instances = []
        self.thread_loops = 0


    def increment_thread_count(self):
        self.thread_count += 1
        eventlog('increment_thread_count: ' + str(self.thread_count))

    def decrement_thread_count(self):
        self.thread_count -= 1
        eventlog('decrement_thread_count: ' + str(self.thread_count))

    def get_thead_count(self):
        eventlog('get_thead_count: ' + str(self.thread_count))
        return self.thread_count

    def join_url_queue(self):
        self.url_queue.join()

    def put_url_queue(self, url):
        self.url_queue.put(url)

    def get_url_queue(self):
        return self.url_queue.get()

    def set_session_load_status(self, b_load_status):
        self.session_load_status = b_load_status

    def get_session_load_status(self):
        return self.session_load_status
    #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
    def init_csv_io(self):
        self.csvio = CSV_IO()
        return self.csvio

    #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
    def start_clock(self):
        self.clock  = Chronos(self.name, self.owner_name)
        return self.clock

    #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
    def i_node(self):
        self.node = Node(self.name)
        return self.node

    #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
    def i_map(self):
        self.map = {}
        newData = {self.name:self.node}
        return self.map.update(newData)

    #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
    def load_previous_memories(self, maxLoops):
        self.memory_fp = ''
        eventlog("load_previous_memories " + str(self.name) + " START ----------- ")
        if not os.path.exists( str( str(os.getcwd()) + '/DATABASE/Memory/')):
            os.makedirs( str( str(os.getcwd()) + '/DATABASE/Memory/'))

        
        self.memoryFilepaths = str( str(os.getcwd()) + '/DATABASE/Memory/' + '*.csv')
        self.memoryFiles = glob.glob(self.memoryFilepaths, recursive=True)
        self.memory = self.get_memory("MemoryFilepaths", maxLoops)
        self.b_foundMemoryFilepaths = False
        
        for filepath in self.memoryFiles:
            self.debuginfo("\n" + filepath)
            if filepath.find('MemoryFilepaths') != -1:
                eventlog("\nFound MemoryFilepaths file")
                ##sleep(0.25))
                try:
                    self.memory.lines = FileIO.get_list_from_file(self, filepath, maxLoops)
                    for line in self.memory.lines:
                        eventlog(str(line))
                    self.b_foundMemoryFilepaths = True
                except:
                    eventlog('WARNING -- self.memory.lines = FileIO.get_list_from_file(self, filepath, maxLoops) failed!')
                    #sleep(3)
            elif filepath.find('.csv') != -1:
                self.thename = os.path.basename(filepath)
                self.thename = FileIO.get_fp_without_suffix(self, self.thename)
                eventlog("Loading previous memories of memory name " + self.thename)
                ###sleep(0.25))
                self.get_memory(self.thename, maxLoops)
                self.memory_fp = filepath
                self.MemoryFilePath = filepath
                eventlog("Filepath: " + filepath)
                #sleep(3)
                self.lines = FileIO.get_list_from_file(self, filepath, maxLoops)
                if self.lines:
                    for i in range(0, len(self.list_memory)):
                        if self.list_memory[i].name == self.thename:
                            self.b_gotKeys = False
                            for line in self.lines:
                                self.list_memory[i].lines.append(str(line))
                                eventlog(str(self.list_memory[i].name))
                                ##sleep(0.25))
                                #if self.list_memory[i].index == 0:
                                if self.b_gotKeys == False:
                                    keys = line.split(", ")
                                    for key in keys:
                                        self.list_memory[i].keys.append(key)
                                        eventlog(str("Key: " + str(key)))
                                        ##sleep(0.25))
                                    self.b_gotKeys = True
                                else:
                                    self.list_memory[i].values.clear()
                                    values = line.split(", ")
                                    for value in values:
                                        self.list_memory[i].values.append(value)
                                        eventlog(str("Value: " + str(value)))
                                        ##sleep(0.25))
                                    eventlog("self.list_memory[i].index " + str(self.list_memory[i].index))
                                    ##sleep(0.25))
                                    eventlog("str(self.list_memory[i].keys) " + str(self.list_memory[i].keys))
                                    ##sleep(0.25))
                                    eventlog("str(self.list_memory[i].values) " + str(self.list_memory[i].values))
                                    ##sleep(0.25))
                                    eventlog("str(self.list_memory[i].lines[self.list_memory[i].index]) " + str(self.list_memory[i].lines[self.list_memory[i].index]))
                                    ##sleep(0.25))
                                    self.list_memory[i].record(self.list_memory[i].index,self.list_memory[i].keys, self.list_memory[i].values, maxLoops)
                                    self.list_memory[i].index += 1
                            self.list_memory[i].write(maxLoops)

        eventlog("\n load_previous_memories ----- " + str(self.name) + " END ----------- ")

        if self.b_foundMemoryFilepaths == False:
            eventlog("\n no memories have been saved")
            self.keys = ["name", "filepath"]
            f_path = str(self.memory.dp_root + self.memory.name + '.csv')
            self.values = [self.memory.name, f_path]
            self.index = 0
            self.memory.update(self.index, self.keys, self.values, maxLoops)

        for memory in self.list_memory:
            eventlog(memory.name)
            for line in memory.lines:
                eventlog(line)

        return self.memory_fp

    #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
    def get_global_list_keys(self):
        return self.global_list_keys

    #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
    def set_global_list_keys(self, list_keys):
        self.global_list_keys = list_keys

    #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
    def show_list_memory(self):
        for memory in self.list_memory:
            eventlog("show_list_memory: " + str(memory.name))
            eventlog("show_list_memory: " + str(memory))

    #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
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
                eventlog(str("\ndebuginfo|" + str(caller.lineno) + "|START|\n " + str(self.debugMessageList[i]) + "  " + str(caller.lineno) +" \n|END|"))
                ##self.f.write(str("\ndebuginfo|" + str(caller.lineno) + "|START|\n " + str(self.debugMessageList[i]) + "  " + str(caller.lineno) +" \n|END|"))
        else:
            eventlog(str("\ndebuginfo|" + str(caller.lineno) + "|START|\n " + str(self.debugMessageList[0])  + "  " + str(caller.lineno) +" \n|END|"))
            ##self.f.write(str("\ndebuginfo|" + str(caller.lineno) + "|START|\n " + str(self.debugMessageList[0])  + "  " + str(caller.lineno) +" \n|END|"))
        self.f.close()

    #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
    def get_memory(self, m_name, maxLoops):
        if self.list_memory:
            for i in range(0, len(self.list_memory)):
                if self.list_memory[i].name == m_name:
                    eventlog("found memory: " + str(self.list_memory[i]) + " get_memory will return " + str(m_name))
                    return self.list_memory[i]
        eventlog("Creating a memory named " + str(m_name))
        memory = self.createMemory(m_name)
        eventlog('CREATED MEMORY: ' + str(memory))
        #sleep(3)
        memory.name = m_name
        eventlog('CREATED MEMORY NAME: ' + str(memory.name))
        self.list_memory.append(memory)
        eventlog("memory named " + str(m_name))
        if self.list_memory:
            for i in range(0, len(self.list_memory)):
                if self.list_memory[i].name == m_name:
                    eventlog("found memory: " + str(self.list_memory[i]) + " get_memory will return " + str(m_name))
                    self.list_memory[i]
                    #node = self.list_memory[i]
                    #data = {m_name:node}
                    #self.map.update(data)
                    return self.list_memory[i]

    #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
    def createTerminal(self):
        return AliceInWonderland.Terminal(self)

    #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
    def createMemory(self, name):
        return AliceInWonderland.Memory(self, name, 999999)

    #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
    def set_nav_queue(self, list_href_nav, list_lang_nav, list_key_nav):
        self.list_href_nav = list_href_nav
        self.list_lang_nav = list_lang_nav
        self.list_key_nav = list_key_nav

    #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
    def get_nav_queue(self):
        return self.list_href_nav, self.list_lang_nav, self.list_key_nav

    def append_visited_url(self, url):
        self.visited_urls.append(url)

    def get_visited_urls(self):
        return self.visited_urls

    #classes start
    class Memory:
        history_name = 'Memory'
        directorypath = ( str( str(os.getcwd()) + '/DATABASE/history/' + history_name + '/'))
        if not os.path.exists( str( str(os.getcwd()) + '/DATABASE/history/' + history_name + '/')):
            os.makedirs( str( str(os.getcwd()) + '/DATABASE/history/' + history_name + '/'))
        history_filepath = str( str(os.getcwd()) + '/DATABASE/history/' + history_name + '.history')
        set_time = datetime.datetime.now()
        hour = str(set_time.strftime("%H"))
        minute = str(set_time.strftime("%M"))
        second = str(set_time.strftime("%S"))
        prefix = str('initialized-time-' + hour + minute + second)

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def __init__(self, memoryParent, name, maxLoops):
            self.csvio = self.init_csv_io()
            self.name = str(name)
            self.memoryParent = memoryParent
            self.owner_name = str(self.memoryParent.name)
            self.history_name = str(str(self.owner_name) + "_" + str(self.name))
            self.history_period_name = 'init'
            self.directorypath = ( str( str(os.getcwd()) + '/DATABASE/history/' + self.owner_name + '/' + self.name + '/' + self.history_period_name + '/'))
            if not os.path.exists(self.directorypath):
                os.makedirs(self.directorypath)


            self.history_filepath = str( str( str(os.getcwd()) + '/DATABASE/history/' + self.owner_name + '/' + self.name + '/' ) + self.history_name + '.history')
            self.clock = self.start_clock()

            self.history_interval = self.clock.history_interval
            self.first_history_period = self.clock.first_history_period
            self.history_period = self.clock.history_period
            self.history_period_name = self.clock.history_period_name
            self.csvio = self.init_csv_io()

            #assign a csv file name to a path 
            self.dict_csv_filename_to_path = {}
            self.dict_csv_filepath_to_filename = {}
            self.n_dict_filename_filepath_list_fields = {}
            self.n_dict_filename_filepath_list_rows = {}
            #self.set_csv_filename_to_path(self.history_name, self.directorypath)
            #associate a field with a name
            self.dict_field_filename = {}
            #associate a phrase with a name
            self.dict_phrase_filename = {}
            #associate a value with a name
            self.dict_value_filename = {}
            #self.test_chronos_tables()
            self.node = self.i_node()
            self.map =self.i_map()
            self.node_path = ''
            self.defaultPath = str(str(os.getcwd()) + '/DATABASE/Memory/')
            self.node_path = self.defaultPath
            self.dp_root = self.node_path
            ##########################
            self.dict_records = {}
            self.keys = []
            self.values = []
            self.index = 0
            self.lines = []
            self.keyValsDict = collections.OrderedDict()
            self.sortedList = []
            self.cols = []
            self.branches = {}
            self.n_columns = {}
            self.n_rows = {}
            self.n_row_index = {}
            self.n_col_index = {}
            self.memoryfilepath = ''
            self.dev_index = 0
            self.dev_rows = {}
            self.dev_report = {}
            self.time_matrix = {}
            self.time_index = 0
            self.named_matricies = {}
            self.memory_row_records = {}
            self.memory_column_records = {}
            self.memory_field_names = []
            self.memory_field_name_init_times = {}
            self.memory_names = []
            self.memory_name_init_times = {}
            self.memory_name_row_col_index_positions = {}
            self.rows = {}
            self.row_index = 0
            self.col_index = 0
            #https://www.programcreek.com/python/example/5193/collections.Mapping


        def init_csv_io(self):
            self.csvio = CSV_IO()
            return self.csvio

        def start_clock(self):
            self.clock  = Chronos(self.name, self.owner_name)
            return self.clock

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def i_node(self):
            self.node = Node(self.name)
            return self.node

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def i_map(self):
            self.map = {}
            newData = {self.name:self.node}
            self.map.update(newData)
            return self.map

        
        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def branch(self, name):
            newBranch = self.memoryParent.get_memory(name, self.memoryParent.maxLoops)
            newBranch.set_node_parent(self.node)
            newBranch.set_root_node(self.node.root)
            self.branches.update(dict(name,newBranch))
            return newBranch

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def n_get_this(self):
            return self.node

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def n_get_fp(self):
            return self.memoryParent.filepath_nodes

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def n_get_web(self, ):
            return self.memoryParent.web_nodes

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def n_get_client_report(self):
            return self.memoryParent.client_report_nodes

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def n_get_dev_report(self):
            return self.memoryParent.dev_report_nodes

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def apply_node_path(self):
            nodePath = self.node.path
            eventlog(str(nodePath))
            self.node_path = nodePath
            self.dp_root = nodePath
            eventlog(str(self.node_path))
            eventlog(str(self.dp_root))
            os.makedirs( str( str(os.getcwd()) + self.node_path))

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def dev_record(self, name, data , b_write):
            self.found = False
            for key, value in self.dev_rows.items():
                if key == name:
                    self.found = True
            if self.found == False:
                for i in range(0, self.dev_index):
                    self.dev_rows.update(i,dict(name,data))
                    for key, value in self.dev_rows.items():
                        self.dev_report.update(dict(key,dict(key,value)))
                        eventlog("dev_report row: " + str(i) + " Key " + str(key)  + " value " + str(value) )

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def set_node_parent(self, theParent):
            self.node.parent = theParent.node

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def get_node(self):
            return self.node

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def get_path(self):
            return self.node.path

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def get_children(self):
            return self.node.children

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def get_ancestors(self):
            return self.node.ancestors

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def get_root(self):
            return self.node.root

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def get_depth(self):
            return self.node.depth

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def get_descendants(self):
            return self.node.descendants

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def get_siblings(self):
            return self.node.siblings

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def get_leaves(self):
            return self.node.leaves

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def get_height(self):
            return self.node.height

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def sortFieldValue(self, sortField, sortBasedOnField, Decending):
            self.sortField = sortField
            self.sortedBasedOnField = sortBasedOnField
            self.DecendingOrder = Decending
            self.sortedKeys = []
            self.sortedVals = []
            for key, value in self.dict_records.items():
                self.recordString = str(key)
                for key, value in value.items():
                    if key == self.sortField:
                        self.sortedKeys.append(key)
                        eventlog("sorting Key : " + str(key) )
                    if value == self.sortedBasedOnField:
                        self.sortedVals.append(value)
                        eventlog("sorting Value : " + str(value) )
            sortThisDict = dict(zip(self.sortedKeys,self.sortedVals))
            l=list(sortThisDict.items())
            l.sort(reverse=self.DecendingOrder)
            self.sortedList = l
            for item in self.sortedList:
                eventlog("sorted: " + str(item))
            return self.sortedList

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def debuginfo(self, message):
            eventlog("\n ----------- " + str(self.name) + " START debuginfo ----------- ")
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
                    eventlog(str("\n Memory|" + str(self.name) + "|debuginfo|" + str(caller.lineno) + "|START|\n " + str(self.debugMessageList[i]) + "  " + str(caller.lineno) +" \n|END|"))
                    #self.f.write(str("\n Memory|" + str(self.name) + "|debuginfo|" + str(caller.lineno) + "|START|\n " + str(self.debugMessageList[i]) + "  " + str(caller.lineno) +" \n|END|"))
            else:
                eventlog(str("\n Memory|debuginfo|" + str(self.name) + "|debuginfo|" + str(caller.lineno) + "|START|\n " + str(self.debugMessageList[0])  + "  " + str(caller.lineno) +" \n|END|"))
                #self.f.write(str("\n Memory|debuginfo|" + str(self.name) + "|debuginfo|" + str(caller.lineno) + "|START|\n " + str(self.debugMessageList[0])  + "  " + str(caller.lineno) +" \n|END|"))
            eventlog("\n ----------- " + str(self.name) + " END debuginfo ----------- ")
            self.f.close()

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def get_parent(self):
            return self.name, str(' is a child of ') , self.memoryParent.name

        '''
        #@pysnooper.snoop('nodes.history', prefix='smart_update', depth=10)
        def smart_update(self, memory_name, field_name, field_value, write):
            self.filepath = str(str(self.dp_root) + str(self.name) + ".csv")
            #self.my_matrix = self.time_matrix.copy()
            #self.my_items = None
            #for key, value in self.my_matrix.items():
                #if key == memory_name:
                    #self.my_items = v
                    # install https://github.com/lark-parser/lark
                    # install https://anytree.readthedocs.io/en/2.6.0/
                    # https://github.com/c0fec0de/anytree
            self.my_items = self.time_matrix.items()
            self.my_fields = self.my_matrix.values()
            self.m_matrix = {}
            self.m_columns = {}
            self.m_rows = {}
            self.m_col_index
            self.m_row_index
            for key, value in self.time_matrix.items():
                eventlog("key " + str(key) + " from: " + str(value.items()) + ".\n" )
                if key == self.time_index:
                    self.m_index = key

                for key, value in value.items():
                    eventlog("key " + str(key) + " from: " + str(value.items()) + ".\n" )
                    if key == memory_name:
                            self.b_m_name = True
            if b_m_time_index == False:
                self.time_matrix.update(dict(self.time_index,self.matricies))

            if self.b_m_name == False:
                for key, value in self.time_matrix.items():
                    eventlog("key " + str(key) + " from: " + str(value.items()) + ".\n" )
                    if key == self.time_index:
                        for key, value in value.items():
                            eventlog("key " + str(key) + " from: " + str(value.items()) + ".\n" )
                            if key == memory_name:
                                self.b_m_name = True
                    column = self.memory_column_records
                    row = dict(self.my_row_index, self.memory_row_records)
                    column = dict(self.my_col_index, self.memory_field_names)
                    memory = dict(memory_name,self.memory_names)
                    self.named_matricies = 
            self.b_memory_name = False
            for memory_index in range(0, len(self.memory_names)):
                eventlog("memory_index " + str(memory_index) + " name is: " + self.memory_names[memory_index] + ".\n" )
                if self.memory_names[memory_index] == memory_name:
                    self.b_memory_name = True
                    if self.memory_names[memory_index] == memory_name:
                        for key, value in self.memory_name_row_col_index_positions.items():
                            if key == memory_name:
                                #the lowest time_matrix number that this memory can go back to.
                                for key, value in value.items():
                                    self.my_row_index = key
                                    self.my_col_index = value
                                self.name_exists = True
            if self.b_memory_name == False:
                my_row_index = 0
                my_col_index = 0
                self.memory_names.append(dict(memory_name, self.memory_name_row_col_index_positions))



            if self.name_exists == True:
                self.found_field_name = False
                for field_index in range(0, len(self.memory_field_names)):
                    if self.memory_field_names[field_index] == field_name:
                        self.found_field_name = True
                if self.found_field_name == False:
                    self.memory_field_names.append(field_name)
                    self.found_field_records = False
                    for key, value in self.memory_column_records.items():
                        if key == field_name:
                            self.found_field_records = True
                        for key, value in value.items():
                            if key == memory_name:
                                self.found_memory_name = True
                                value[self.my_row_index] = field_value
                        if self.found_memory_name == False:
                            mem = dict(self.my_row_index, field_value)
                            rec = memory_name
                            self.memory_column_records.update(dict(rec, mem))

            #matrix_index
                #matrix_resolution_index
                    #resolution_name
                        #row index (0 to N from top to bottom past to present)
                            #col index (0 to N how far left or right primary resolution to peripheral)

                                #fieldname and value

            #self.smart_memory_rows.update(row)

            keyVal = {}
            keyVal[field_name] = field_value
            columns = {self.col_index:keyVal} #fieldname and value at column number
            rows = {self.row_index:columns} #row index containing columns

            memory_state = {memory_name:field_name}
            self.memory_names.update(memory_state)
            
            self.matrix_dimensions.update(self.matrix_time)
            

                

            self.memory_matrix.update(simulation)
            #given the time something changed
            for key, value in self.matrix_time:
                
                #time index is key

                for key, value in self.matrix_resolution:
                    #matrix resolution is key
                    
                    for key, value in self.resolution_names:
                        #resolution name is key

                        if memory_name == key:
                            for key, value in self.columns.items():
                                #row number

                                self.smart_memory_row = str(key)
                                eventlog(str(self.smart_memory_row) + " smart_memory_row ")
                                self.lineKeys = ''
                                self.lineValues = ''
                                self.resolution_
                                self.col_index = 0
                                for key, value in self.cols_and_vals.items():
                                    #column number
                                    self.theKeys += str(str(key) + ", ")
                                    self.theValues += str(str(value) + ", ")
                                    self.col_index += 1
                                    #column
                                self.lineKeys = self.lineKeys[:-2]
                                self.lineValues = self.lineValues[:-2]
                                eventlog(str(" \n\n " +  str(self.name) + "\n smart_memory " + self.recordString + " Keys " + self.theKeys))

                                eventlog(str(" smart_memory " + self.recordString + " Vals " + self.theValues + " \n\n "))
                                if write == True:
                                    if self.recordNumber == 0:
                                        write_line(self, self.filepath, self.theKeys, 'a+')
                                    write_line(self, self.filepath, self.theValues, 'a+')
                                    self.recordNumber += 1
                            sleep(5)
            self.time_index += 1
        '''


        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def update(self, i, keys, values, maxLoops):
            eventlog("\n --index " + str(i) + " ----- " + str(self.name) + " START update ----------- ")
            self.filepath = str(str(self.dp_root) + str(self.name) + ".csv")
            newData = dict(zip(keys,values))
            self.keyValsDict.update(newData)
            self.allKeys = []
            for key, value in self.keyValsDict.items():
                eventlog("keyValsDict Keys " + str(key) )
                self.allKeys.append(str(key))
            self.allValues = []

            for allKeysIndex in range(0, len(self.allKeys)):
                try:
                    eventlog("allValues " + str(allKeysIndex) + " " + str(values[allKeysIndex]))
                    self.allValues.append(values[allKeysIndex])
                except:
                    eventlog("allValues " + str(allKeysIndex) + " " + "None")
                    self.allValues.append("None")
            #mem = self.keyValsDict
            mem  =  dict(zip(self.allKeys,self.allValues))
            rec = {i:mem}
            self.dict_records.update(rec)
            FileIO.clear_file(self, self.filepath)
            eventlog("\n ---index " + str(i) + " memory status: ")
            self.recordNumber = 0
            for key, value in self.dict_records.items():
                self.recordString = str(key)
                self.theKeys = ''
                self.theValues = ''
                for key, value in value.items():
                    self.theKeys += str(str(key) + ", ")
                    self.theValues += str(str(value) + ", ")
                self.theKeys = self.theKeys[:-2]
                self.theValues = self.theValues[:-2]
                eventlog(str("dict_record " + self.recordString + " Keys " + self.theKeys))
                eventlog(str("dict_record " + self.recordString + " Vals " + self.theValues))

                if self.recordNumber == 0:
                    FileIO.write_line(self, self.filepath, self.theKeys, 'a+')
                FileIO.write_line(self, self.filepath, self.theValues, 'a+')
                self.recordNumber += 1
            self.lines = FileIO.get_list_from_file(self, self.filepath, maxLoops)
            for index in range(0, len(self.lines)):
                eventlog("lines row: " + str(index) + " line: " + str(self.lines[index]))
            self.values.clear()
            eventlog("\n --index " + str(i) + " ----- " + str(self.name) + " END update ----------- ")

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def record(self, i, keys, values, maxLoops):
            eventlog("\n --index " + str(i) + " ----- " + str(self.name) + " START record ----------- ")
            self.filepath = str(str(self.dp_root) + str(self.name) + ".csv")
            mem  =  dict(zip(keys,values))
            rec = {i:mem}
            self.dict_records.update(rec)
            FileIO.clear_file(self, self.filepath)
            self.values.clear()
            eventlog("\n --index " + str(i) + " ----- " + str(self.name) + " END record ----------- ")

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def write(self, maxLoops):
            self.filepath = str(str(self.dp_root) + str(self.name) + ".csv")

            FileIO.clear_file(self, self.filepath)
            self.recordNumber = 0
            for key, value in self.dict_records.items():
                self.recordString = str(key)
                self.theKeys = ''
                self.theValues = ''
                for key, value in value.items():
                    self.theKeys += str(str(key) + ", ")
                    self.theValues += str(str(value) + ", ")
                self.theKeys = self.theKeys[:-2]
                self.theValues = self.theValues[:-2]
                eventlog(str("write " + self.recordString + " Keys " + self.theKeys))
                eventlog(str("write " + self.recordString + " Vals " + self.theValues))

                if self.recordNumber == 0:
                    FileIO.write_line(self, self.filepath, self.theKeys, 'a+')
                FileIO.write_line(self, self.filepath, self.theValues, 'a+')
                self.recordNumber += 1
            self.lines = FileIO.get_list_from_file(self, self.filepath, maxLoops)
            for index in range(0, len(self.lines)):
                eventlog("lines row: " + str(index) + " line: " + str(self.lines[index]))
            self.values.clear()

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def get_list_field(self, theField):
            eventlog("\n --field " + str(theField) + " ----- " + str(self.name) + " START get_list_field ----------- ")
            self.list_column = []
            for key, value in self.dict_records.items():
                self.recordString = str(key)
                self.theKeys = ''
                self.theValues = ''
                for key, value in value.items():
                    if key == theField:
                        self.list_column.append(value)
                        eventlog(str(key) + " is " + str(value))
                    #self.theKeys += str(str(key) + ", ")
                    #self.theValues += str(str(value) + ", ")
                #self.theKeys = self.theKeys[:-2]
                #self.theValues = self.theValues[:-2]
                #eventlog(str("dict_record " + self.recordString + " Keys " + self.theKeys))
                #eventlog(str("dict_record " + self.recordString + " Vals " + self.theValues))
            return self.list_column
            eventlog("\n --field " + str(theField) + " ----- " + str(self.name) + " END get_list_field ----------- ")

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def get_lines(self):
            return self.lines

        #@pysnooper.snoop(history_filepath, prefix=str(prefix), depth=1)
        def render_lines(self):
            eventlog("\n ----------- " + str(self.name) + " START update ----------- ")
            for i in range (0, len(self.lines)):
                eventlog("Line " + str(i) + " is: " + str(self.lines[i]))
            eventlog("\n ----------- " + str(self.name) + " END update ----------- ")
            return self.lines

    class Terminal:
        #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/Terminal.history', prefix='Memory', depth=1)
        def __init__(self, terminalParent):
            self.name = 'initConsole'
            self.terminalParent = terminalParent
            self.run_test()

        #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/Terminal.history', prefix='Memory', depth=1)
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
                    eventlog(str("\n Terminal|debuginfo|" + str(caller.lineno) + "|START|\n " + str(self.debugMessageList[i]) + " " + str(caller.lineno) + "|" + "\n|END|"))
                    #self.f.write(str("\n Terminal|debuginfo|" + str(caller.lineno) + "|START|\n " + str(self.debugMessageList[i]) + "  " + str(caller.lineno) +" \n|END|"))
            else:
                eventlog(str("\n Terminal|debuginfo|" + str(caller.lineno) + "|START|\n " + str(self.debugMessageList[0])  + "  " + str(caller.lineno) +" \n|END|"))
                #self.f.write(str("\n Terminal|debuginfo|" + str(caller.lineno) + "|START|\n " + str(self.debugMessageList[0])  + "  " + str(caller.lineno) +" \n|END|"))

            self.f.close()

        #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/Terminal.history', prefix='Memory', depth=1)
        def tRight(self, string):
            s0 = str('{:.200}'.format(str(string)))
            #now pad 10 chars on each side
            s1 = str('{:>10}'.format(s0))
            return s1

        #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/Terminal.history', prefix='Memory', depth=1)
        def tLeft(self, string):
            #first 10 chars only
            s0 = str('{:.200}'.format(str(string)))
            #now pad 10 chars on each side
            s1 = str('{:<10}'.format(s0))
            return s1

        #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/Terminal.history', prefix='Memory', depth=1)
        def tCenter(self, string):
            #first 10 chars only
            s0 = str('{:.200}'.format(str(string)))
            #now pad 10 chars on each side
            s1 = str('{:^10}'.format(s0))
            return s1

        #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/Terminal.history', prefix='Memory', depth=1)
        def displayThree(self, left, center, right):
            string = str(self.tLeft(left) + " " + self.tCenter(center) + " " + self.tLeft(right))
            eventlog(string)
            #self.debuginfo(string)
            return string

        #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/Terminal.history', prefix='Memory', depth=1)
        def run_test(self):
            result = self.displayThree( "Left", "Center", "Right")
            eventlog(result)
            #sleep(1)
            result = self.displayThree("1", "2", "3")
            eventlog(result)
            #sleep(1)
            self.left = str(str('test_column_name'))
            self.center = str('test_Total: ' + str('1') + '/' + str('10'))
            self.right = str('Task: ' + str('1') + '/' + str('50'))
            terminal_string = self.displayThree(self.left, self.center, self.right)
            eventlog(terminal_string)
            #sleep(3)

        #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/Terminal.history', prefix='Memory', depth=1)
        def render_parent_globals(self):
            for i in range(0, self.terminalParent.global_index):
                self.displayThree(self.terminalParent.global_index[i],self.terminalParent.global_list_keys[i], self.terminalParent.global_list_values[i])

        #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/Terminal.history', prefix='Memory', depth=1)
        def get_parent(self):
            return self.name, str(' is a child of  ') , self.terminalParent.name
    #classes end


