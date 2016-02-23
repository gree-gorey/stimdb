# -*- coding:utf-8 -*-
__author__ = 'Gree-gorey'

import codecs
import re

prefix = u'<a href="http://stimdb.ru/pictures/'
suffix = u'.jpg" class="wp-live-preview" target="_blank">'
end = u'</a>'

w = codecs.open(u'linkful', u'w', u'utf-8')

repeat = False
d = []

with codecs.open(u'linkless', u'r', u'utf-8') as f:
    for line in f:
        line = line.rstrip()
        d.append(line)
    for i in xrange(len(d)):
        line = d[i].rstrip()
        if i != len(d)-1:
            if not repeat:
                nextLine = d[i+1].rstrip()
                word = re.search(u'(.+?) \(.+?\)', line, flags=re.U).group(1)
                nextWord = re.search(u'(.+?) \(.+?\)', nextLine, flags=re.U).group(1)
                if word == nextWord:
                    new_line = prefix + word + u'_1' + suffix + line + end + u'\n'
                    repeat = True
                else:
                    new_line = prefix + word + suffix + line + end + u'\n'
            else:
                word = re.search(u'(.+?) \(.+?\)', line, flags=re.U).group(1)
                new_line = prefix + word + u'_2' + suffix + line + end + u'\n'
                repeat = False
        else:
            word = re.search(u'(.+?) \(.+?\)', line, flags=re.U).group(1)
            new_line = prefix + word + suffix + line + end + u'\n'
        w.write(new_line)

w.close()