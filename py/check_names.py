# -*- coding:utf-8 -*-

import os
import codecs

__author__ = 'Gree-gorey'

with codecs.open(u'noun_names.csv', u'r', u'utf-8') as f:
    names = [line.rstrip() + u'.jpg' for line in f]

# print names[8]

path = u'/home/gree-gorey/stimdb/Version_20.02.16/NounsDB2.1/NounsPictures/'

for root, dirs, files in os.walk(path):
    # for filename in files:
    #     if u' )' in filename:
    #         new_name = filename.replace(u' )', u')')
    #         os.rename(path + filename, path + new_name)

    for name in names:
        if name not in files:
            print name
