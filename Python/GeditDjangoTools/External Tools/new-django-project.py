#!/usr/bin/python
# [Gedit Tool]
# Name=New Django Project
# Shortcut=<Shift><Control>p
# Applicability=all
# Input=document
# Output=nothing
# Save-files=document

import os
import subprocess as sp

if __name__ == '__main__':
    f = sp.Popen("zenity --file-selection --text 'Porject Location'", shell=True, stdout=sp.PIPE)
    out = os.path.split(f.communicate()[0])
    dirname = out[0]
    project = out[1]
    os.chdir(dirname)
    sp.call('gnome-terminal -x django-admin.py startproject %s &' %project, shell=True)
