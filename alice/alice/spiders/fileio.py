from .AliceRequiredModules import *
from .webtools import WebTools
from .databasetools import DatabaseTools
from .csv_io import CSV_IO
from .standalone_tools import *

class FileIO:
    csv = CSV_IO()
    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='debuginfo', depth=1)
    def debuginfo(self, message):
        caller = getframeinfo(stack()[1][0])
        #frame = inspect.previ
        #eventlog( "%s:%d - %s" % (caller.filename, caller.lineno, message))
        #eventlog("\n | ")
        #eventlog("|FileIO line| " + str(caller.lineno) + " start.")
        #eventlog("\n | ")
        self.debugMessageList = []
        if message is not list:
            self.debugMessageList.append(message)
        else:
            self.debugMessageList = message
        self.f = open("parse.txt", "a+")
        #self.f.write(str("|FileIO line| " + str(caller.lineno) + "| "))
        if message is list:
            for i in range(0, len(self.debugMessageList)):
                pass
                #eventlog(str("FileIO|" + str(caller.lineno) + "|START| " + str(self.debugMessageList[i]) + "  " + str(caller.lineno) +" |END|"))
                #self.f.write(str("" + str(caller.lineno) + "|START| " + str(self.debugMessageList[i]) + "  " + str(caller.lineno) +" |END|"))
        else:
            pass
            #eventlog(str("FileIO|" + str(caller.lineno) + "|START| " + str(self.debugMessageList[0])  + "  " + str(caller.lineno) +" |END|"))
            #self.f.write(str("debuginfo|" + str(caller.lineno) + "|START| " + str(self.debugMessageList[0])  + "  " + str(caller.lineno) +" |END|"))
        #eventlog("\n | ")
        
        #eventlog("\n | ")
        self.f.close()

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/getDatabaseContent.history', prefix='getDatabaseContent', depth=1)
    def getDatabaseContent(self, name, searchpath):
        for filename in Path(searchpath).glob('**/*.c'):
            eventlog(filename)
        return filename
    
    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/get_list_files_folders_in_path.history', prefix='get_list_files_folders_in_path', depth=1)
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

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='writeHrefCsv', depth=1)
    def writeHrefCsv(self, htmlsourcepath):
        #self.debuginfo(" writeHrefCsv \n")
        #self.debuginfo(" htmlsourcepath is: " + htmlsourcepath +  "\n")
        self.suffixlessFP = FileIO.getFilePathWithoutsuffix(self, htmlsourcepath)
        #self.fp = str(Path(htmlsourcepath).name + "links.csv")
        #self.debuginfo(" suffixlessFP is: " + self.suffixlessFP)
        readIt = open(htmlsourcepath, 'r')
        soup = BeautifulSoup(readIt, 'html.parser')
        links = [a['href'] for a in soup.select('a[href]')]
        readIt.close()
        self.list_ignore = WebTools.get_list_ignore(self)
        self.uniqueLinks = WebTools.getCleanurls(self, links, self.list_ignore)
        #self.uniqueLinks = links
        #self.uniqueLinksFP = str(str(os.getcwd()) + '/DATABASE/Memory/')
        self.uniqueLinksFP = str(str(self.suffixlessFP) + str("uniqueLinks.csv"))
        #self.debuginfo("Working on: " + str(htmlsourcepath))
        #self.debuginfo("uniqueLinksFP is: " + self.uniqueLinksFP)
        f = open(self.uniqueLinksFP, 'w+')
        for item in self.uniqueLinks:
            f.write(item)
            #self.debuginfo(" writing unique link: " + item )
            f.write("\n")
        f.close()
        self.xpaths = []
        for link in links:
            if link[0] == '/':
                self.xpaths.append(link)

        self.xpathsFP = str(str(self.suffixlessFP) + str("xpaths.csv"))
        f = open(self.xpathsFP, 'w+')
        for item in self.xpaths:
            f.write(item)
            #self.debuginfo(" writing unique link: " + item )
            f.write("\n")
        f.close()

        return self.uniqueLinks, self.uniqueLinksFP, self.xpaths, self.xpathsFP


    def walk(self, iFileIO, top, maxdepth):
        eventlog('def walk(self, top, maxdepth)')
        sleep(3)
        for entry in os.scandir(top):
            (self.dirs if entry.is_dir() else self.nondirs ).append(entry.path)
        yield top, self.dirs, self.nondirs
        if maxdepth > 1:
            for path in self.dirs:
                for x in iFileIO.walk(iFileIO, path, maxdepth-1):
                    yield x
        for x in iFileIO.walk(iFileIO, ".", 200):
            pass
            #eventlog('for x in self.walk(self, ".", 2): x: ' + str(x) )
            #eventlog(x)

    def search_files(self, directory='.', extension=''):
        list_found_files = []
        extension = extension.lower()
        for dirpath, dirnames, files in os.walk(directory):
            for name in files:
                if extension and name.find(extension) != -1:
                    #eventlog(os.path.join(dirpath, name))
                    list_found_files.append(str(os.path.join(dirpath, name)))
                #elif not extension:
                    #eventlog(os.path.join(dirpath, name))
                    #eventlog('|')
        '''
        extension = extension.lower()
        for dirpath, dirnames, files in os.walk(directory):
            for name in files:
                if extension and name.lower().endswith(extension):
                    eventlog(os.path.join(dirpath, name))
                elif not extension:
                    eventlog(os.path.join(dirpath, name))
        '''
        return list_found_files

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/get_list_of_filepaths_containing_string.history', prefix='get_list_of_filepaths_containing_string', depth=1)
    def get_list_of_filepaths_containing_string(self, iFileIO, iString, root_dp):

        eventlog('get_list_of_filepaths_containing_string: iString: ' + str(iString) )
        eventlog('get_list_of_filepaths_containing_string: root_dp: ' + str(root_dp) )
        self.l_results = []
        self.dirs = []
        self.nondirs = []


        '''
        extension = '.txt'
        for dirpath, dirnames, files in os.walk('.'):
            for name in files:
                if extension and name.lower().endswith(extension):
                    eventlog(os.path.join(dirpath, name))
                elif not extension:
                    eventlog(os.path.join(dirpath, name))
        '''
        eventlog('get_list_of_filepaths_containing_string: ABOUT TO WALK FILEPATHS' )
        #iFileIO.walk(iFileIO, str(root_dp), 10000000)
        #iFileIO.search_files(root_dp, )
        self.l_results =  self.search_files(str(root_dp), str(iString))
        '''
        for fp in self.nondirs:
            self.index = 0
            if fp.find(str(iString)) != -1:
                self.l_results.append(str(fp))
                eventlog('Target ' + str(self.index) + ' filepath: ' + str(fp) )
                self.index += 1
        '''
        return self.l_results



    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='combineMinedurls', depth=1)
    def get_l_fp_contents_unique_lines(self, l_fps):
        self.file_content_lines = []
        for filepath in l_fps:
            l_combined_file_contents = FileIO.get_list_from_file(self, filepath, 100000)
            l_current_file_contents = self.totalLinks
            self.file_content_lines = DatabaseTools.getCombinedLists(self, l_current_file_contents, l_combined_file_contents, 100000)
        return self.file_content_lines



    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='combineMinedurls', depth=1)
    def combineMinedurls(self, ignoreExisting, maxLoops):
        #self.debuginfo(" combineMinedurls \n")
        if not os.path.exists( str( os.getcwd() + '/DATABASE/combined/')):
            os.makedirs( str( os.getcwd() + '/DATABASE/combined/'))
        self.totalLinksFP =  str( os.getcwd() + '/DATABASE/combined/totalLinks.csv')
        self.combinedFilePathsList = []
        self.combinedFilePathsListFilePath = str( os.getcwd() + '/DATABASE/combined/combinedFilePathsList.csv')
        if not os.path.isfile( self.combinedFilePathsListFilePath):
            FileIO.clear_file(self, self.combinedFilePathsListFilePath)
        else:
            self.combinedFilePathsList = FileIO.get_list_from_file(self, self.combinedFilePathsListFilePath, maxLoops)
        from pathlib import Path
        htmlsourcepaths = str( os.getcwd() + '/DATABASE/mined/web/' + '**/' + "*.csv")
        htmlFiles = glob.glob(htmlsourcepaths, recursive=True)
        self.uniqueFiles = DatabaseTools.getListWithoutDuplicates(self, htmlFiles)
        self.totalLinks = []
        if ignoreExisting:
            #self.debuginfo(" IGNORING EXISTING FILES = \n")
            self.missingfp_urls = []
            for item in self.uniqueFiles:
                exists, fp_url = WebTools.getindexFilepathFromUrl(self, item)
                if exists == False:
                    #self.debuginfo(" targeting url " + item)
                    #sleep(0.01)
                    self.missingfp_urls.append(item)
                else:
                    self.debuginfo(" skipping url " + item)
            self.uniqueFiles = self.missingfp_urls
        for filepath in self.uniqueFiles:
            #self.debuginfo("\n" + filepath)
            if filepath.find('uniqueLinks') != -1:
                moreLinks = FileIO.get_list_from_file(self, filepath, maxLoops)
                currentLinks = self.totalLinks
                self.totalLinks = DatabaseTools.getCombinedLists(self, currentLinks, moreLinks, maxLoops)
                self.combinedFilePathsList.append(str(filepath))

        FileIO.writelistOfStuff(self, self.totalLinks, self.totalLinksFP)

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='getFileDate', depth=1)
    def getFileDate(self, path_to_file):
        stat = os.stat(path_to_file)
        try:
            ##self.debuginfo(" File Was Created on: " + str(stat.st_birthtime))
            #sleep(0.01)
            return stat.st_birthtime
        except AttributeError:
            ##self.debuginfo(" File Was Modified on: " + str(stat.st_mtime))
            #sleep(0.01)
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='compileLinksFromMinedSearchEngines', depth=1)
    def compileLinksFromMinedSearchEngines(self, ignoreExisting, ignoreOldFiles, maxLoops):
        #self.debuginfo(" compileLinksFromMinedSearchEngines \n")
        from pathlib import Path
        htmlsourcepaths = str( os.getcwd() + '/DATABASE/mined/web/' + '**/' + '**/'  + '**/' + "*.html")
        htmlFiles = glob.glob(htmlsourcepaths, recursive=True)
        self.uniqueFiles = DatabaseTools.getListWithoutDuplicates(self, htmlFiles)
        if ignoreExisting:
            #self.debuginfo(" IGNORING EXISTING FILES = \n")
            #sleep(0.01)
            self.missingfp_urls = []
            self.loops = 0
            self.working = True
            while self.working == True:
                for item in self.uniqueFiles:
                    self.loops +=1
                    if self.loops > maxLoops:
                        self.working = False
                        break
                    #self.debuginfo(" Item is: " + item)
                #sleep(0.01)
                    exists, fp_url = FileIO.getFileExists(self, item)
                    if exists == False:
                        #self.debuginfo(" targeting url " + item)
                        #sleep(0.01)
                        self.missingfp_urls.append(item)
                    else:
                        self.debuginfo(" skipping url " + item)
                        #sleep(0.01)
                self.uniqueFiles = self.missingfp_urls
                self.working = False

        if ignoreOldFiles:
            #self.debuginfo(" IGNORING OLD FILES = \n")
            #sleep(0.01)
            self.missingfp_urls = []
            for item in self.uniqueFiles:
                #self.debuginfo(" Item is: " + item)
                #sleep(0.01)
                fileDate = FileIO.getFileDate(self, item)
                ##self.debuginfo("getFileDate(item) is: " + str(fileDate))
                sourceCodeDate = FileIO.getFileDate(self, __file__)
                ##self.debuginfo("getFileDate(__file__) date is:  " + str(sourceCodeDate))
                #sleep(0.01)
                age = float(float(sourceCodeDate - fileDate) / 4)
                if age < 2500:
                    #self.debuginfo(" filepath age is: " + str(age) + " and will be INCLUDED.")
                    #sleep(0.01)
                    self.missingfp_urls.append(item)
                else:
                    self.debuginfo(" filepath age is: " + str(age) + " and will be IGNORED.")
                    #sleep(0.01)
            self.uniqueFiles = self.missingfp_urls
        for filepath in self.uniqueFiles:
            #self.debuginfo("\n" + filepath)
            FileIO.writeHrefCsv(self, filepath)


    def write_dict_file(self, iDict, columns, fp ):
        CSV_IO.write_dict_to_csv_file(self, iDict, columns, fp )


    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='write_dict_to_csv_file', depth=1)
    def os_make_web_directories(self, subdirectory, webTargetPage):
        webKey = "".join([c for c in webTargetPage if c.isalpha() or c.isdigit() or c==' ']).rstrip()

        if not os.path.exists( str(os.getcwd() + '/DATABASE/mined/web/' + str(subdirectory) + str(webKey) )):
            os.makedirs( str(os.getcwd() + '/DATABASE/mined/web/' + str(subdirectory) + str(webKey) ))
            #writehistoryEvent(webKey, " New directory..")
        htmlsourcepath = str( os.getcwd() + '/DATABASE/mined/web/' + str(subdirectory) + str(webKey)  + '/' + "index.html")
        textFilePath = str( os.getcwd() + '/DATABASE/mined/web/' + str(subdirectory) + str(webKey)  + '/' +"textFilePath.html")
        emailFilePath = str( os.getcwd() + '/DATABASE/mined/web/' + str(subdirectory) + str(webKey)  + '/' + "emailFilePath.html")
        plinkfilepath = str( os.getcwd() + '/DATABASE/mined/web/' + str(subdirectory) + str(webKey)  + '/' + "plinkfilepath.html")
        linksFilePath = str( os.getcwd() + '/DATABASE/mined/web/' + str(subdirectory) + str(webKey)  + '/' +"linksFilePath.html")
        plinkahap  = str( os.getcwd() + '/DATABASE/mined/web/' + str(subdirectory) + str(webKey)  + '/' + "plinkahap.html")
        badlinks  = str( os.getcwd() + '/DATABASE/mined/web/' + str(subdirectory) + str(webKey)  + '/' + "badlinks.html")
        return str(str(os.getcwd() + '/DATABASE/mined/web/' + str(subdirectory) + str(webKey)))


    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='write_dict_to_csv_file', depth=1)
    def leave(self, session):
        session.driver.close()
        quit()

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='write_dict_to_csv_file', depth=1)
    def randListElems(self, list):
        #s=set(range(min,max))
        import random
        s = ""
        max = int(len(list))
        choice = random.randint(1, max)
        index = 0
        newList = []
        for elem in list:
            if index == choice:
                s = elem
                ii = 0
                for element in list:
                    if ii != choice:
                        newList.append(element)
                    ii += 1
            else:
                index += 1
        return s, newList

    '''
    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='write_dict_to_csv_file', depth=1)
    def memorizeEverything(self, filepath):
        
        if filepath[:4] == ".pyc" or filepath[:4] == ".history":
            pass
        if filepath[:3] == ".py":
            base=os.path.basename(filepath)
            eventlog("Found some code " + base)

        elif not os.path.exists( str(os.getcwd() + '/DATABASE/FileIO/memory' + str(subdirectory) + str(webKey) )):
            if filepath[1:] == ".":
                filepath = filepath[1:]
            elif filepath[1:] == "/":
                os.makedirs( str(os.getcwd() + '/DATABASE/FileIO/memory' + str(filepath) + str(webKey) ))
    '''


    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='write_dict_to_csv_file', depth=1)
    def makefilepath(self, filepath):
        base = os.path.basename(filepath)
        eventlog("Filepath base is: " + base)
        if not os.path.exists( base ):
            os.makedirs( base )
            eventlog("Directory path was created:  " + base)
        else:
            eventlog("Directory path exists :  " + base)


    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='getFileExists', depth=1)
    def getFileExists(self, filepath):
        if not os.path.isfile( filepath):
            #self.debuginfo("MISSING, returning False, None")
           #sleep(0.01)
            return False, None
        else:
            #self.debuginfo("FOUND, returning True, filepath")
            return True, filepath
        
    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='|FileIO|writeFileAs| ', depth=1)
    def io_get_filepath_as(self, filepath, suffix):
        dp = str(os.path.abspath(os.path.join(os.path.dirname(filepath))))
        suffixlessFilepath = FileIO.getFilePathWithoutsuffix(self, filepath)
        newFilepath = str( suffixlessFilepath + "." + suffix)
        return newFilepath, dp


    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='|FileIO|writeFileAs| ', depth=1)
    def io_write_file_as(self, filepath, suffix, contents, operand):
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
    for dirname, dirnames, filenames in os.walk('.'):
        # eventlog path to all subdirectories first.
        for subdirname in dirnames:
            eventlog(os.path.join(dirname, subdirname))

        # eventlog path to all filenames.
        for filename in filenames:
            eventlog(os.path.join(dirname, filename))

        # Advanced usage:
        # editing the 'dirnames' list will stop os.walk() from recursing into there.
        if '.git' in dirnames:
            # don't go into any .git directories.
            dirnames.remove('.git')
    '''






    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='|FileIO|write_line| ', depth=1)
    def write_line(self, filepath, string, operation):
        f = open(filepath, operation)
        #self.debuginfo(string)
        f.write(string + "\n")
        f.close()

    def tail(self, filename, numberOfLines, searchstring, boolSearchForString ):
        # Tail
        
        numberOfLines * -1
        linesUp = numberOfLines * -1
        find_str = searchstring                   # String to find
        fname = filename
        #fname = "g:/autoIt/ActiveWin.history_2"     # File to check

        with open(fname, "r") as f:
            f.seek (0, 2)           # Seek @ EOF
            fsize = f.tell()        # Get Size
            f.seek (max (fsize-1024, 0), 0) # Set pos @ last n chars
            lines = f.readlines()       # Read to end

        lines = lines[linesUp:]
        linesList = []
        for line in lines[linesUp:]:
            #eventlog(str(line))
            linesList.append(line)

        #lines = lines[-10:]    # Get last 10 lines


        if boolSearchForString == True:
            # This returns True if any line is exactly find_str + "\n"
            eventlog (find_str + "\n") in lines
            # If you're searching for a substring
            for line in lines:
                if find_str in line:
                    eventlog (True)
                    break
        return linesList

    #too big.


    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='|FileIO|getListFromFile| ', depth=1)
    def get_list_from_file(self, filepath, maxLoops):
        
        self.listFromFile = []
        self.listFromFile.clear()

        self.counter = 0
        self.loops = 0
        self.working = True
        with open(filepath) as self.fh:
            #self.fh = open(filepath)
            self.max = maxLoops + 500
            while self.working == True:
                for line in self.fh:
                    self.loops +=1
                    if self.loops > self.max:
                        self.working = False
                        break
                    self.listFromFile.append(line.rstrip())
                    #eventlog(line)
                self.working = False
            self.fh.close()
        return self.listFromFile


    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='|FileIO|makeCsv| ', depth=1)
    def csv_write_row(self, filepath, fields):
        with open(filepath, 'a+') as f:
            self.row = ""
            self.valueSeparater = ", "
            for index in range(0, len(fields)):
                self.row += str(fields[index])
                if index < int(len(fields) - 1):
                    self.row += self.valueSeparater
            f.write(str(self.row) + '\n')
        

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='|FileIO|makeCsv| ', depth=1)
    def csv_check_lines_for_duplicate_line_of_values(self, filepath, values):
        self.row = ""
        self.valueSeparater = ", "
        for index in range(0, len(values)):
            self.row += str(values[index])
            if index < int(len(values) - 1):
                self.row += self.valueSeparater

        eventlog("checking for duplicate row of values: " + str(self.row))
        with open(filepath, 'r') as f:
            #f = open(filepath, 'r')
            self.listFromFile = []
            counter = 0
            #loops = 0
            while True:
                #loops +=1
                #if loops > maxLoops:
                    #break
                ##self.debuginfo("loop " + str(loops))
                line = f.readline()
                if line == '':
                    break
                ##self.debuginfo("getListFromFile Line " + str(counter) + " is " + str(line) )
                self.listFromFile.append(line.rstrip())
                counter += 1
            f.close()
        self.duplicatesCounter = 0
        for i in range(0, len(self.listFromFile)):
            if self.listFromFile[i] == self.row:
                self.duplicatesCounter += 1
                eventlog("FOUND " + str(self.duplicatesCounter) + " DUPLICATE ROW of values: " + str(self.row))
        return self.duplicatesCounter


    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='|FileIO|makeCsv| ', depth=1)
    def csv_read_into_nested_dict(self, filepath, fields):
        with open(filepath, 'a+') as f:
            self.row = ""
            self.valueSeparater = ", "
            for index in range(0, len(fields)):
                self.row += str(fields[index])
                if index < int(len(fields) - 1):
                    self.row += self.valueSeparater
            f.write(str(self.row) + '\n')



    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='|FileIO|getFilePathWithoutsuffix| ', depth=1)
    def get_fp_without_suffix(self, filepath):
        filepathWithoutsuffix = filepath.split('.')
        fpIndex = 0
        for fpElement in filepathWithoutsuffix:
            ##self.debuginfo(" filepathWithoutsuffix element " + str(fpIndex) + " is: " + fpElement)
            fpIndex += 1
        return str(filepathWithoutsuffix[0])

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='read_csv_rows', depth=1)
    def read_csv_rows(self, path):
        """
        Extract the rows from the CSV at the specified path.
        Will throw an error if the file doesn't exist.

        :type path: string
        :rtype: list[list[string]]
        """
        with open(path, 'rU') as infile:
            reader = csv.reader(infile, delimiter=',')
            rows = [row for row in reader]
            # eliminate trailing cols that have no entries (CSI-215)
            for idx, row in enumerate(rows):
                clipIndex = 0
                for col in row[::-1]:
                    if not col:
                        clipIndex -= 1
                    else:
                        break
                if clipIndex < 0:
                    rows[idx] = rows[idx][:clipIndex]
        return rows 



    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix=str('UNDEFINIED'), depth=1)
    def write_key_value_file(self, csvfile, dictionary,append=False):
        """Writes a dictionary to a writable file in a CSV format

        Args
            csvfile (FILE): Writable file
            dictionary (dict): Dictionary containing key-value pairs
            append (bool, optional): Writes `key,value` as fieldnames if False

        Returns:
            None: No return
        """
        writer = csv.writer(csvfile, delimiter=',')
        if not append:
            writer.writerow(['key','value'])
        for key,val in dictionary.items():
            writer.writerow([key,val]) 


    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix=str('UNDEFINIED'), depth=1)
    def read_key_value_file(self, csvfile):   
        """Reads CSV file, parses content into dict

        Args:
            csvfile (FILE): Readable file

        Returns:
            DICT: Dictionary containing file content
        """
        kvstore = {}  # init key value store
        first_line = csvfile.readline()
        if 'key' not in first_line or 'value' not in first_line:
            csvfile.seek(0)  # Seek to start if first_line is not an header
        dialect = csv.Sniffer().sniff(first_line, delimiters=',\t')
        reader = csv.reader(csvfile, dialect)  # create reader
        for row in reader:
            kvstore[row[0]] = row[1]
        return kvstore


    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix=str('UNDEFINIED'), depth=1)
    def from_csv(self, fp, field_names = None, **kwargs):

        dialect = csv.Sniffer().sniff(fp.read(1024))
        fp.seek(0)
        reader = csv.reader(fp, dialect)

        table = PrettyTable(**kwargs)
        if field_names:
            table.field_names = field_names
        else:
            #if py3k:
                #table.field_names = [x.strip() for x in next(reader)]
            #else:
                #table.field_names = [x.strip() for x in reader.next()]
            table.field_names = [x.strip() for x in reader.next()]
        for row in reader:
            table.add_row([x.strip() for x in row])

        return table 





    def load_input_data(self, points):
        """Creates DictReader from *.csv file.

        :param points (file object):
            *.csv file with
            'lon' (required),
            'lat' (required), 
            'name' (optional) columns.
        
        Returns:
            data (csv.DictReader)
        """

        dialect = csv.Sniffer().sniff(points.read())
        
        points.seek(0)

        data = csv.DictReader(points, dialect=dialect)
        
        return data 











    '''
    def remove(self, spec_or_id=None, multi=True, **kwargs):
            """Remove a document(s) from this collection.

            **DEPRECATED** - Use :meth:`delete_one` or :meth:`delete_many` instead.

            .. versionchanged:: 3.0
            Removed the `safe` parameter. Pass ``w=0`` for unacknowledged write
            operations.
            """
            warnings.warn("remove is deprecated. Use delete_one or delete_many "
                        "instead.", DeprecationWarning, stacklevel=2)
            if spec_or_id is None:
                spec_or_id = {}
            if not isinstance(spec_or_id, collections.Mapping):
                spec_or_id = {"_id": spec_or_id}
            write_concern = None
            if kwargs:
                write_concern = WriteConcern(**kwargs)
            with self._socket_for_writes() as sock_info:
                return self._delete(sock_info, spec_or_id, multi, write_concern)








    def _fields_list_to_dict(fields, option_name):
        """Takes a sequence of field names and returns a matching dictionary.

        ["a", "b"] becomes {"a": 1, "b": 1}

        and

        ["a.b.c", "d", "a.c"] becomes {"a.b.c": 1, "d": 1, "a.c": 1}
        """
        if isinstance(fields, collections.Mapping):
            return fields

        if isinstance(fields, collections.Sequence):
            if not all(isinstance(field, string_type) for field in fields):
                raise TypeError("%s must be a list of key names, each an "
                                "instance of %s" % (option_name,
                                                    string_type.__name__))
            return dict.fromkeys(fields, 1)

        raise TypeError("%s must be a collections.Mapping or "
                        "list of key names" % (option_name,)) 
    '''







    def _update_nested_dict(self, original_dict, new_dict):
        """Update the dictionary and its nested dictionary fields.

        Note: This was copy-pasted from:
            opengrok/xref/submodules/yelp_lib/yelp_lib/containers/dicts.py?r=92297a46#40
            The reason is that this revision requires yelp_lib>=11.0.0 but we
            can not use this version yelp-main yet (see YELPLIB-65 for details).
            It's simpler to just temporarily pull this in.

        :param original_dict: Original dictionary
        :param new_dict: Dictionary with data to update
        """
        # Using our own stack to avoid recursion.
        stack = [(original_dict, new_dict)]
        while stack:
            original_dict, new_dict = stack.pop()
            for key, value in new_dict.items():
                if isinstance(value, collections.Mapping):
                    original_dict.setdefault(key, {})
                    stack.append((original_dict[key], value))
                else:
                    original_dict[key] = value




    def to_key_val_list(self, value):
        """Take an object and test to see if it can be represented as a
        dictionary. If it can be, return a list of tuples, e.g.,

        ::

            >>> to_key_val_list([('key', 'val')])
            [('key', 'val')]
            >>> to_key_val_list({'key': 'val'})
            [('key', 'val')]
            >>> to_key_val_list('string')
            ValueError: cannot encode objects that are not 2-tuples.

        :rtype: list
        """
        if value is None:
            return None

        if isinstance(value, (str, bytes, bool, int)):
            raise ValueError('cannot encode objects that are not 2-tuples')

        if isinstance(value, collections.Mapping):
            value = value.items()

        return list(value)








    # From mitsuhiko/werkzeug (used with permission). 


    '''
    def build_vocabulary( words, max_size ):
        vocab_instances = 0
        unique_counts = Counter(words)
        d = dict(unique_counts.most_common(cfg.vocabulary_size-2) )
        vocabulary = OrderedDict( sorted(d.items(), key=lambda t: t[1],  reverse=True) )

        # start at 2 to leave room for padding & unknown
        pb = Progress_bar(len(d) - 1) 
        for i, (key, value) in enumerate(vocabulary.items(), start=2):		
            vocab_instances += value
            vocabulary[key] = i
            pb.tick()

        vocabulary[cfg.padding_char] = 0
        vocabulary[cfg.placeholder_char] = 1
        #reverse the vocbulary (for reverse lookup)
        rev_vocabulary = {v: k for k, v in vocabulary.items()}	
        vocab = (len(unique_counts), vocab_instances, vocabulary, rev_vocabulary)

        return vocab 

    '''



    '''
    def build_vocab(self, train_data):
        counter = collections.Counter()
        for stories, questions, answerself:
            for story in stories:
                for sent in story:
                    for word in nltk.wself
                        counter[word.lself
            for question in questions:self
                for word in nltk.word_tokenize(question):
                    counter[word.lower()] += 1
            for answer in answers:
                for word in nltk.word_tokenize(answer):
                    counter[word.lower()] += 1
        # no OOV here because there are not too many words in dataset
        word2idx = {w:(i+1) for i, (w, _) in enumerate(counter.most_common())}
        word2idx["PAD"] = 0
        idx2word = {v:k for k, v in word2idx.items()}
        return word2idx, idx2word 
    '''





    '''
    def generate_csv(domains, file_name):
        output = open(file_name, 'w')
        writer = csv.writer(output)

        # First row should always be the headers
        writer.writerow(CSV_HEADERS)

        for domain in domains:
            row = []

            # Grab the dictionary for each row.
            # Keys for the dict are the column headers.
            results = domain.generate_results()

            for column in CSV_HEADERS:
                row.append(results[column])

            writer.writerow(row)

        output.close() 
    '''


    def _writeToCSV(self):
            '''
            INFO
            ----
            Writes a 2-dimensional list to a CSV text file
            Comma-delimits values.  If there is no data, then there is no attempt to
            creat a file.

            RETURNS
            -------
            None

            '''
            '''
            if self._dataAsList:
                with open(self._filePathAndName,'w') as csvFile:
                    writer = csv.writer(csvFile, lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC )
                    writer.writerows(self._dataAsList)
                csvFile.close() 
            '''
            
            eventlog('needs work,')











    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='getRawFileContents', depth=1)
    def getRawFileContents(self, filepath):
        self.raw = ''
        f = open(filepath, "r")
        self.raw = f.read()
        f.close()
        return self.raw

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='getRawFromPdf', depth=1)
    def getRawFromPdf(self, pdf_path):
        self.pdfText = ''
        with open(pdf_path, 'rb') as fh:
            # iterate over all pages of PDF document
            for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
                # creating a resoure manager
                resource_manager = PDFResourceManager()
                # create a file handle
                fake_file_handle = io.StringIO()
                # creating a text converter object
                converter = TextConverter(
                                    resource_manager, 
                                    fake_file_handle, 
                                    codec='utf-8', 
                                    laparams=LAParams()
                            )

                # creating a page interpreter
                page_interpreter = PDFPageInterpreter(
                                    resource_manager, 
                                    converter
                                )

                # process current page
                page_interpreter.process_page(page)
                # extract text
                self.pdfText = fake_file_handle.getvalue()
                yield self.pdfText

                # close open handles
                converter.close()
                fake_file_handle.close()
        return self.pdfText


    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='getRawFromDoc', depth=1)
    def getRawFromDoc(self, doc_path):
        temp = docx2txt.process("getRawFromDoc.docx")
        text = [line.replace('\t', ' ') for line in temp.split('\n') if line]
        return ' '.join(text)

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='getListFromFile', depth=1)
    def getListFromFile(self, filepath, maxLoops):
        f = open(filepath, 'r')
        listFromFile = []
        self.counter = 0
        self.loops = 0
        self.working = True
        
        while self.working == True:
            self.loops +=1
            if self.loops > maxLoops:
                self.working = False
                break
            ##self.debuginfo("loop " + str(loops))
            line = f.readline()
            if line == '':
                break
            ##self.debuginfo("getListFromFile Line " + str(counter) + " is " + str(line) )
            listFromFile.append(line.rstrip())
            self.counter += 1
        self.working = False
        f.close()
        return listFromFile


    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='writelistOfStuff', depth=1)
    def writelistOfStuff(self, listOfStuff, filename):
        f = open(filename, 'a+')
        counter = 0
        for stuff in listOfStuff:
            #self.debuginfo("writelistOfStuff line: " + str(counter) + " is " + str(stuff))
            f.write(str(stuff) + "\n")
            counter += 1
        f.close()


    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='getPathsAndTime', depth=1)
    def getPathsAndTime(self, fp):
        fp_access_history =''
        b_filepath_exists = False
        if fp.find(".") != -1:
            filename, file_suffix = os.path.splitext(fp)
            dp = str(os.path.abspath(os.path.join(os.path.dirname(fp),"..")))
            b_filepath_exists = True
        else:
            dp = fp
            fp_access_history = str(dp + "def_getPathsAndTime.history" )

        if not os.path.exists(dp):
            os.makedirs(dp)
            b_new = True
        else:
            b_new = False
        return b_filepath_exists, b_new, dp, fp, fp_access_history

    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='writeDictToCsv', depth=1)
    def writeDictToCsv(self, filepath, theDict, fields, dictIndex):
        self.values = []
        with open(str(filepath), 'a+') as f:
            self.row = ""
            self.valueSeparater = ", "
            for index in range(0, len(fields)):
                try:
                    self.row += theDict[dictIndex][str(fields[index])]
                except:
                    self.debuginfo("\n\n - - - - - - - - - EXCEPTION - - - - - - - - - \n\n")
                    self.debuginfo("\n why is this part failing? \n")
                if index < int(len(fields) - 1):
                    self.row += self.valueSeparater
                    #sleep(0.01)
            ##self.debuginfo(str(self.row))
            f.write(self.row + '\n')
        #self.debuginfo("Writing dict index to row csv file complete")


    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='clear_file', depth=1)
    def clear_file(self, filepath):
        f = open(filepath, 'w+')
        #self.debuginfo("clearing " + str(filepath))
        f.write("")
        f.close()


    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='makeCsv', depth=1)
    def makeCsv(self, filepath, fields):
        with open(filepath, 'a+') as f:
            self.row = ""
            self.valueSeparater = ", "
            #self.debuginfo(self.row)
            #sleep(0.01)
            for index in range(0, len(fields)):
                self.row += fields[index]
                #self.debuginfo(self.row)
                #sleep(0.01)
                if index < int(len(fields)):
                    self.row += self.valueSeparater
                    #self.debuginfo(self.row)
                    #sleep(0.01)
            #self.debuginfo(self.row)
            #sleep(0.01)
            f.write(self.row + '\n')
        #self.debuginfo("Writing complete")


    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='getFilePathWithoutsuffix', depth=1)
    def getFilePathWithoutsuffix(self, filepath):
        filepathWithoutsuffix = filepath.split('.')
        
        fpIndex = 0
        for fpElement in filepathWithoutsuffix:
            ##self.debuginfo(" filepathWithoutsuffix element " + str(fpIndex) + " is: " + fpElement)
            fpIndex += 1
        return str(filepathWithoutsuffix[0])



    #@pysnooper.snoop('/home/gordon/p3env/alice/alice/spiders/auto_cleared_history/fileio.history', prefix='bot_db_initialize_filepaths', depth=1)
    def bot_db_initialize_filepaths(self, url_landingPage, dp_root):
        #self.debuginfo(str("bot_db_initialize_filepaths"))
        #sleep(1.5)
        path0 = "".join([c for c in url_landingPage if c.isalpha() or c.isdigit() or c==' ']).rstrip()
        path1 = path0.replace(" ", "")
        fixedName = ''
        if len(path1) > 60:
            fixedName = str('{:.60}'.format(str(path1)))
        else:
            fixedName = path1
        
        #self.debuginfo(path1)
        self.htmlsourcepath = str( dp_root + "web/" + fixedName  + '/' + fixedName + "index.html")
        
        self.nlp_targets = str( dp_root + 'nlp_targets.csv')
        self.navigation_targets = str( dp_root + 'navigation_targets.csv')
        self.fp_db_archive = str( dp_root + 'fp_db_archive.csv')
        self.fp_db_realtime = str( dp_root + 'fp_db_realtime.csv')
        self.fp_db_queue = str( dp_root + 'fp_db_queue.csv')
        self.fp_db_dev_report = str( dp_root + 'fp_db_dev_report.csv')
        self.fp_db_user_report = str( dp_root + 'fp_db_user_report.csv')
        self.dp_db_web = str( dp_root + 'web/')
        self.fps = [self.htmlsourcepath, self.dp_db_web, self.navigation_targets, self.fp_db_archive, self.fp_db_realtime, self.fp_db_queue, self.fp_db_dev_report, self.fp_db_user_report, self.nlp_targets ]
        for filepath in self.fps:
            #self.debuginfo( "\n bot_db_initialize_filepaths ++ \n sending filepath \n"+ filepath + " \n")
            self.b_filepath_exists, self.b_new, self.dp, fp, self.fp_access_history = FileIO.getPathsAndTime(self, filepath)
            #self.debuginfo( "\n bot_db_initialize_filepaths after getPathsAndTime ++ \n new, directory, filepath, fp access history \n"+ str(b_new) + " \n" + dp + " \n" + filepath + " \n" + fp_access_history  + " \n")
            ##sleep(1.5)
        return self.b_new, self.htmlsourcepath, self.dp_db_web, self.navigation_targets, self.fp_db_archive, self.fp_db_realtime, self.fp_db_queue, self.fp_db_dev_report, self.fp_db_user_report, self.nlp_targets