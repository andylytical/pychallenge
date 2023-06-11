import string
from pychallenge import mkurl

tr_from = string.lowercase
tr_to = tr_from[2:26] + tr_from[0:2]
tr_map = string.maketrans( tr_from, tr_to )

def tr(s):
	out_str = string.translate( s, tr_map )
	print( out_str )
	print( mkurl( out_str ) )

strings = [ "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.",
"map" ]

for s in strings:
	tr(s)

#out_str = string.translate( in_str, tr_map )
#
#print( out_str )
#
#print( mkurl( out_str ) )
