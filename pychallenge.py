import urllib
from HTMLParser import HTMLParser

URL_BASE = "http://www.pythonchallenge.com/pc/def"

def mkurl(s):
	return "{0}/{1}.html".format(URL_BASE, s)

def url2comment(url, i=-1):
	f = urllib.urlopen( url )
	parser = MyHtmlParser()
	parser.feed( f.read() )
	return parser.comments[i]


def url2parts( url ):
	f = urllib.urlopen( url )
	parser = MyHtmlParser()
	

class MyHtmlParser(HTMLParser):
	def __init__(self):
		self.comments = []
		HTMLParser.__init__(self)

	def handle_comment(self, data):
		self.comments.append(data)
