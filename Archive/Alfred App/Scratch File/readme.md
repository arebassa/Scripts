![](http://media.tumblr.com/tumblr_m53pfi6Gn01r6w22q.png)

## The Introduction
I was inspired by this [idea](http://cl.ly/H7lz) from Gabe over at [Macdrifter](http://www.macdrifter.com/) and decided to port the idea over to my [Alfredapp][1]. A shell extension, part of the [PowerPack](http://www.alfredapp.com/powerpack/) could surely make quick work of this... and indeed it did!

I've created a quick and easy way of appending text to a file. This is great for those that have a running file or one or more text files that are used to capture ideas or whatever you may see fit (as long as it's text of course).

This also works wonderfully with [TaskAgent](http://taskagentapp.com/) text files!

Working a little on Gabe's method and simplifying it with see, text can either be appended to the beginning of a file or to the end of a file.


## Usage
- Downloaded  the extension [**here**](http://cl.ly/I2BP) 
- Double click, give it a name and then choose Import;
- Personalize the keyword to fit your needs or just leave the default;
- Now choose whether you wan't to append to begging or end of file and uncomment as needed;
- Place the path to your scratch file (remember to escape spaces if you have any). A simple way of doing it is just drag the text file onto the text area.
- All done. Now enjoy! 


- If however you prefer, you can simply create a new shell extension and add the following code:

        # A simple script to keep a running file.
        # 
        # 2 options available, insert at beginning of file or append to end of file
        # Uncomment the desired action and remember to edit the path to your scratchfile

        ## Insert at beginning of file #
        #------------------------------#

        sed -i '' -e "1i\\
        - {query}" PATH TO TEXT FILE HERE


        ## Append to end of file #
        #------------------------#

        #sed -i '' -e "a\\
        #- {query}" PATH TO TEXT FILE HERE

- Next click on advanced and make sure your options look like the following otherwise strange things could happen with your text

![](http://media.tumblr.com/tumblr_m53rac8nqc1r6w22q.png)

You can have more than one file by simply creating another extension and changing the path to the new file.

## The Caveats
Now this is far from perfect and has a few caveats that I must point out.

1. If the filename or path to file has a space, remember to escape it otherwise this will fail;
2. The file must have some text in it to start off with. This is a limitation of BSD's version of sed (if anybody knows a way around this please let me know so that I may update the post and extension);
3. While not really a caveat, I should point out that this script is adding a "-" at the beginning of each line so as to work nicely with my TaskAgent lists. If you don't wan't that then simply remove the "-" before {query} in the above script.