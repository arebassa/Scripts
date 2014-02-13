![](http://media.tumblr.com/tumblr_m7020kGadh1r6w22q.png)

## The Introduction
Most who know me, are well aware of my love for [Alfred][1], a great productivity app for Mac OS X which aims to save you time in searching your local computer and the web. It makes me infinitely more productive and gives me endless possibilities for workflows that improve aforementioned productivity.   
Another little gem that has helped me control my wasted hours and thus help me focus is [TicToc][4], a simple yet feature-full  app that sits in your menubar and tracks time on various projects/tasks. Later it is possible to export tracked time to an array of formats.  
Finally, if you've read any of my previous posts (no, then go do that quick, there aren't many yet) you will also realize my new love for the simplicity and future proof of text files. I am on a constant mission to improve my workflows and include evermore text where possible.  
This is where [TaskPaper][3] comes in. I've been using it on my mac to manage my tasks and have been loving it so far. It's fast, beautiful and just plain text so it fits like a glove.

## The Itch
No matter how great and application is, there will always be an itch. Luckily TaskPaper has extensive AppleScript support so itches aren't to difficult to scratch.  
I'm referring this time in particular to Time tracking. Now there are 1 or 2 solutions over on their wiki, but I much prefer to integrate it with something I already use... You guessed it, TicToc and of course Alfred.

So without further delay I give you the extension... **[TaskPaper Timetracking](http://cl.ly/I03a)**

**Note:** You will need Alfred's [Powerpack][2] in order for this to work

## Features (so far)
- Track time on multiple tasks
- Indication of tasks currently being tracked
- Customizable tags for these actions
- Growl notifications of start/stop and error (fallback to dialog box if growl isn't installed / running)

## Usage
- Simply double click the extension to install it;
- Before the first run it is important you customize the script with your preferred tags.    
- @tictoc is the default "tracking" tag. The Value of this tag has to be the name of your task in TicToc.  

Take for instance:  

![](http://cl.ly/I0EI/Screen%20Shot%202012-07-11%20at%202.12.04%20PM.png)

I would then have to have tasks in TaskPaper as:  

    - Complete readme.md for script @tictoc(TaskPaper Timetracking)
    - Complete some random test @tictoc(test)

**NOTE:** This is case insensitive so no need to be too fussy ;)

- @running is the default for tasks being "tracked"
- After the first run you can set `registered` to **true**. It's only needed on first run in order to register the script with Growl.

## Errors
In this first version, the script will output errors in the following situations:  

- Entry selected is not a task;
- Entry selected doesn't have a tracking tag (@tictoc default);
- Tracking tag is either empty or it's value doesn't correspond to a task/event in TicToc

## Tips and Tricks

- A good use is to create a Task/Event in Tictoc with the same name as the project, or smaller aspects of the project. Say we have a project in TPM named Create Website. That can be broken down into various tasks, some relating to design, others to coding etc. We could have to events in TicToc named Design and another named Development, so...


        Create WebSite:
            - Mockup initial ideas @tictoc(Design)
            - Email mockup and get approval @tictoc(Design)
            .....
            - Code base HTML @tictoc(Development)
            - Code CSS @tictoc(Development)
            ... (you get the idea ;) )


   This would them allow you breakdown and analyze exactly how much time each part of the process took.

- Another great idea is to assign a global hotkey to trigger the extension, that way you can be in Taskpaper and quickly toggle time tracking for the selected task


## Caveats

- Unfortunately Tictoc's AppleScript support is still rather limited and therefor I have no way of telling if a task is being tracked/timed except by the @running tag. This means that if you start a task in TPM and then stop it in TicToc, I have no way yet of syncing those changes (updating @running tag in TPM) so therefore all starting and stopping should be done in TPM.  
- It is also not yet possible to create new tasks/events in ticToc with AppleScript so they will have to either already exist or be manually created beforehand.
- You **MUST** configure TicToc to allow tracking of multiple tasks otherwise things will get confused real quick

## Support

I've setup a [github page](http://cl.ly/I0Dn) for this so I ask that if you find any errors please file a issue over at github.


[1]:http://www.alfredapp.com
[2]:http://www.alfredapp.com/powerpack/
[3]:http://www.hogbaysoftware.com/products/taskpaper/
[4]:http://overcommitted.com/tictoc/