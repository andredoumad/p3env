import pysnooper, re, os

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

@pysnooper.snoop('parsehistory')
def longestStringInList(lists):
	return len(max(lists, key=len))

@pysnooper.snoop('parsehistory')
def strip_url_params2(url, param_to_strip=[]):
	if '?' not in url:
		return url
	queries = (url.split('?')[1]).split('&')
	queries_obj = [query[0] for query in queries]
	for i in range(len(queries_obj) - 1, 0, -1):
		if queries_obj[i] in param_to_strip or queries_obj[i] in queries_obj[0:i]:
			queries.pop(i)
	return url.split('?')[0] + '?' + '&'.join(queries)

@pysnooper.snoop('parsehistory')
def cleanText(self,inputText):
	'''
	Takes inputText and clean up the html special charcters.
	:return string
	'''
	inputText=inputText.decode('utf8')
	okList='abcdefghijklmnopqrstuvwxyz'
	okList+='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	okList+="1234567890!@#$%^&*()-_+=[]{}' "
	okList+=';"?.,`~'
	tempString=''
	# ignore all characters not in the ok list
	for character in inputText:
		if character in okList:
			tempString+=character
			# convert all html entities in the title to unicode charcters
			tempString=HTMLParser().unescape(tempString)
	return tempString

@pysnooper.snoop('parsehistory')
def find_between( s, first, last ):
	try:
		start = s.index( first ) + len( first )
		end = s.index( last, start )
		return s[start:end]
	except ValueError:
		return ""

@pysnooper.snoop('parsehistory')
def find_between_r( s, first, last ):
	try:
		start = s.rindex( first ) + len( first )
		end = s.rindex( last, start )
		return s[start:end]
	except ValueError:
		return ""

@pysnooper.snoop('parsehistory')
def checkKey(dict, key):
	if key in dict.keys():
		# print("Present, ", end =" ")
		#print("value =", dict[key])
		return True
	else:
		# print("Not present")
		return False

@pysnooper.snoop('parsehistory')
def updateMemoriesWithWebsiteSourceCodes(self):
	self.mined_info_lines_count =0
	self.mined_info_omitted_duplicates_count =0
	self.mined_info_fully_qualified_domains =0
	self.uniqueLinesList = []
	for path, subdirs, files in os.walk(root):
		for name in files:
			memorizedLines = []
			if fnmatch(name, pattern):
				print (os.path.join(path, name))
				fh = open(os.path.join(path, name), 'r')
				ftw = open(str(os.getcwd() + '/DATABASE/memories/TotallRecallText.txt'), 'a+')
				fw = open(str(os.getcwd() + '/DATABASE/memories/TotallRecall.html'), 'a+')
				fwd = open(str(os.getcwd() + '/DATABASE/memories/TotallRecallDomains.html'), 'a+')
				while True:
					duplicate = False
					line = fh.readline()
					self.mined_info_lines_count += 1
					try:
						for mem in memorizedLines:
							if mem == line:
								duplicate = True
					except:
						pass
					if duplicate == False:
						fw.write(line)
						memorizedLines.append(line)
						self.uniqueLinesList.append(line)
						#textLine = filter(lambda c: c.isalpha(), line)
						ftw.write(line)
					if duplicate == True:
						print("DUPLICATE LINE OMITTED: " + line)
						self.mined_info_omitted_duplicates_count += 1
					print("memorizing: " + line )
					if self.validate_url(line) == True:
						front = find_between(line, "http", " ")
						try:
							newdomain = str("http" + front + front[:-1])
							fwd.write(newdomain)
							fwd.write("\n")
							self.mined_info_fully_qualified_domains += 1
						except:
							pass
					if not line:
						break
				fh.close()
				fw.close()
				fwd.close()
	#self.memory_goalwordsdict = self.word_frequencies_from_file_matching_goals(self.ahapGoals, self.uniqueLinesList)
	csv = open(str(os.getcwd() + '/DATABASE/memories/goalWordsDict.csv'), 'w+')
	csv.write("'positive','count'")
	for key, value in self.mined_goal_words_dict.items():
		csv.write(key,',',value)

@pysnooper.snoop('parsehistory')
def word_frequencies_from_file_to_dict(self, filename):
	"""
	Returns a dictionary with the frequencies
	of the words occurring on file with name.
	"""
	file = open(filename, 'r')
	result = {}
	while True:
		line = file.readline()
		if line == '':
			break
		words = line.split(' ')
		for word in words:
			if word in result:
				result[word] += 1
			else:
				result[word] = 1
	file.close()
	return result

@pysnooper.snoop('parsehistory')
def word_frequencies_from_file_matching_goals(self, goalsList, filename):
	file = open(filename, 'r')
	result = {}
	while True:
		line = file.readline()
		if line == '':
			break
		words = line.split(' ')
		for word in words:
			if word in result:
				for goal in goalsList:
					if word == goal:
						result[word] += 1
	file.close()
	return result

'''
def word_feats(words):
	return dict([(word, True) for word in words)
'''