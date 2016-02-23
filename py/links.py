# -*- coding:utf-8 -*-

import codecs
import re

__author__ = 'Gree-gorey'

prefix = u'<a href="http://stimdb.ru/pictures/'
suffix = u'" class="wp-live-preview" target="_blank">'
end = u'</a>'

with codecs.open(u'linkful', u'w', u'utf-8') as w:

    with codecs.open(u'noun_names.csv', u'r', u'utf-8') as f:
        for line in f:
            line = line.rstrip()
            filename = line.replace(u' ', u'_')
            filename = filename.replace(u'\'', u'_')
            name = re.sub(u' [0-9]+\.jpg', u'', line, flags=re.U)
            name = name.replace(u'\'', u'&#39;')
            new_line = prefix + filename + suffix + name + end + u'\n'
            w.write(new_line)


'''
RE-шечки для geany

\t(.*?)\n

 (\1)\n

<span id="409">409</span>

<span id="\1">\1</span>\n
'''
