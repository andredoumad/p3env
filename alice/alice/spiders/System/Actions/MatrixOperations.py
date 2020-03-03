import pytablereader
import pytablewriter












def printcsv(csvLocation):
	loader = pytablereader.CsvTableFileLoader(csvLocation)
	for table_data in loader.load():
		print("\n".join([
			"load from file",
			"==============",
			"{:s}".format(pytablewriter.dumps_tabledata(table_data)),
		]))
