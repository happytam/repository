#!/usr/bin/env python

import os 
ls = os.linesep

fileName = raw_input("Please input fileName: ")
context = []
if os.path.exists(fileName):
    print "\nError: %s file is exist.\n" % fileName
else:
    print "\nEnter '.' to quit."
    while True:
        line = raw_input(">")
        if line=='.':
            break
        else:
            context.append(line)
fileObj = open(fileName, 'w')
fileObj.writelines(['%s\n' % x for x in context])
fileObj.close()
print 'Done'

