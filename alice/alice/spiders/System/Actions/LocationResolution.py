


'''
@pysnooper.snoop('parsehistory')
def getGeoTextNLP(self, string):
	#places = GeoText("London is a great city")
	places = GeoText(string)
	return places.cities
	# "London"

@pysnooper.snoop('parsehistory')
def getGeoTextNLPandCity(self, string, city):

	# filter by country code
	#result = geotext.GeoText('I loved Rio de Janeiro and Havana', 'BR').cities
	# 'Rio de Janeiro'
	result = GeoText(string, city).cities
	return result

@pysnooper.snoop('parsehistory')
def getGeoTextNLPDict(self, string):
	#GeoText(string).country_mentions
	#GeoText('New York, Texas, and also China').country_mentions
	# OrderedDict([(u'US', 2), (u'CN', 1)])
	return GeoText(string).country_mentions
'''

