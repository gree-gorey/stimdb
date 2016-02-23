# -*- coding:utf-8 -*-

import os
import re

__author__ = 'Gree-gorey'

repeat = False

for root, dirs, files in os.walk(u'/home/gree-gorey/Загрузки/VerbsDB1.1/Pictures'):
    sortedFiles = sorted(files)
    for i in xrange(len(sortedFiles)):
        word = re.search(u'[0-9]+?\. (.*?) ', sortedFiles[i], flags=re.U).group(1)
        oldName = u'/home/gree-gorey/Загрузки/VerbsDB1.1/Pictures/' + sortedFiles[i]
        if i != len(files)-1:
            if not repeat:
                nextWord = re.search(u'[0-9]+?\. (.*?) ', sortedFiles[i+1], flags=re.U).group(1)
                if word == nextWord:
                    newName = u'/home/gree-gorey/Загрузки/new/' + word + u'_1' + u'.jpg'
                    repeat = True
                else:
                    newName = u'/home/gree-gorey/Загрузки/new/' + word + u'.jpg'
            else:
                newName = u'/home/gree-gorey/Загрузки/new/' + word + u'_2' + u'.jpg'
                repeat = False
        else:
            newName = u'/home/gree-gorey/Загрузки/new/' + word + u'.jpg'

        os.rename(oldName, newName)
        # print oldName, newName