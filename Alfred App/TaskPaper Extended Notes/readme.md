![](http://media.tumblr.com/tumblr_m7b4dvpETQ1r6w22q.png)

## Introduction
I will forever tinker with my workflow, especially when finding new and exciting ways of improving it. One thing that does however remain a constant in almost all my workflows is [Alfred][]. Another recent addition to my workflow has been [TaskPaper][], so it would only make sense I integrate the two as much as possible.

Now while TaskPaper's notes are great, there are times when I feel I need more. That is where Extended Notes comes into play.

The concept is a rather simple one. Have a tag that defines a certain type of file. An outline file in opml format, a text file, a scrivener file etc. The value of said tag would be the file name. You can see it in action **[here][3].**

## Usage and Setup
- You need Alfred's [PowerPack][] for this to work so if you don't yet have it.. GET IT! You can thank me later.
- Download the [Extension][1] and install it the same way you install all others.
- Set your preferred keyword and then setup your tags and paths.

**Tags and Paths**  
This is where you need to be careful. The variable is a list in the manner of:  

    set workList to {{"note", "outline"}, {docPath:"/Users/pedro/Dropbox/Notes/", ext:"txt"}, {docPath:"/Users/pedro/Dropbox/Outliner/", ext:"opml"}}

Breaking it down we have:  

1. Item 1 is a list of your tags. In my case I have "Note" and "Outline"  
2. Item 2 onwards is a list of records pertaining to each tag.  

So in the above example, item 2 is a list of the **path** where you place docs related to your **Note** tag and the **extension** of your **Note** tag (some may prefer txt, md, mmd etc.)
Item 3 pertains to tag **outline**.  
If you prefer more tags/document types then just expand on this.

**NOTE:**  
If a document with the specified name doesn't exist it will be created (Text file types only so far...)

## Tips and Use Cases
- Tip number 1 and most important of all, assign a global shortcut key to this!
- Tip number 2... assign a global shortcut key to this! :)


Not to sure how this could benefit you or why you may need extra notes? Let me give you a scenario I stated in an earlier [post][2].

You're a Web Developer with a task list similar to (forgive me if it's silly but hey, I'm no WebDev) :

[![](http://f.cl.ly/items/290g1u3I0O2h2X3v3s1z/Screen%20Shot%202012-07-17%20at%205.46.29%20PM.png)](http://f.cl.ly/items/290g1u3I0O2h2X3v3s1z/Screen%20Shot%202012-07-17%20at%205.46.29%20PM.png)

With this simple list you can easily see how quickly you can get things done. Used in conjunction with my previous [extension][1] you could, without leaving your task list, toggle the timer on and open the project file you need to work on.
The added benefit is of course that you can have extensive notes without cluttering your task list.


## What's to Come
I've got a few more things planned for this and other extensions. This is far from perfect so if you find any bugs or would like to request a feature, please do so on the [GitHub][] page I've setup.

[Alfred]:http://cl.ly/HUgX
[PowerPack]:http://cl.ly/I9Mc
[Taskpaper]:http://cl.ly/I8eQ
[2]:http://cl.ly/I0W9
[1]:http://cl.ly/I8nP
[GitHub]:http://cl.ly/I4Wz
[3]:http://cl.ly/I3CP