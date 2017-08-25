#!/usr/bin/env python

import string
import sys
import json
import math

__all__ = [
    "removePunctuation", 
    "cleanText", 
    "progress_bar", 
    "bar_completed", 
    "readJson", 
    "writeJson",
    "stringOut"
]

__version__ = '1.0.0'

def stringOut(outstring, delim='='):
    print delim*len(outstring)
    print outstring 
    print delim*len(outstring)
    print ''

def cleanText(text) :
  	return removePunctuation(text).lower()

def removePunctuation(text) :
  	return ' '.join(text.translate(string.maketrans(string.punctuation, ' '*len(string.punctuation))).split())

def progress_bar(index, length):
	bar = "["
	percent_completion = math.ceil(float(index) * 100 / length)
	bar += int(percent_completion) * "=" + (100-int(percent_completion)) * " " + "] " + str(int(percent_completion)) + "%"
	sys.stdout.write("%s\r" % bar)
	sys.stdout.flush()

def bar_completed(process_name):
    sys.stdout.write("%s!                                                                                                           \n" % process_name)

def writeJson(dict, filename) :
	with open(filename, 'w') as f:
		json.dump(dict, f, indent=2)

def readJson(filename) :
	with open(filename, 'r') as f:
		return json.load(f)
