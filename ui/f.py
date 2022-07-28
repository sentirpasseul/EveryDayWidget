# -*- coding: utf-8 -*-
# python 2

path1 = "/Users/xah/web/xahlee_info/python/xxtest"
path2 = "/Users/xah/web/xahlee_info/python/xxtest2"

coding1 = "utf-8"
coding2 = "gb18030"

f= open(path1, 'rb')
content= unicode(f.read(), coding1 )
f.close()
f= open(path2, 'wb')
f.write(content.encode(coding2))
f.close()

