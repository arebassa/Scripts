Volume Indicator

Unzip all files into the same folder.

Create 3 geeklets, 2 images and 1 script
- Image glet 1 place the background image (Normal.png)
- Image glet 2 place foreground image (any volume level image 0-100)
- Shell glet put "osascript <<path to files>>/VolumeIndicator.scpt. Set a refresh rate of about 5-10s
 The refresh rate depends on the lag between volume adjustment and geeklet update.
 Higher refresh rate less lag but (but will use a little more resources, not much though ;-) )

Edit VolumeIndicator.scpt e replace the 3 property values with the correct ones

Note: To get the geeklet id simply open GeekTool Preferences,
select the geeklet, and double click on the bottom of the inspector palette where the ID is displayed. 
This will copy the ID in the pasteboard.