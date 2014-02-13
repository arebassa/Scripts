# Alfred Spotlight Comments
![](http://cl.ly/image/341G3F20431H/Screen%20Shot%202013-01-05%20at%2002.55.15.png)

## Introduction

[Alfred][] is a great productivity app for Mac OS X which aims to save you time in searching your local computer and the web. By itself it's a great application but with the [Powerpack][]
the possibilities seem endless.


## Extension Description
I’ve been looking of ways in which Hazel could help speed up some of my workflows and decided I would create a few rules to archive files based on Spotlight comments. I quickly realised that adding those comments was a tedious chore, one better left to Alfred. So enter 
**Alfred Spotlight Comments** (catchy name ... huh)

With this handy little extension, you can select a bunch of files, trigger the extension (I’d recommend a hotkey assigned to it) and type in the comments you’d like to add. The extension allows for a default action when encountering existing spotlight comments, as well as interactive mode and parameter options (more on that later).

## Installation and Setup
As with all extension, installing is simply a matter of downloading the [extension](http://bit.ly/X7x1aU) and double clicking or dragging onto Alfred’d extension panel.

As for setup, there isn’t much to it. Simply define  what your desired default action should be when encountering existing comments.

Change `property defaultOverwrite : "append"` (line 15) accordingly. Possible options are **append**, **replace** and **interactive**.

## Extension Usage

Triggering the extension and entering text without any of the following parameters will default the the behaviour discussed above, with the exception of **delete** of course.

* **-d** — Will remove any spotlight comment from the selected files;
* **-a** — Will append to existing comments;
* **-r** — Will replace existing comments;
* **-i** — Will function interactively allowing you to decide on a file by file basis. It will display the existing comment to facilitate your decision too ;)

There is no need to leave any space after the parameter but you can do so if you prefer (it will be stripped from the begging)

**Examples**  

`comments -aExpenses,Archive,2012	`  
`comments -r 2012, expense, report`  










 [Alfred]: http://www.alfredapp.com
  [Powerpack]: http://www.alfredapp.com/powerpack/