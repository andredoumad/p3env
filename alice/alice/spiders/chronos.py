from .AliceRequiredModules import *
from .csv_io import CSV_IO
from .standalone_tools import *


class Chronos:
    history_name = 'Chronos'
    history_period = datetime.datetime.now()
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
    def __init__(self, owner_name, name):
        self.name = str(name)
        self.owner_name = str(owner_name)
        self.history_name = str(str(owner_name) + "_" + str(name))
        self.history_period_name = 'init'
        self.directorypath = ( str( str(os.getcwd()) + '/DATABASE/history/' + self.owner_name + '/' + self.name + '/' + self.history_period_name + '/'))
        if not os.path.exists(self.directorypath):
            os.makedirs(self.directorypath)
        self.history_filepath = str(self.directorypath + '/' + self.history_name + '.history')
        self.history_interval = self.set_history_interval(3)
        self.first_history_period = datetime.datetime.now()
        self.history_period = self.first_history_period
        self.history_period_name = self.get_history_period_name()
        self.csvio = self.init_csv_io()
        self.cTime = datetime.datetime.now()


        #assign a csv file name to a path 
        self.dict_csv_filename_to_path = {}
        self.dict_csv_filepath_to_filename = {}
        self.n_dict_filename_filepath_list_fields = {}
        self.n_dict_filename_filepath_list_rows = {}
        self.set_csv_filename_to_path(self.history_name, self.directorypath)
        #associate a field with a name
        self.dict_field_filename = {}
        #associate a phrase with a name
        self.dict_phrase_filename = {}
        #associate a value with a name
        self.dict_value_filename = {}
        #self.test_chronos_tables()


    def init_csv_io(self):
        self.csvio = CSV_IO()
        return self.csvio
 
    def test_populate_chronos_tables(self):
        self.set_csv_filename_to_path('andre', self.directorypath)
        self.associate_field_with_filename('date', 'andre')
        self.associate_field_with_filename('message', 'andre')
        self.associate_field_with_filename('priority', 'andre')
        self.associate_phrase_with_filename('builds awesome', 'andre')
        self.associate_phrase_with_filename('artificial intelligence', 'andre')
        self.associate_phrase_with_filename('every waking moment', 'andre')
        self.associate_value_with_filename('something', 'andre')
        self.associate_value_with_filename('alice', 'andre')
        self.associate_value_with_filename('found', 'andre')
        
        
        
    #def get_dict_created in the last few mins_(self):
        #for key, value in self.dict_filename_paths_
        
        
        
    #def get_dicts_created in the last few mins_(self):
        #for key, value in self.dict_filename_paths_
        
        
        

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/set_csv_filename_to_path.history', prefix='set_csv_filename_to_path', depth=1)
    def set_csv_filename_to_path(self, ifilename, ifilepath):
        self.lp = self.get_history_period_name()
        self.dp = str(str(ifilepath) + str(ifilename)+ '/')
        if not os.path.exists( str(self.dp)):
            os.makedirs( str(self.dp) )
        self.fp = str(str(self.dp) + str(ifilename) + '_' + self.lp +'.csv')
        self.dict_csv_filepath_to_filename.update()
        self.b_ifilename = False
        if os.path.isfile(self.fp):
            for filename in os.listdir(self.dp):
                #os.rename(old_file_name, new_file_name)
                if filename.find(str(self.get_history_period())) != -1:
                    eventlog("found history_period_group_path_csv file ")
                    if filename.find(str(ifilename)) != -1:
                        #self.list_csv_filepath_fields =
                        eventlog("found ifilename: " + str(ifilename))
                        self.b_ifilename = True
        if self.b_ifilename == False:
            eventlog("did not find ifilename: " + str(ifilename))
        else:
            self.dict_csv_filename_to_path.update(str(filename), path)
            self.csvio.new_chronos_file(
                str(ifilename), str(self.fp),
        self.dict_csv_filename_to_path,
        self.dict_csv_filepath_to_filename,
        self.n_dict_filename_filepath_list_fields,
        self.n_dict_filename_filepath_list_rows,
        self.dict_field_filename,
        self.dict_phrase_filename,
        self.dict_value_filename
                 )
        return self.dict_csv_filename_to_path

    def associate_field_with_filename(self, field, filename):
        self.dict_field_filename.update(field, filename)
        return self.dict_field_filename

    def associate_phrase_with_filename(self, phrase, filename):
        self.dict_phrase_filename.update(phrase, filename)
        return self.dict_phrase_filename

    def associate_value_with_filename(self, value, filename):
        self.dict_value_filename.update(value, filename)
        return self.dict_value_filename


    def harvest(self):
        for key, value in self.dict_csv_filename_to_path.items():
            self.csv_filepath = str(value)
            self.csv_name = str(key)
            #FileIO.write_key_value_file(csv_filepath, self.dict_csv_filename_to_path)
            #FileIO.write_key_value_file(self, self.dict_csv_filename_to_path)

    def set_history_interval(self, history_interval):
        self.history_interval = int(history_interval)
        return self.history_interval

    def set_history_period(self):
        self.history_period = datetime.datetime.now()
        return self.history_period
    
    def previous_history_time(self):
        if not self.history_period:
            self.set_history_period()
        return self.history_period
    def get_interval(self):
        return self.history_interval
    
    def get_history_period(self):
        data2 = datetime.datetime.now()
        old = self.previous_history_time()
        diff = data2 -old 
        days, seconds = diff.days, diff.seconds
        hours = days * 24 + seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        if minutes > self.get_interval():
            self.set_history_period()
            return self.previous_history_time()
        else:
            self.set_history_period()
            self.get_history_period_name()
            return self.previous_history_time()

    def get_history_period_name(self):
        self.history_period = self.previous_history_time()
        self.history_period_name = str(str(self.history_name) + str(self.history_period))
        return self.history_period_name

    def getHourlyFileName(self, subdirectory, filename):
        global _Fps, _Tbs
        isNew = False
        mcwd = os.getcwd()
        # datetime object containing current date and time
        set_time = datetime.datetime.now()
        year = int(set_time.strftime("%Y"))
        month = int(set_time.strftime("%m"))
        day = int(set_time.strftime("%d"))
        hour = int(set_time.strftime("%H"))
        minute = int(set_time.strftime("%M"))
        second = int(set_time.strftime("%S"))
        microsecond = int(set_time.strftime("%f"))
        tTime = '{:%Y-%m-%d-%H}'.format(datetime(year, month, day, hour))
        _Fps = "/"
        myFilePath = str(str(mcwd) + _Fps + str(subdirectory) + _Fps + str(tTime) + _Fps + str(filename))
        if os.path.isfile(myFilePath):
            isNew  = True
        if not os.path.exists(mcwd + _Fps + subdirectory + _Fps + tTime):
            os.makedirs( str(mcwd + _Fps + subdirectory + _Fps + tTime))
            isNew  = True
        return str(os.getcwd() + _Fps + subdirectory + _Fps + tTime + _Fps + filename), isNew

    def getProperTime(self):
        # datetime object containing current date and time
        set_time = datetime.datetime.now()
        year = int(set_time.strftime("%Y"))
        month = int(set_time.strftime("%m"))
        day = int(set_time.strftime("%d"))
        hour = int(set_time.strftime("%H"))
        minute = int(set_time.strftime("%M"))
        second = int(set_time.strftime("%S"))
        microsecond = int(set_time.strftime("%f"))
        tTime = str(str(year) + "-" + str(month) + "-" + str(day) + "-" + str(hour) + "-" + str(minute) + "-" + str(second) + "-" + str(microsecond))
        historyTime = year+month+day+hour+minute+second+microsecond
        #self.debuginfo(tTime)
        return str(tTime), historyTime

    def getDayMonthHourString(self):
        # datetime object containing current date and time
        set_time = datetime.datetime.now()
        year = int(set_time.strftime("%Y"))
        month = int(set_time.strftime("%m"))
        day = int(set_time.strftime("%d"))
        hour = int(set_time.strftime("%H"))
        minute = int(set_time.strftime("%M"))
        second = int(set_time.strftime("%S"))
        microsecond = int(set_time.strftime("%f"))
        tTime = '{:%Y-%m-%d-%H}'.format(datetime(year, month, day, hour))
        return str(tTime)

    def getMinSecMicroString(self):
        # datetime object containing current date and time
        set_time = datetime.datetime.now()
        year = int(set_time.strftime("%Y"))
        month = int(set_time.strftime("%m"))
        day = int(set_time.strftime("%d"))
        hour = int(set_time.strftime("%H"))
        minute = int(set_time.strftime("%M"))
        second = int(set_time.strftime("%S"))
        microsecond = int(set_time.strftime("%f"))
        tTime = str(str(minute) + str(second) + str(microsecond))
        return str(tTime)

