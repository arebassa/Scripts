# Network Actions for Alfred
![](http://media.tumblr.com/tumblr_lyewz9pEcl1qlw248.png)

#Introduction

[Alfred][] is a great productivity app for Mac OS X which aims to save you time in searching your local computer and the web. By itself it's a great application but with the [Powerpack][]
the possibilities seem endless.


# Extension Description
If you're anything like me and appreciate an uncluttered menubar then this extension is for you. I often have to use a VPN for work and until now, that meant having to either:  
* Have the icon on the menubar for quick access and knowing when it's active;  
* Or open system preferences, navigate to network, connect or check the VPN's state.  

__Not anymore!__ Network Actions to the rescue! With Network Actions I can easily toggle my VPN on/off and check it's status with Growl (fallback do popup dialog if you don't have growl). Here's how it works...


# Extension Installation and Setup
__Step 1__  
[Download](http://cl.ly/I1r0) and install the Etension. To install all you have yo do is double click it and alfred will do the rest.  
__Step 2__  
Edit a few basic values in the AppleScript, namely:  
* The name of the VPN Service as seen in Network Settings;  
* The location of an icon you'd like to appear in the Growl Notification. Personally I use [these][icons]  
__Step 3__  
On first run you'll have to Register with Growl. Just open alfred and typ __nw growl__


# Extension Usage
__nw__ Will toggle the service on/off depending on it' state. 
__nw on__ Will simply connect the service;  
__nw off__ Will simply disconnect the service;  
__nw stat__ Will show the current state of the connection using Growl (or fallback method)

More actions to come soon...

# Tips and Tricks
A useful trick is to assign a global shortcut key to the extension. That way you can easily check the state of the service or toggle it on/off with a simple keypress. Give it a try and you'll see how much time it saves (not to mention menubar real-estate now that you don't need the vpn icon ;) ) 



  [Alfred]: http://www.alfredapp.com
  [Powerpack]: http://www.alfredapp.com/powerpack/
  [icons]: http://bit.ly/Ahw7ke