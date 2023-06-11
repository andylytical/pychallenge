from pychallenge import mkurl, url2comment

src = "http://www.pythonchallenge.com/pc/def/ocr.html"

comment = url2comment( src )

val = string.translate( comment, None, delete_chars )

print( mkurl( val ) )
