import string
from pychallenge import mkurl, url2comment

src = "http://www.pythonchallenge.com/pc/def/ocr.html"

comment = url2comment( src )

counter = {}
for c in comment:
	if c not in counter:
		counter[c] = 0
	counter[c] = counter[c] + 1

pairs = [ (v, k) for (k, v) in counter.iteritems() ]

delete_chars = ""
for (v,k) in pairs:
	if v > 10:
		delete_chars = delete_chars + k
val = string.translate( comment, None, delete_chars )

print( mkurl( val ) )
