#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys 
import re

for line in sys.stdin: 
    words = re.split('\W',line)
    for word in words:
        if word.isalpha():
          print('%s\t%s' % (word, 1))
