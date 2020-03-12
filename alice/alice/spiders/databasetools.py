from AliceRequiredModules import *
# from .AliceRequiredModules import *


class DatabaseTools:

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='getCombinedLists', depth=1)
    def getCombinedLists(self, listA, listB, maxLoops):
        combinedList = []

        self.loops = 0
        self.working = True
        self.max = maxLoops + 500
        while self.working == True:

            for item in listA:
                self.loops +=1
                if self.loops > self.max:
                    self.working = False
                    break
                ##self.debuginfo("loop " + str(loops))
                combinedList.append(item)
            self.working = False

        self.working = True
        while self.working == True:

            self.loops = 0
            for item in listB:
                self.loops +=1
                if self.loops > self.max:
                    self.working = False
                    break
                ##self.debuginfo("loop " + str(loops))
                combinedList.append(item)
            self.working = False

        cleanCombinedList = self.getListWithoutDuplicates(combinedList)
        return cleanCombinedList

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='getListWithoutDuplicates', depth=1)
    def getListWithoutDuplicates(self, theList):
        from collections import OrderedDict
        return list(dict.fromkeys(theList))

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/make_job_paths.history', prefix='make_job_paths', depth=1)
    def make_job_paths(self, name):
        path = str(os.getcwd() + '/DATABASE/JOBS/' + str(name) + '/')
        if not os.path.exists( path ):
            #shutil.rmtree( str(os.getcwd() + '/DATABASE/JOBS/' + str(job_name)))
            os.makedirs( path)
        return path

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/make_job_paths.history', prefix='make_job_paths', depth=1)
    def get_job_paths(self, name):
        path = str(os.getcwd() + '/DATABASE/JOBS/' + str(name) + '/')
        if not os.path.exists( path ):
            #shutil.rmtree( str(os.getcwd() + '/DATABASE/JOBS/' + str(job_name)))
            os.makedirs( path)
            return path, False
        else:
            return path, True


    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='testNestedDictForKeyValue', depth=1)
    def testNestedDictForKeyValue(self, nestedDict, testKey, testValue):
        try:
            next(item for item in nestedDict if item[testKey] == testValue)
            #self.debuginfo(" Value Found: " + str(testValue) + " from Field " + str(testKey))
            return True
        except:
            # nested dict for key value failed.
            print(" nested dict for key value failed.")
            return False

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='find_between', depth=1)
    def find_between(self, s, first, last ):
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return ''

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/ordered.history', prefix='ordered', depth=1)
    def ordered(self, orderme):
        """Converts the provided dictionary into a collections.OrderedDict.
        The items in the returned OrderedDict will be inserted based on the
        natural sort order of the keys. Nested dictionaries will also be sorted
        in order to ensure fully predictable ordering.
        :param orderme: the dict to order
        :return: collections.OrderedDict
        :raises: ValueError: if `orderme` isn't a dict instance.
        """
        if not isinstance(orderme, dict):
            raise ValueError('argument must be a dict type')
        result = OrderedDict()
        for k, v in sorted(six.iteritems(orderme), key=lambda x: x[0]):
            if isinstance(v, dict):
                result[k] = self.ordered(v)
            else:
                result[k] = v
        return result

    # ==========================================================================================================================
    # ==========================================================================================================================

    def clear_screen(self):
        pass
        '''
        """
        Clears the terminal screen.
        """

        # Clear command as function of OS
        command = "cls" if platform.system().lower()=="windows" else "clear"

        # Action
        return subprocess.call(command) == 0
        '''

    def return_deduplicated_list_file_A_given_file_B(self, file_A, file_B):
        def get_list_from_file(filepath):
            listFromFile = []
            listFromFile.clear()
            working = True
            fh = open(str(filepath))
            while working == True:
                for line in fh:
                    print('INPUT: ' + str(line.rstrip()))
                    listFromFile.append(line.rstrip())
                working = False
            fh.close()
            return listFromFile

        list_file_A = get_list_from_file(str(file_A))
        list_file_B = get_list_from_file(str(file_B))
        list_dedup = []

        for file_A_item in list_file_A:
            searching = True
            found = False
            while searching == True:
                for file_B_item in list_file_B:
                    if len(file_A_item) == len(file_B_item):
                        if file_A_item == file_B_item:
                            print('DUPLICATE: ' + str(file_B_item))
                            found = True
                            searching = False
                
                searching = False

            if found != True:
                list_dedup.append(file_A_item)
                print('UNIQUE: ' + str(file_A_item))
        return list_dedup

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/examine_database.history', prefix='examine_database', depth=1)
    def examine_database(self, path, _Alice):
        #self.clear_screen()
        print('def examine_database')
        self.b_examining_database = False
        self.b_dp, self.b_fp, self.list_dp, self.list_fp = _Alice.iFileIO.get_list_files_folders_in_path( str(path))
        self.list_of_directory_paths.append(str(path))
        self.list_of_directory_paths = DatabaseTools.getListWithoutDuplicates(self, self.list_of_directory_paths)
        self.list_of_visited_directory_paths.append(str(path))
        self.list_paths.append(str(path))
        self.b_current_directory_contains_navigation_matrix = False
        self.b_current_directory_contains_web_matrix = False

        if self.b_fp == True:
            for i in range(0, len(self.list_fp)):
                #print('|examine_database| self.b_fp file_nav found: ' + str(i) + ' ' + str(self.list_fp[i]))
                self.list_of_file_paths.append(str(self.list_fp[i]))
                if self.list_fp[i].find('_+|file_nav|+_') != -1:
                    self.list_of_file_nav.append(self.list_fp[i])
                    #print('|examine_database| self.b_fp found navigation matrix: ' + str(self.list_fp[i]))
                elif self.list_fp[i].find('_matrix.csv') != -1:
                    self.list_of_web_matrix_files.append(self.list_fp[i])
                    for matrix_file in self.list_of_web_matrix_files:
                        pass
                        #print('|examine_database| self.b_fp for matrix_file in self.list_of_web_matrix_files: ' + str(matrix_file))
                        #sleep(0.5)
                    #print('|examine_database| self.b_fp found web matrix: ' + str(self.list_fp[i]))
                #sleep(0.5)
            #write lists to nav file
            self.list_of_file_paths = DatabaseTools.getListWithoutDuplicates(self, self.list_of_file_paths)
            with open(str(path + '_+|file_nav|+_.csv'), 'w+') as f:
                #f = open(str(path + '_+|file_nav|+_.csv'), 'w+')
                for item in self.list_of_file_paths:
                    #print('|examine_database| for item in self.list_of_file_paths: ' + str(item))
                    f.write(str(item))
                    f.write('\n')
                    #sleep(0.003)
                f.close()

            #write nav_matrix file
            self.b_found_website_matrix_files = False
            for i in range(0, len(self.list_of_web_matrix_files)):
                if self.list_of_web_matrix_files[i].find('0_matrix.csv') != -1:
                    self.b_found_website_matrix_files = True

            if self.b_found_website_matrix_files == True:
                #f = open(str(path + '_+|matrix_nav|+_.csv'), 'w+')
                self.list_sorted_matrix_files = []
                self.b_sorting_matrix = True
                self.target_index = 0
                '''
                while self.b_sorting_matrix == True:
                    for i in range(0, len(self.list_of_web_matrix_files)):
                        print('|examine_database| length list_of_web_matrix_files: ' + str(len(self.list_of_web_matrix_files)) )
                        print('|examine_database| length list_sorted_matrix_files: ' + str(len(self.list_sorted_matrix_files)) )
                        self.current_matrix_filepath = str(self.list_of_web_matrix_files[i].strip())
                        print('|examine_database| current_matrix_filepath: ' + str(self.current_matrix_filepath))
                        self.current_target_string = str('_' + str(self.target_index) + '_matrix.csv')
                        print('|examine_database| current target is: ' + str(self.current_target_string))
                        print('|examine_database| comparing ' + self.current_matrix_filepath + ' with ' + self.current_target_string)
                        if self.current_matrix_filepath.find(self.current_target_string) != -1:
                            print(self.current_matrix_filepath + ' DOES CONTAIN ' + self.current_target_string)
                            #sleep(0.003)
                            self.list_sorted_matrix_files.append(str(self.current_matrix_filepath))
                            self.target_index += 1
                            #sleep(0.003)
                            for ib in range(0, len(self.list_sorted_matrix_files)):
                                print('|examine_database| list_sorted_matrix_files: ' + str(ib) + ' ' + str(self.list_sorted_matrix_files[ib]))
                                #sleep(0.003)
                        else:
                            print(str(self.current_matrix_filepath) + ' does not contain ' + self.current_target_string)
                            #sleep(0.003)
                        if len(self.list_sorted_matrix_files) == len(self.list_of_web_matrix_files):
                            print('|examine_database| matrix sorting complete :)')
                            self.b_sorting_matrix = False
                '''
                #print('length len(self.list_of_web_matrix_files): ' + str(len(self.list_of_web_matrix_files)))
                #print('self.list_of_web_matrix_files[0] ' + str(self.list_of_web_matrix_files[0]))
                #sleep(1)
                #self.list_of_web_matrix_files = self.list_sorted_matrix_files
                with open(str(path + '_+|matrix_nav|+_.csv'), 'w+') as f:
                    for item in self.list_of_web_matrix_files:
                        #print('|examine_database| for item in self.list_of_web_matrix_files: ' + str(item))
                        f.write(str(item))
                        f.write('\n')
                        #sleep(0.003)
                    #print('|examine_database| ======== items in list_of_web_matrix_files =========')
                    f.close()

        #directories
        if self.b_dp == True:
            for i in range(0, len(self.list_dp)):
                #print('|examine_database| Found Directory: ' + str(i) + ' ' + str(self.list_dp[i]))
                self.list_of_directory_paths.append(self.list_dp[i])
                #sleep(0.003)
                self.b_examining_database = True

        #make a nav file -- then go deeper
        if self.b_examining_database == True:
            self.list_of_directory_paths = DatabaseTools.getListWithoutDuplicates(self, self.list_of_directory_paths)

            #f = open(str(path + '_+|directory_nav|+_.csv'), 'w+')
            #print('|examine_database| ======== items in list_of_directory_paths =========')
            with open(str(path + '_+|directory_nav|+_.csv'), 'w+') as f:
                for item in self.list_of_directory_paths:
                    #print('|examine_database| for item in self.list_of_directory_paths: ' + str(item))
                    f.write(str(item))
                    f.write('\n')
                    #sleep(0.003)
                f.close()
            #print('|examine_database| ======== items in list_of_directory_paths =========')
            self.made_decision = False
            while self.made_decision == False:
                for selected_directory_path in self.list_of_directory_paths:
                    if selected_directory_path != path:
                        #_Alice.terminal.displayThree(str(path), str('|examine_database|  will change to'), str(selected_directory_path))
                        self.list_of_visited_directory_paths.append(str(selected_directory_path))
                        self.target_directory = selected_directory_path
                        self.b_examining_database = True
                        #_Alice.terminal.displayThree(str('|examine_database| from directory'), str(path), str('======='))
                        #_Alice.terminal.displayThree(str('|examine_database| to directory '), str(self.target_directory), str('======='))
                        self.made_decision = True
                        #sleep(0.003)
        #print('length len(self.list_of_web_matrix_files): ' + str(len(self.list_of_web_matrix_files)))
        #print('self.list_of_web_matrix_files[0] ' + str(self.list_of_web_matrix_files[0]))
        ##sleep(0.5)
        return self.b_examining_database, self.list_of_web_matrix_files, self.target_directory

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/get_website_directory_filepath.history', prefix='get_website_directory_filepath', depth=1)
    def get_website_directory_filepath(self, job_name, website_target ):
        self.directory_key = None
        #print('job_name: ' + str(job_name))
        self.website_root_path = DatabaseTools.make_job_paths(self, job_name)
        #print('website_root_path: ' + str(self.website_root_path))
        self.regex = re.compile('[@_!$%^&*()<>?\|}{~:;],.')
        self.cleaned = ''
        self.previous_newVal = ''
        for ch in website_target:
            newVal = str(ch)
            if self.regex.search(ch) != None:
                newVal = '-'
            if newVal == ' ':
                newVal = '-'
            if newVal == '#':
                newVal = '-'
            if newVal == '/' and self.previous_newVal == '/':
                newVal = ''

            if newVal.isdigit() == True:
                self.cleaned += newVal
            elif newVal.isalpha() == True:
                self.cleaned += newVal
            elif newVal == '/':
                self.cleaned += newVal
            elif newVal == '':
                self.cleaned += newVal
            #print(str(ch))
            self.previous_newVal = newVal
        self.fp_url = self.cleaned

        if len(self.cleaned) > 60:
            self.fp_url = str('{:.60}'.format(str(self.cleaned)))
        else:
            self.fp_url = self.cleaned

        #print('fp_url: ' + str(self.fp_url))
        named_tuple = time.localtime() # get struct_time
        daily_time_string = time.strftime("%H_%M_%S", named_tuple)
        self.dp_website =str( str(self.website_root_path) + 'web/' + str(daily_time_string) + '/' + str(self.fp_url) )


        if self.dp_website.endswith('/'):
            #print(self.dp_website)
            pass
        else:
            self.dp_website += '/'
            #print(self.dp_website)

        if not os.path.exists( str(self.dp_website)):
            os.makedirs(  str(self.dp_website))
        sleep(0.1)
        return self.dp_website


    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/filesystem_browse_list_of_google_matrix_files.history', prefix='filesystem_browse_list_of_google_matrix_files', depth=1)
    def filesystem_browse_list_of_google_matrix_files(self, list_of_web_matrix_files, _Alice):
        #sleep(3)
        #self.clear_screen()

        print('def browse_list_of_web_matrix_files')
        #sleep(3)
        #for i in range(0, len(list_of_web_matrix_files)):
            #print('browse_web_matrix ' + str(i) + ' ' + list_of_web_matrix_files[i])
            #sleep(0.003)

        self.global_list_keys = []
        self.global_list_keys = _Alice.get_global_list_keys()
        #for i in range(0, len(self.global_list_keys)):
            #print(_Alice.name + ' ' + str(i) + ' ' + str(self.global_list_keys[i]))
            #sleep(0.003)

        self.test_matrix_rows = []
        #related language to href relationship
        self.href_queue_index = 0

        self.href_target = ''
        #self.href_target_temp_list = []

        self.href_language = ''
        self.href_language_temp_list = []

        self.csv_io_href_fields = ['queue', 'href', 'language']
        self.href_queue_list = []
        self.href_target_list = []
        self.href_language_list = []

        self.csv_io_columns = []
        #for item in list_of_web_matrix_files:
            #print('for item in list_of_web_matrix_files: ' + str(item) )
            #sleep(0.003)
        #print('length len(list_of_web_matrix_files): ' + str(len(list_of_web_matrix_files)))
        self.b_missingGoogleMatrix = False
        try:
            print('str(list_of_web_matrix_files[0]) ' + str(list_of_web_matrix_files[0]))
        except:
            #print('MISSING GOOGLE MATRIX -- !!!!!! ')
            self.b_missingGoogleMatrix = True
            self.csv_io_path = ''
            #sleep(0.5)
        if self.b_missingGoogleMatrix == False:
            self.csv_io_path = str(os.path.dirname(os.path.realpath(str(list_of_web_matrix_files[0]))))
            #print('self.csv_io_path ' + self.csv_io_path)
            #sleep(0.003)
            self.csv_io_name = str('|=-parsed-=|')
            #print('self.csv_io_name ' + self.csv_io_name)
            #sleep(0.003)
            for i in range(0, len(list_of_web_matrix_files)):
                self.test_matrix_rows = _Alice.iFileIO.getListFromFile(str(list_of_web_matrix_files[i]), 9999999)
                for row in self.test_matrix_rows:
                    #print('for row in self.test_matrix_rows: ' + str(row))
                    #sleep(0.01)
                    self.column_number = 0
                    self.href_column_value = ''
                    self.b_first_character_of_new_column = True
                    for ch in row:
                        if ch == ',':
                            self.column_number += 1
                            self.b_first_character_of_new_column = True
                        if self.column_number == 2:
                            self.href_column_value += ch
                        if self.column_number == 4:
                            if self.b_first_character_of_new_column == True:
                                self.href_language += ' '
                            self.href_language += ch
                        if self.column_number == 7:
                            self.href_language += ch
                        self.b_first_character_of_new_column = False
                    self.href_language_temp_list.append(self.href_language)
                    self.href_language = ''
                    if len(self.href_column_value) > 15 and self.href_column_value.find('.google.') == -1 and self.href_column_value.find('.googleapis.') == -1 and self.href_column_value.find('.googleadservices.') == -1 and self.href_column_value.find('.gstatic.') == -1 and self.href_column_value.find('/schema.org') == -1 and self.href_column_value.find('jpg') == -1 and self.href_column_value.find('jpeg') == -1 and self.href_column_value.find('.gif') == -1 and self.href_column_value.find('.png') == -1 and self.href_column_value.find('\\') == -1 and self.href_column_value.find('.svg') == -1 and self.href_column_value.find('.css') == -1 and self.href_column_value.find('.js') == -1 and self.href_column_value.find('.gov') == -1 and self.href_column_value.find('jquery') == -1 and self.href_column_value.find('json') == -1 and self.href_column_value.find('.xml') == -1 and self.href_column_value.find('s=function(){') == -1 and self.href_column_value != 'href' and self.href_column_value != self.href_target:
                        #load previous temp lists to row lists
                        self.href_queue_list.append(self.href_queue_index)
                        self.href_queue_index += 1
                        self.href_target_list.append(self.href_target)
                        self.href_target = self.href_column_value
                        self.combined_language = ' '
                        for item in self.href_language_temp_list:
                            if item.strip() != 'lang':
                                self.combined_language += str(item.strip()) + ' '
                        self.href_language_list.append(self.combined_language)
                        self.href_language_temp_list.clear()
            _Alice.set_nav_queue(self.href_target_list, self.href_language_list, self.global_list_keys)
            self.csv_io_columns = [self.href_queue_list, self.href_target_list, self.href_language_list]
            _Alice.iFileIO.csv.write_list_of_lists_to_csv_file(self.csv_io_columns, self.csv_io_href_fields, self.csv_io_name, self.csv_io_path, 0)
        return self.csv_io_path, self.b_missingGoogleMatrix

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/explore_matrix.history', prefix='explore_matrix', depth=1)
    def explore_matrix(self, path, _Alice):
        #sleep(3)
        #self.clear_screen()

        print('def explore_matrix')
        #sleep(3)
        self.list_paths = []
        self.list_of_file_nav = []
        self.list_of_web_matrix_files = []
        self.list_of_directory_paths = []
        self.list_of_file_paths = []
        self.list_of_visited_directory_paths = []
        self.list_of_visited_web_matrix_files = []
        self.current_navigation_matrix_filepath = ''
        self.previous_navigation_matrix_filepath = ''
        self.list_current_directory_web_matrix_files = []
        self.list_previous_navigation_matrix_files = []
        self.b_examining_database = True
        self.target_directory = ''
        self.target_directory = path
        self.job_directory = path
        self.list_google_matrix = _Alice.iFileIO.get_list_of_filepaths_containing_string( _Alice.iFileIO, 'google_search_results', path)

        #for item in self.list_google_matrix:
            #print('for item in self.list_google_matrix: \n' + str(item))
            #sleep(0.5)

        self.b_browsing_web = True
        while self.b_browsing_web == True:
            if self.b_browsing_web == True:
                #_Alice.terminal.displayThree(str(str(_Alice.name) + ' is browsing the web '), str(path), str('======='))
                self.b_browsing_web = DatabaseTools.filesystem_browse_list_of_google_matrix_files(self, self.list_google_matrix, _Alice)
        #_Alice.terminal.displayThree(str(str(_Alice.name) + ' is browsing the web '), str(path), str('======='))
        self.csv_io_path, self.b_missingGoogleMatrix = DatabaseTools.filesystem_browse_list_of_google_matrix_files(self, self.list_google_matrix, _Alice)

        #self.list_website_matrix = _Alice.iFileIO.get_list_of_filepaths_containing_string( _Alice.iFileIO, 'matrix.csv', path)

        while self.b_examining_database == True:
            if self.b_examining_database == True:
                #_Alice.terminal.displayThree(str(str(_Alice.name) + ' is exploring '), str(self.target_directory), str('======='))
                #sleep(0.5)
                self.b_examining_database, self.list_website_matrix, self.target_directory = DatabaseTools.examine_database(self, self.target_directory, _Alice)
                #for item in self.list_of_web_matrix_files:
                    #print('for item in self.list_of_web_matrix_files: \n' + str(self.target_directory) + '\n' + str(item))
                    #sleep(0.5)
        return self.list_google_matrix, self.list_website_matrix


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


    def merge_dict(self, target, *sources):
        """
        Merge the given list of `collections.Mapping` objects into `target` object.
        :param Mutablecollections.Mapping target: The collections.Mapping to receive the merge.
        :param tuple sources: The list of `collections.Mapping` objects to be merged.
        """
        for source in sources:
            if not isinstance(target, collections.MutableMapping):
                raise TypeError('target must be a dict')

            if not isinstance(source, collections.Mapping):
                raise TypeError('data must be a dict')

            for key in source:
                target_value = target.get(key)
                source_value = source[key]

                if target_value is None or source_value is None:
                    target[key] = source_value

                elif isinstance(target_value, collections.Mapping) and isinstance(source_value, collections.Mapping):
                    self.merge_dict(target_value, source_value)

                else:
                    target[key] = source_value 


    def remove_commas_between_symbols(self, iFileIO, symbol, replace, target_file):
        rows = iFileIO.getListFromFile(target_file, 9999999)
        self.modified_rows = []
        for row in rows:
            self.b_inside_symbol = False
            self.modified_row = ''
            for ch in row:
                if ch.find(symbol) != -1:
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

    def rec_merge(self, d1, d2):
        """
        Update two dicts of dicts recursively,
        if either collections.Mapping has leaves that are non-dicts,
        the second's leaf overwrites the first's.
        """
        # in Python 2, use .iteritems()!
        for k, v in d1.items():
            if k in d2:
                # this next check is the only difference!
                if all(isinstance(e, collections.MutableMapping) for e in (v, d2[k])):
                    d2[k] = self.rec_merge(v, d2[k])
                if isinstance(v, list):
                    d2[k].extend(v)
                # we could further check types and merge as appropriate here.
        d3 = d1.copy()
        d3.update(d2)
        return d3

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='getEmailList', depth=1)
    def get_email_list(self, filepath, iFileIO, maxLoops):
        #raw = session.driver.page_source
        with open(filepath, 'r') as f:
            #f = open(filepath, 'r')
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
            self.list_ignore_emails = iFileIO.get_list_from_file('/home/gordon/p3env/alice/alice/spiders/list_ignore_emails.csv', maxLoops)
            for item in duplicateLessEmails:
                if self.validateItemBasedOnList(item, self.list_ignore_emails):
                    self.cleanedEmails.append(item)
            f.close()
        return self.cleanedEmails




    def REPORT_column_of_emails_from_directory(self, source_directory, output_filepath, iFileIO):
        self.list_pretty_index_filepaths = []
        self.list_emails = []
        root = source_directory
        pattern = "*_pretty_index.html"

        for path, subdirs, files in os.walk(root):
            for name in files:
                if fnmatch(name, pattern):
                    print (os.path.join(path, name))
                    self.list_pretty_index_filepaths.append(str(os.path.join(path, name)))

        for i in range(0, len(self.list_pretty_index_filepaths)):
            self.temp_list_emails = []
            self.temp_list_emails = DatabaseTools.get_email_list(self, self.list_pretty_index_filepaths[i], iFileIO, 999999999999999)
            with open(str(output_filepath + str('TAIL')), 'a+') as f:
                f = open(str(output_filepath + str('TAIL')), 'a+')
                for email in self.temp_list_emails:
                    print('self.temp_list_emails: ' + str(email))
                    self.list_emails.append(str(email))

                    f.write(str(email))
                    f.write('\n')
                f.close()
        #self.clear_screen()
        all_emails_from_file = iFileIO.get_list_from_file(str(output_filepath + str('TAIL')), 999999999999999)
        self.list_emails = DatabaseTools.getListWithoutDuplicates(self, all_emails_from_file)
        with open(str(output_filepath + str('COMPLETE')), 'w+') as f:
            f = open(str(output_filepath + str('COMPLETE')), 'w+')
            for email in self.list_emails:
                print('self.list_emails: ' + str(email))
                f.write(str(email))
                f.write('\n')
            f.close()



    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/parse.history', prefix='getEmailList', depth=1)
    def get_NAME_list(self, a_nlp, a_matcher, filepath, iFileIO, maxLoops):
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
        #NAMES = []
        #NAMES = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", self.raw)
        LINES = iFileIO.get_list_from_file(filepath, maxLoops)
        self.list_LINES_NAME = []
        self.list_ignore_NAMES = iFileIO.get_list_from_file('/home/gordon/p3env/alice/alice/spiders/list_ignore_NAMES.csv', maxLoops)
        for line in LINES:

            #print('line: ' + str(line))
            self.NAME = ''
            self.implicit_targets = []
            self.implicit_index_positions = []
            if line.find('PERSON') != -1 or line.find('FAC') != -1 or line.find('ORG') != -1 or line.find('LOC') != -1 or line.find('NORP') != -1 or line.find('NPE') != -1:
                temp_words = line.split()
                list_words = []
                for word in temp_words:

                    #print(str(word))
                    if self.validateItemBasedOnList(word, self.list_ignore_NAMES):
                        list_words.append(word)

                #self.found_index = 0
                for i in range(0, len(list_words)):
                    if list_words[i].find('PERSON') != -1 or list_words[i].find('FAC') != -1 or list_words[i].find('ORG') != -1 or list_words[i].find('LOC') != -1 or list_words[i].find('NORP') != -1 or line.find('NPE') != -1:
                        #self.found_index = i
                        self.implicit_targets.append(str(list_words[i]))
                        self.implicit_index_positions.append(i)
                        #print(str('self.found_index:' + str(self.found_index)))
                for i in range(0, len(self.implicit_targets)):
                    current_implicit_target = self.implicit_targets[i]
                    #print('current_implicit_target: ' + str(current_implicit_target))
                    current_implicit_index = self.implicit_index_positions[i]
                    #print('current_implicit_index: ' + str(current_implicit_index))
                    self.NAME_index_start = current_implicit_index - 3
                    #print(str('self.NAME_index_start:' + str(self.NAME_index_start)))
                    if self.NAME_index_start < 0:
                        self.NAME_index_start = 0
                    for i in range(self.NAME_index_start, current_implicit_index):
                        word = str(list_words[i]).strip()
                        if word.find('...') == -1 and word.find(' ') == -1 and len(word) > 2:
                            for ch in word:
                                if str(ch).find(',') == -1 and str(ch).find(' ') == -1 and str(ch).isdigit() == False:
                                    self.NAME += str(ch)
                            self.NAME += ' '
                    #print(' -------------  ')

                    if self.validateItemBasedOnList(self.NAME.strip(), self.list_ignore_NAMES):
                        self.doc = self.a_nlp(str(self.NAME.strip()))

                        for ent in self.doc.ents:
                            if str(ent.label_).find('PERSON') != -1 or str(ent.label_).find('FAC') != -1 or str(ent.label_).find('ORG') != -1 or str(ent.label_).find('LOC') != -1 or str(ent.label_).find('NORP') != -1 or str(ent.label_).find('NPE') != -1:
                                self.NAME = str(self.NAME).strip()
                                #print(str('FOUND NAME:' + str(self.NAME)))
                                languages = []
                                valid_name = ''
                                for i, token in enumerate(self.doc):
                                    languages.append(token._.language["language"])
                                    if languages[i] != 'UNKNOWN':
                                        valid_name += str('|lang-org| ' + str(languages[i]) + ' |LANG| ' + str(token) )
                                        #print('appending: ' + str(valid_name))
                                        print('token: ' + str(token) + ' language: ' + str(languages[i]))
                                    #sleep(0.01)
                                    print(str('|------ -- - NAME: ' + str(self.NAME)) + ' :NAME - -- ------|')
                                    self.list_LINES_NAME.append(str(valid_name))
                                #break
                                #sleep(0.000123)
                #print(' -------------  ')
            #sleep(0.1234)
        duplicateLessNAMES = []
        duplicateLessNAMES = DatabaseTools.getListWithoutDuplicates(self, self.list_LINES_NAME)


        f.close()
        return duplicateLessNAMES

    def REPORT_column_of_NAME_from_directory(self, source_directory, output_filepath, iFileIO):
        self.a_nlp = spacy.load('en_core_web_sm')
        self.a_matcher = Matcher(self.a_nlp.vocab)
        self.a_nlp.add_pipe(LanguageDetector(), name="language_detector", last=True)
        self.matrix_filepaths = []
        self.list_NAMES = []
        root = source_directory
        pattern = "*matrix.csv"

        for path, subdirs, files in os.walk(root):
            for name in files:
                if fnmatch(name, pattern):
                    print (os.path.join(path, name))
                    self.matrix_filepaths.append(str(os.path.join(path, name)))
                    #sleep(0.003)

        for i in range(0, len(self.matrix_filepaths)):
            self.temp_list_NAMES = []
            self.temp_list_NAMES = DatabaseTools.get_NAME_list(self, self.a_nlp, self.a_matcher, self.matrix_filepaths[i], iFileIO, 999999999999999)
            f = open(str(output_filepath + str('TAIL')), 'a+')
            for NAME in self.temp_list_NAMES:
                #print('self.temp_list_NAMES: ' + str(NAME))
                self.list_NAMES.append(str(NAME))

                f.write(str(NAME))
                f.write('\n')
                #sleep(0.1234)
            f.close()
            #sleep(0.1234)
        #self.clear_screen()
        all_NAMES_from_file = iFileIO.get_list_from_file(str(output_filepath + str('TAIL')), 999999999999999)
        self.list_NAMES = DatabaseTools.getListWithoutDuplicates(self, all_NAMES_from_file)
        f = open(str(output_filepath + str('COMPLETE')), 'w+')
        for NAME in self.list_NAMES:
            #print('self.list_NAMES: ' + str(NAME))
            f.write(str(NAME))
            f.write('\n')
        f.close()
