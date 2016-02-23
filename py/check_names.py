# -*- coding:utf-8 -*-

import os
import codecs
import re

__author__ = 'Gree-gorey'


def nouns():
    with codecs.open(u'noun_names.csv', u'r', u'utf-8') as f:
        names = [line.rstrip() + u'.jpg' for line in f]

    path = u'/home/gree-gorey/stimdb/Version_20.02.16/NounsDB2.1/NounsPictures/'

    for root, dirs, files in os.walk(path):
        # for filename in files:
        #     if u' )' in filename:
        #         new_name = filename.replace(u' )', u')')
        #         os.rename(path + filename, path + new_name)

        # for filename in files:
        #     new_name = re.sub(u'([0-9]+?)\. (.+?)\.jpg', u'\\2 #\\1.jpg', filename, flags=re.U)
        #     os.rename(path + filename, path + new_name)

        for name in names:
            if name not in files:
                print name


def verbs():
    names = []
    with codecs.open(u'verb_names.csv', u'r', u'utf-8') as f:
        for line in f:
            line = line.rstrip().split(u'\t')
            names.append(line[1] + u' (' + line[2] + u') #' + line[0] + u'.jpg')

    # print names[5]

    path = u'/home/gree-gorey/stimdb/Version_20.02.16/VerbsDB1.2/Pictures/'

    for root, dirs, files in os.walk(path):
        for name in names:
            if name not in files:
                print name

        # for filename in files:
        #     new_name = re.sub(u'([0-9]+?)\. (.+?)\.jpg', u'\\2 #\\1.jpg', filename, flags=re.U)
        #     os.rename(path + filename, path + new_name)

verbs()
