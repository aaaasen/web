#!/usr/bin/env python2

import os
from random import choice
import time
import cgi

print('Content-type: text/html\n\n')

#name=raw_input('Happy Mother\'s Day Mom, please enter your name: ')

fs=cgi.FieldStorage()

locname=''

for key in fs.keys():
    if key == 'name' :
       locname=fs[key].value

locname=locname.strip('\n').lower()

niceword=[['Angelic','Awesome','Awe-Inspiring','Amazing','Astonishing','Admirable'],['Bodacious','Beautiful','Benevolent','Bountiful'],['Calm','Cheerful','Charming','Considerate','Comical'],['Delectable','Desirable','Delightful'],['Excellent','Engaging','Educated'],['Fabulous','Fantastic'],['Gallant','Genius','Glorious'],['Honest','Honourable','Humorous'],['Ingenious','Impressive','Inspiring'],['Jubilant','Joyful'],['Kind','Keen'],['Loving','Light-hearted','Lovely'],['Magnificent','Marvellous','Moral'],['Nice','Neat','Notable'],['Outstanding','Outgoing'],['Perfect','Passionate','Precious'],['Qualified'],['Radiant','Reliable','Responsible'],['Special','Sacred','Splendid','Splendiferous','Sympathetic'],['Timeless','Tactful','Triumphant'],['Ultimate','Unequivocal','Upstanding'],['Vivacious','Virtuous'],['Wholesome','Win','Wise','Witty'],['XXX'],['Youthful'],['Zealous']]

locname=map(lambda x: choice(niceword[(ord(x)-97)]), locname)

print 'You are:\n<br />'

for word in locname:
    print '<br />' + word

