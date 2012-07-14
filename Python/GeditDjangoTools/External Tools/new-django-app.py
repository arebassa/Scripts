#!/usr/bin/python
# [Gedit Tool]
# Name=New Django Application
# Shortcut=<Shift><Control>a
# Applicability=all
# Output=nothing
# Input=document
# Save-files=document

import os
import subprocess as sp

def manage():
    '''
    Find manage.py or output error if not found (meaning not in django project)
    '''
    # Get directory of current file
    p = os.path.split(os.environ['GEDIT_CURRENT_DOCUMENT_PATH'])
    while(True):
        #Find manage.py or output error if not found (meaning not in django project)
        f = os.path.join(p[0],'manage.py')
        if os.path.isfile(f):
            return f
        elif p[0] == r'/':
            return 'Error'
        else:
            p = os.path.split(p[0])
        
if __name__ == '__main__':
    f = manage()
    if f == 'Error':
        sp.call("zenity --error --text 'Current file is not part of a Django Project.'", shell=True)
    else:
        fd = sp.Popen('zenity --entry --text "Application Name"', shell=True, stdout=sp.PIPE,)
        out = fd.communicate()[0]
        name = out[0:-1] #Cater to communicate() newline caracter
        sp.call('gnome-terminal -x python %s startapp %s &' %(f, name), shell=True)
