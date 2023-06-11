#import string
import re
from pychallenge import mkurl, url2comment

src = "http://www.pythonchallenge.com/pc/def/equality.html"

comment = url2comment( src )

rx = re.compile( "(?<![^a-z])[A-Z]{3}([a-z])[A-Z]{3}(?![^a-z])" )

rv = rx.findall( comment )
val = ''.join( rv )
print( mkurl( val ) )
