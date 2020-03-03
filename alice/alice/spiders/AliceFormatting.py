from .AliceRequiredModules import *

global FSP
_Fps = "/"
_Tbs = ","
import numpy
import pysnooper
#standard column preview
def default(string):
	#first 10 chars only
	s0 = str('{:.10}'.format(str(string)))
	#now pad 10 chars on each side
	s1 = str('{:^15}'.format(s0))
	return s1

def tRight(string):
	s0 = str('{:.200}'.format(str(string)))
	#now pad 10 chars on each side
	s1 = str('{:>10}'.format(s0))
	return s1
def tLeft(string):
	#first 10 chars only
	s0 = str('{:.200}'.format(str(string)))
	#now pad 10 chars on each side
	s1 = str('{:<10}'.format(s0))
	return s1
def tCenter(string):
	#first 10 chars only
	s0 = str('{:.200}'.format(str(string)))
	#now pad 10 chars on each side
	s1 = str('{:^10}'.format(s0))
	return s1

def tConsole(string):
	#first 10 chars only
	s0 = str('{:.160}'.format(str(string)))
	#now pad 10 chars on each side
	s1 = str('{:>10}'.format(s0))
	return s1

tempCols = []
def tAppendCols(col):
	global tempCols
	tempCols.append(col)

def tClearTempCols():
	tempCols.clear()

tempRows = []
def tAppendRows(value):
	global tempRows
	tempRows.append(value)


def tClearTempRows():
	tempRows.clear()


def aliceFormatStringForCSV(string):
	#first 10 chars only
	s0 = str('{:.10}'.format(str(string)))
	#now pad 10 chars on each side
	s1 = str('{:^15}'.format(s0))
	return s1


def microstring(string):
	#first 10 chars only
	#s0 = "".join([c for c in string if c.isalpha() or c.isdigit() or c==' ']).rstrip()
	s0 = str('{:.10}'.format(str(string)))
	return s0






