#!/usr/bin/env python

import fileinput
import sys
import os
import urllib2
import subprocess

tp_path = subprocess.Popen(['defaults', 'read', 'com.freron.MailMate', 'MmDefaultTaskPaperPath'], stdout=subprocess.PIPE).communicate()[0].rstrip()
tp_file = subprocess.Popen(['defaults', 'read', 'com.freron.MailMate', 'MmDefaultTaskPaperFile'], stdout=subprocess.PIPE).communicate()[0].rstrip()
tp_project = subprocess.Popen(['defaults', 'read', 'com.freron.MailMate', 'MmDefaultTaskPaperProject'], stdout=subprocess.PIPE).communicate()[0].rstrip()

mm_subject = os.getenv('MM_SUBJECT','')
mm_url = 'message:////%3c' + urllib2.quote( os.getenv('MM_MESSAGE_ID','') ) + '%3e'

output = os.path.join(tp_path, tp_file)


for line in fileinput.input(output, inplace=1):
  if line.startswith(tp_project):
    processing = True
  else:
    if processing:
      print '\t- ' + mm_subject + '\n\t\t' + mm_url
    processing = False
  print line,