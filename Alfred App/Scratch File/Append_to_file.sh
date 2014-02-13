# A simple script to keep a running file.
# 
# 2 options available, insert at beginning of file or append to end of file
# Uncomment to desired action and remember to edit the path to your scratchfile. The easiest way is to drag the file onto the textarea.

## Insert at beginning of file #
#------------------------------#

sed -i '' -e "1i\\
- {query}" PATH TO FILE HERE (Simple Drag the file onto this spot)


## Append to end of file #
#------------------------#

#sed -i '' -e "a\\
#- {query}" PATH TO FILE HERE (Simple Drag the file onto this spot)
