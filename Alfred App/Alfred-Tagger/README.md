![][cl]

## Introduction
Even with all the talk that Openmeta tags may disappear due to some Mountain Lion restrictions, I've decided to start tagging my files in order to better find them. Now there are a great slew of applications that support Openmeta, but since it's future is uncertain, I felt reluctant to dish out some hard earned cash on an application than may soon become obselete in the near future.

Fortunately, there are a few alternatives that are provided freely. Of those, I settled for [Tagger][bit]. The only downside for me however was the constant need to drag files onto it's icon in order to trigger it.

## A Quick Fix
Fortunately, as is the case with so many of my little itches, the fix is rather quick. A simple little automator workflow triggered by [Alfred][bit 2] and voila, no need to take my hands off the keyboard. You will of course need the [Powerpack][bit 3] in order for this to work.

## Setup and Tips
Download the pack below. You will find a zip file with the Extension and the Automator Workflow. Save the workflow any place of your choosing, import the extension and then update the path to point to where you saved the workflow.  
All you need now if to assign a global hotkey to trigger the extension (or just summon Alfred and start typing **tagger**).  
With this in place, you can now choose 1 or multiple files in finder, trigger the extension and tag away.

A quick note on **searching**, to get Alfred to search your newly created tags, just follow this [tip][bit 4]. 


[![][cl 2]][github]

[bit]: http://bit.ly/Rx8LiI
[bit 2]: http://bit.ly/QtRq8w
[bit 3]: http://bit.ly/S3rqgY
[bit 4]: http://bit.ly/S3tHsp
[cl]: http://cl.ly/JLjo/Alfred-Tagger.png
[cl 2]: http://f.cl.ly/items/2x0A1T1c0N3b1H3H3T0a/Alfed-Extension-Download.png
[github]: https://github.com/pslobo/Scripts/raw/master/Alfred%20App/Alfred-Tagger/Alfred-Tagger.zip