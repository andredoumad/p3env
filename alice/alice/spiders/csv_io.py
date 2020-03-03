from inspect import currentframe, getframeinfo, getsourcelines, stack
import os
import csv
import unittest
from csv import DictWriter
import pysnooper
# This is the csv file read/write class.
from time import sleep
import platform    # For getting the operating system name
import subprocess  # For executing a shell command



class CSV_IO(object):

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
        
    dict_filepath_rows = {}
    dict_filepath_fields = {}
    dict_filepath_names = {}
    dict_fields_names = {}
    dict_values_names = {}
    dict_phrases_names = {}
    
    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/CSV_IO.history', prefix='__init__', depth=1)
    def __init__(self):
        self.sourcecode_name, self.sourcecode_path  = self.init_sourcecode()
        self.iPair = {'CSV_IO':str(os.getcwd())}
        self.iMatrix = 0
        self.n_dict_name_paths = {self.iMatrix:self.iPair}
        self.dict_filename_to_path = {}
        self.dict_filepath_to_filename = {}
        self.n_dict_filename_filepath_list_fields = {}
        self.n_dict_filename_filepath_list_rows = {}
        self.dict_field_filename = {}
        self.dict_phrase_filename = {}
        self.dict_value_filename = {}

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/CSV_IO.history', prefix='init_sourcecode', depth=1)
    def init_sourcecode(self):
        self.sourcecode_name = str(str(getframeinfo(currentframe()).filename))
        self.sourcecode_path = str(os.path.abspath(os.path.join(os.path.dirname(self.sourcecode_name))))
        return self.sourcecode_name, self.sourcecode_path

    line_return_character = '\r\n'
    comma_separator = ', '

    # Write a data_list into a csv file identified by file_path.
    # Each element in the data_list is also a list object represent one row.
    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/CSV_IO.history', prefix='write_list_to_csv_file', depth=1)
    def write_list_to_csv_file(self, data_list, file_path):

        try:
            file_object = open(file_path, 'w')
            csv_file_writer = csv.writer(file_object, delimiter=",", quoting=csv.QUOTE_ALL, quotechar="'")

            for item in data_list:
                csv_file_writer.writerow(item)

            print(file_path + " has been created successfully.")
        except FileNotFoundError:
            print(file_path + " not found.")


    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/Terminal.history', prefix='displayTwoLists', depth=1)
    def balance_list_pair(self, rowTargetLength, center, right):
        print('center Length is: ' + str(len(center)))
        print('right Length is: ' + str(len(right)))
        self.length = 0
        if len(center) != len(right):
            print('\n\nWARNING LINE LENGTHS DO NOT MATCH!\n\nWARNING LINE LENGTHS DO NOT MATCH!\n\nWARNING LINE LENGTHS DO NOT MATCH!\n\nWARNING LINE LENGTHS DO NOT MATCH!\n\nWARNING LINE LENGTHS DO NOT MATCH!')

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

        print('\n\n SUCCESS THE LENGTHS MATCH  \n\n')

        print('extending to matrix target length')

        if self.length != rowTargetLength:
            print('\n\nWARNING LINE LENGTHS DO NOT MATCH!\n\nWARNING LINE LENGTHS DO NOT MATCH!\n\nWARNING LINE LENGTHS DO NOT MATCH!\n\nWARNING LINE LENGTHS DO NOT MATCH!\n\nWARNING LINE LENGTHS DO NOT MATCH!')

            for i in range(self.length, len(rowTargetLength)):
                center.append('- ---- -')
                right.append('- ---- -')

            self.length = rowTargetLength

        print('\n\n SUCCESS THE LENGTHS MATCH  rowTargetLength\n\n')
        '''
        for i in range(0, rowTargetLength):
            string = str(str(i) + " " + str(center[i]) + " " + str(right[i]))
            print(string)
        '''
        return center, right


    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/tRight.history', prefix='tRight', depth=1)
    def tRight(self, string):
        s0 = str('{:.200}'.format(str(string)))
        #now pad 10 chars on each side
        s1 = str('{:>10}'.format(s0))
        return s1

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/tLeft.history', prefix='tLeft', depth=1)
    def tLeft(self, string):
        #first 10 chars only
        s0 = str('{:.200}'.format(str(string)))
        #now pad 10 chars on each side
        s1 = str('{:<10}'.format(s0))
        return s1

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/tCenter.history', prefix='tCenter', depth=1)
    def tCenter(self, string):
        #first 10 chars only
        s0 = str('{:.200}'.format(str(string)))
        #now pad 10 chars on each side
        s1 = str('{:^10}'.format(s0))
        return s1

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/displayThree.history', prefix='displayThree', depth=1)
    def displayThree(self, left, center, right):
        string = str(self.tLeft(left) + " " + self.tCenter(center) + " " + self.tLeft(right))
        #self.debuginfo(string)
        return string

    # Write a data_list into a csv file identified by file_path.
    # Each element in the data_list is also a list object represent one row.
    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/write_list_to_csv_file.history', prefix='write_list_to_csv_file', depth=1)
    def write_list_of_lists_to_csv_file(self, listOfLists, fields, spreadsheet_name, path_root, iresult):
        #sleep(3)
        #self.clear_screen()

        print('\n ---------------- def write_list_of_lists_to_csv_file ---------------- \n')
        #sleep(3)

        self.target_directory = str(path_root + '/' + str(spreadsheet_name) + '/')
        
        self.temp_target_directory = ''
        self.previous_ch = ''
        for ch in self.target_directory:
            if self.previous_ch != '/' and ch == '/':
                self.temp_target_directory += str(ch)
            elif ch != '/':
                self.temp_target_directory += str(ch)
            self.previous_ch = str(ch)
            #print(str(self.temp_target_directory))
        self.target_directory = str(self.temp_target_directory)
        #print(self.target_directory)
        if not os.path.exists(self.target_directory):
            os.makedirs( self.target_directory)
        self.records = {}
        self.dictionaries = {}
        self.rows = []
        self.matrixRowCount = 0
        self.spreadsheetRowsStringOfLines = []
        self.spreadsheetRowsListOfItems = []
        self.matrix_filepath = ''
        for column in listOfLists:
            if self.matrixRowCount < len(column):
                self.matrixRowCount = len(column)

        #in the event that a few lists are sent to this method that are not the same length, we do this.
        for column in listOfLists:
            if self.matrixRowCount > len(column):
                self.matrixRowCount = len(column)
                for i in range(len(column), self.matrixRowCount):
                    column.append('- ---- -')

        self.firstRow = ''
        self.firstRowList = []
        self.firstRowList = fields

        #in the event that the number of fields provided does not match the number of lists, we do this.
        if len(listOfLists) != len(fields):
            for i in range(len(fields), len(listOfLists)):
                fields.append(str('field-' + str(i) ))
                self.firstRowList.append(str('field-' + str(i) ))
        #we make sure the fields are separated by commas
        for i in range(0, len(fields)):
            self.firstRow += str(fields[i])
            if i < len(fields) :
                self.firstRow += ', '

        #print(str('first row is: ' + str(self.firstRow)))
        self.spreadsheetRowsStringOfLines.append(str(self.firstRow))
        self.newRowList = []
        self.matrixTerminal = []
        self.formatted_listOfLists = []
        for icol in range(0, len(listOfLists)):
            self.col_name = self.firstRowList[icol]
            self.column_values = listOfLists[icol]
            self.column_length = len(self.column_values)
            self.column_filepath = str( self.target_directory + str(spreadsheet_name) + '_iresult_' + str(iresult) + '_field_' + str(self.col_name) + '_icol_' + str(icol) + '.csv')
            self.column_values_unformatted = []
            self.column_values_unformatted = listOfLists[icol]
            self.column_values_formatted = []
            self.unformatted_column_fields = ['entity_text', 'href', 'lang']
            self.b_check_for_invalid_data = False
            for i in range(0, len(self.column_values_unformatted)):
                self.left = str(str(self.col_name))
                self.center = str('Total: ' + str(icol) + '/' + str(len(listOfLists)))
                self.right = str('Task: ' + str(i) + '/' + str(len(self.column_values_unformatted)))
                terminal_string = self.displayThree(self.left, self.center, self.right)
                #print(terminal_string)
                self.str0 = ''
                #self.str0 = str(self.column_values_unformatted[i])
                self.str0 = str('{:.500}'.format(str(self.column_values_unformatted[i])))
                self.dirty_value = False
                if self.str0.find(',') != -1:
                    self.dirty_value = True
                if self.str0.find('"') != -1:
                    self.dirty_value = True
                if self.str0.find(';') != -1:
                    self.dirty_value = True
                #print('original val: ' + str(self.str0))
                self.str1 = ''
                self.str1 = ' '.join(self.str0.split())
                if self.dirty_value == True:
                    #print('progress val: ' + str(self.str1))
                    self.chars_replace = ',";'
                    self.translated_col_value = ''
                    for ch in self.str1:
                        if str(ch) in str(self.chars_replace):
                            self.translated_col_value += ' '
                        else:
                            self.translated_col_value += str(ch)
                else:
                    self.translated_col_value = self.str1
                self.col_value = self.translated_col_value
                #print(self.col_value)
                self.column_values_formatted.append(self.col_value)
            self.column_values = self.column_values_formatted
            self.formatted_listOfLists.append(self.column_values)

            #f = open(self.column_filepath, 'w+')
            #for val in self.column_values:
                #f.write(str(val))
                #f.write(str('\n'))
            #f.close()

        for row_index in range(0, self.matrixRowCount):
            #print('Matrix row_index: ' + str(row_index))
            #sleep(0.1)
            self.newRowList.clear()
            self.newRowString = ''
            
            for col_index in range(0, len(self.formatted_listOfLists)):
                #print('Matrix column ' + str(col_index) + ' length is: ' + str(len(self.formatted_listOfLists[col_index])))
                #sleep(0.075)
                self.col_name = self.firstRowList[col_index]
                self.col_list = self.formatted_listOfLists[col_index]
                self.col_value = self.col_list[row_index]
                self.newRowList.append(self.col_value)
                self.newRowString += str(self.col_value)
                if col_index < len(self.formatted_listOfLists):
                    self.newRowString += ', '
                self.left = str(spreadsheet_name)
                self.center = str('|iresult|' + str(iresult) + '|irow|' + str(row_index) + '|icol|' + str(col_index) + '||' + str(self.firstRowList[col_index] + '||'))
                self.right =  str(self.col_value)
                terminal_string = self.displayThree(self.left, self.center, self.right)
                #print(terminal_string)
                self.matrixTerminal.append(terminal_string)
            self.spreadsheetRowsStringOfLines.append(self.newRowString)
            self.spreadsheetRowsListOfItems.append(self.newRowList)

        self.matrix_filepath = str(self.target_directory + str(spreadsheet_name) + '_iresult_' + str(iresult) + '_matrix.csv') 
        f = open(str(self.matrix_filepath), 'w+')
        #string = str('Matrix_time' + ', ' + str(self.firstRow))
        #f.write(string)
        #f.write(str('\n'))
        for i in range(0, len(self.spreadsheetRowsStringOfLines)):
            #f.write(str(i) + ', ' + str(self.spreadsheetRowsStringOfLines[i]))
            f.write(str(self.spreadsheetRowsStringOfLines[i]))
            f.write(str('\n'))
        f.close()


        f = open(str(str(self.target_directory) + 'test_csv_io.csv'), 'w+')
        #string = str('Matrix_time' + ', ' + str(self.firstRow))
        #f.write(string)
        #f.write(str('\n'))
        for i in range(0, len(self.spreadsheetRowsStringOfLines)):
            #f.write(str(i) + ', ' + str(self.spreadsheetRowsStringOfLines[i]))
            f.write(str(self.spreadsheetRowsStringOfLines[i]))
            f.write(str('\n'))
        f.close()



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



    # Write a data_list into a csv file identified by file_path.
    # Each element in the data_list is a dictionary object represent one row.
    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/CSV_IO.history', prefix='write_dict_to_csv_file', depth=1)
    def write_dict_to_csv_file(self, data_list, column_name_list, file_path):
        try:
            file_object = open(file_path, 'w')
            csv_dict_file_writer = csv.DictWriter(file_object, fieldnames=column_name_list)
            csv_dict_file_writer.writeheader()

            for item in data_list:
                csv_dict_file_writer.writerow(item)

            print(file_path + " has been created successfully.")
        except FileNotFoundError:
            print(file_path + " not found.")

    # Read csv file line by line and return the content.
    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/CSV_IO.history', prefix='read_csv_file_by_reader', depth=1)
    def read_csv_file_by_reader(self, file_path):
        ret = ''
        try:
          file_object = open(file_path, 'r')
          csv_file_reader = csv.reader(file_object, delimiter=',')
          row_number = 0

          for row in csv_file_reader:
              # Get one row list data string value,
              # below code can avoid type convert error if column has number or boolean value.
              row_str = ''
              row_size = len(row)
              for i in range(row_size):
                  row_str += str(row[i]) + self.comma_separator

              print("row_" + str(row_number) + " = " + row_str)
              ret += row_str
              ret += self.line_return_character
              row_number += 1
        except FileNotFoundError:
            print(file_path + " not found.")
        finally:
          print("ret = " + ret)
          return ret





    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/CSV_IO.history', prefix='syncronize_filename', depth=1)
    def syncronize_filename(self, filename, filepath, filename_to_path, filepath_to_filename, filename_filepath_list_fields, filename_filepath_list_rows, field_filename, phrase_filename, value_filename):
        self.db_filename = ''
        self.db_filepaths = ''
        for key, value in filename_to_path.items():
            print("syncronizing_CSV_IO_dict_filename_to_path: " + str(key) + " : " + str(value))
            if key == filename:
                self.dict_filename_to_path.update(filename, filepath)
        for key, value in self.dict_filepath_to_filename.items():
            print("checking " + str(filename) + " dict_filepath_to_filename paths: " + str(key) + " for matching names: " + str(value))
            if filename == value:
                print("Found " + str(filename) + " in path: " + str(value))

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/CSV_IO.history', prefix='pair_filename_to_path', depth=1)
    def pair_filename_to_path(self, filename, file_path):
        self.dict_filename_to_path.update(str(filename), str(file_path))

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/CSV_IO.history', prefix='get_filepath_of_filename', depth=1)
    def get_filepath_of_filename(self, filename):
        for key, value in self.dict_filename_to_path.items():
            if key == filename:
                print("found filename: " + str(filename) + " located in path: " + str(value))
            return value



    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/CSV_IO.history', prefix='read_filepath_fieldnames', depth=1)
    def read_filepath_fieldnames(self, file_path):
        ret = ''
        self.dict_fields = {}
        try:
            file_object = open(file_path, 'r')
            # csv.DictReader will return a dictionary list.
            csv_file_dict_reader = csv.DictReader(file_object)

            # Get csv file fields name list.
            field_names = csv_file_dict_reader.fieldnames

            # Get field name list size.
            field_name_size = len(field_names)

            # Get each field name.
            for i in range(field_name_size):
                field_name = field_names[i]
                ret += field_name + self.comma_separator
                self.dict_fields.update(field_name, filename)
            return self.dict_fields
        except:
            print(file_path + " not found.")
            print("bro what's with the tabs.")

            print(file_path + " not found.")


    # Read csv file line by line and return the content.
    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/CSV_IO.history', prefix='read_csv_file_by_dict_reader', depth=1)
    def read_csv_file_by_dict_reader(self, file_path):
        ret = ''
        try:
          file_object = open(file_path, 'r')
          # csv.DictReader will return a dictionary list.
          csv_file_dict_reader = csv.DictReader(file_object)

          # Get csv file fields name list.
          field_names = csv_file_dict_reader.fieldnames

          # Get field name list size.
          field_name_size = len(field_names)

          # Get each field name.
          for i in range(field_name_size):
              field_name = field_names[i]
              ret += field_name + self.comma_separator

          # Add line return character.
          ret += self.line_return_character
          print("Field Names : " + ret)

          row_number = 0
          # Each row is one dictionary.
          for row in csv_file_dict_reader:
              row_str = ''
              # Loop the row field name.
              for i in range(field_name_size):
                  field_name = field_names[i]
                  # Get field value in this row. Convert to string to avoid type convert error.
                  row_str += str(row[field_name]) + self.comma_separator

              print("row_" + str(row_number) + " = " + row_str)
              ret += row_str
              ret += self.line_return_character
              row_number += 1
        except FileNotFoundError:
            print(file_path + " not found.")
        finally:
          print("ret = " + ret)
          return ret

# This is the test case class for CSVFileOperator class.
class TEST_CSV_IO(unittest.TestCase):

    # Test CSVFileOperator's write_list_to_csv_file.
    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/CSV_IO.history', prefix='test_write_list_to_csv_file', depth=1)
    def test_write_list_to_csv_file(self):
        data_row_header = ['Name','Email','Title']
        data_row_1 = ['jerry','jerry@dev2qa.com','CEO']
        data_row_2 = ['tom','tom@dev2qa.com','Developer']
        data_list = [data_row_header, data_row_1, data_row_2]
        csv_file_operator = CSV_IO()
        csv_file_operator.write_list_to_csv_file(data_list, "./csv_user_info.csv")

    # Test CSVFileOperator's write_dict_to_csv_file.
    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/CSV_IO.history', prefix='test_write_dict_to_csv_file', depth=1)
    def test_write_dict_to_csv_file(self):
        # First create some dictionary type data.
        data_row_header = ['Coding Language','Popularity']
        data_row_1 = {'Coding Language':'Java','Popularity':'17797'}
        data_row_2 = {'Coding Language':'JavaScript','Popularity':'18998'}
        data_row_3 = {'Coding Language':'Python','Popularity':'29898'}
        data_row_4 = {'Coding Language':'C++','Popularity':'16567'}
        data_row_5 = {'Coding Language':'C','Popularity':'9989'}
        data_row_6 = {'Coding Language':'Html','Popularity':'18983'}

        # Add dictionary data into a list
        data_list = [data_row_1, data_row_2, data_row_3, data_row_4, data_row_5, data_row_6]
        csv_file_operator = CSV_IO()
        csv_file_operator.write_dict_to_csv_file(data_list, data_row_header, "./csv_coding_language.csv")

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/CSV_IO.history', prefix='test_read_csv_file_by_reader', depth=1)
    def test_read_csv_file_by_reader(self):
        csv_file_operator = CSV_IO()
        csv_file_operator.read_csv_file_by_reader("./csv_coding_language.csv")

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/CSV_IO.history', prefix='test_read_csv_file_by_dict_reader', depth=1)
    def test_read_csv_file_by_dict_reader(self):
        csv_file_operator = CSV_IO()
        csv_file_operator.read_csv_file_by_dict_reader("./csv_coding_language.csv")

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/CSV_IO.history', prefix='test_chronos_operations', depth=1)
    def test_chronos_operations(self):
        csv_file_operator = CSV_IO()
        csv_file_operator.read_csv_file_by_dict_reader("./csv_coding_language.csv")
        #clock.test_chronos_tables()

def run_all_test_case():
    unittest.main()

def run_special_test_case(test):
    # Create a TestSuite object.
    test_suite = unittest.TestSuite()
    # Add test.
    test_suite.addTest(test)
    # Create a TestResult object to save test result info.
    test_result = unittest.TestResult()
    # Run the test suite.
    test_suite.run(test_result)

if __name__ == '__main__':
    run_special_test_case(TEST_CSV_IO("test_chronos_operations"))
    '''
    run_all_test_case()
    run_special_test_case(TEST_CSV_IO("test_read_csv_file_by_reader"))
    run_special_test_case(TEST_CSV_IO("test_read_csv_file_by_dict_reader"))
    run_special_test_case(TEST_CSV_IO("test_write_list_to_csv_file"))
    run_special_test_case(TEST_CSV_IO("test_write_dict_to_csv_file"))
    '''