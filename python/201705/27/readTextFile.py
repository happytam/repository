#!/usr/bin/env python

import  os

fileName = raw_input("Enter fileName: ")
try:
    fileObj = open(fileName, 'r')
except IOError, e:
    print "%s file open error: %s" % (fileName,e)
else:
    for eachLine in fileObj:
        print eachLine;
    fileObj.close()
