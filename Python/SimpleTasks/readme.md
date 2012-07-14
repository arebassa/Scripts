## Introduction
There are many great applications to create and manage your tasks. Some simple some more complex. Some integrate with online services others don't. SimpleTasks doesn't aim to be the new kid on the block. It's simply a personal project to help me learn python and fill in a small gap I found when I started working with OpenBox. I had previously used Gnome and then later KDE. In both I had some app or other just to help me manage my daily tasks and to-do's. However, having moved to a lighter WM, I wanted a lighter way of doing this. Enter SimpleTasks.

## The How
SimpleTasks takes advantage of the great flexibility that OpenBox pipe menus provide. New tasks can be created through an entry in a pipe menu. The resulting tasks are displayed in the pipe menu and alternatively can also be displayed on the desktop via a Conky script.

## General Usage
- Make this script executable or call it with "python path/to/script  
- Clicking on New task creates a new task.
- Clicking on available task renders it done and therefore deletes it
- It is not necessary to create the file where tasks are stored. You can call the filename as an argument to the script and if it doesn't exist it will be created. If no name is supplied then a default will be used. All that is need is to change the location where the file should be saved.
- It is possible to have the script handle various diferent tasks files, just call the script with a diferent taskfile name (-f taskfile)

### Pipe Menu
- Arguments for use with pipe menu are:
	
		-a <action> (Valid action: menu -> prints pipe menu structure)
		-f <taskfile> (File where tasks are stored)

- Put an entry in /.config/openbox/menu.xml:
`<menu id="pipe-tasklist" label="Task List" execute="python ~/.config/openbox/scripts/tasklist.py -a menu -f taskfile" />`
- Then put the following in the root-menu wherever you'd like the SimpleTasks pipe menu to be displayed:
`<menu id="pipe-tasklist" /> `

**Note:** It is possible to have various tasklists. Create another pipe menu with -f taskfile2

### Conky
- Arguments for use with conky are:

		-a <action> (Valid action: conky -> prints conky structure)
		-t <title> (Title for conky tasks. remember to quote titles with spaces)
		-f <taskfile>
		-m <number> (max number of tasks to be displayed)
		
- Place the following in your conky config:

		${execpi 1080 python /home/pedro/.config/openbox/scripts/tasklist.py -a conky -t "Groceries" -f taskfile -m 10} 

As of yet there is no way of personalizing conky display outside of the script. That is currently being worked on so for the time being personalize your conky output directly in the script.