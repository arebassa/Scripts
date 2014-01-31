![][tumblr]

## Introduction
A while back I took the plunge and handed all my task /project management needs over to TaskPaper. I haven't regretted the decision, in fact quite the contrary.  
My current needs are humble and since I could never really get into GTD most other applications are overkill. Those that aren't, are either too slow, dumbed down or just plain rubbish.
TaskPaper however, is a nimble, lightning fast and extremely versatile application. It's text format so it's future proof and lite on resources, syncs well with other devices and it's very scriptable.

## Context
One key feature of TaskPaper is it's tagging system. Tags as basically "@" follow by some text with an optional value. This allows me to set up contexts rather easily, @home, @work, @client(TimCook), @today, @priority(1), you get the gist of it.
Contexts are great, but even better is when contexts become aware of your location. This opens up a whole new realm of automation possibilities.

## Make it Happen
What makes this possible with TaskPaper is a separate application called [ControlPlane][bit]. 

>ControlPlane allows you to build configuration profiles, contexts in ControlPlane lingo, for your Mac based on where you are or what you are doing.  ControlPlane determines where you are or what you are doing based on a number of available evidence sources and then automatically reconfigures your Mac based on your preferences.

Setting up an evidence source and corresponding context (as in a location)  is rather easy and I won't go into that here. I will however cover how that can be useful for our TaskPaper workflow.

I currently have 2 main locations (context in ControlPlane lingo) setup, Home and Work. When I get to work I obviuosly want to see my work related tasks and when I get home, my home related tasks. Now there are 2 ways of doing this and I'll cover both.

## Download and Install
Before we get started though, you will need to download [this][bit 2] little shell script and save it somewhere. You will then need to edit in some basic information before it will work. Open the script in your favourite editor (textedit will do fine too) and change the location to where you store your TaskPaper files, namely the **TPDIR** variable.  

The shell script accepts 2 arguments, the name of your TaskPaper file (required) and the Search Field String (optional)

## Separate Files
In the event that you keep separate files for dirent cenarios, one for work and one for personal then it's rather simple. Once you have your locations setup, navigate to the **Actions** tab, add a new **System Action > Run Shell Script**. A file chooser will popup at which time you should point to the shell script. You will then need to further edit the Parametar field and add the name of your file as such:

	/Users/pedro/Development/Scripts/TaskPaper Scripts/SetContext.sh|Work.taskpaper
	
Note the **|** , ControlPlane uses it to separate arguments that will be passed to the shell script. Set which context (location) you want this to be triggered and when (arrive, depart, both) and that's it. Get creative and let the Automation begin.

![][cl]

## Search Field String
Taking the previous example a little further, or in case you just use one single file and tag all your contexts with @home @work etc. we make use of the second possible argument. The Search Field String.

Create or edit your action as in the previous case but this time we add a second paramater. The Search Fiels String, just as you would do in TaskPaper.  

	/Users/pedro/Development/Scripts/TaskPaper Scripts/SetContext.sh|Work.taskpaper|@today and not project = Archive
	
With the above example, when I get to work, TaskPaper will open my Work file and set the search string to **@today and not project = Archive**

## So Many Possibilities
ControlPlane has many more Evidence Sources as seen on the site. Thanks to that and this little shell script, the possibilities are endless.

- Like to review while at starbucks each morning, set eveidence source for their wifi and a certain time;
- Want to see what's on your list for weekend home improvement, set location to home and time to weekend... you get the drift...

[bit]: http://bit.ly/TMTOYW
[bit 2]: http://bit.ly/Nmhhzi
[cl]: http://f.cl.ly/items/0P1e1N0E0w1z2v2i112B/Screen%20Shot%202012-09-11%20at%2013.32.15%20.png
[tumblr]: http://media.tumblr.com/tumblr_ma5bobjcnf1r6w22q.png