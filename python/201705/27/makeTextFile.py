#!/usr/bin/env python

import os
ls = os.linesep

fname=raw_input("Please input file name: ")
if os.path.exists(fname):
    print "Error: '%s' already exists." % fname
else:
    context = []
    print "\nEnter lines ('.' by itself to quit.)\n" 
    
    while True:
        entry = raw_input('>')
        if entry == '.':
            break
        else:
            context.append(entry)

fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x,ls) for x in context])
fobj.close()
print "Done!"

