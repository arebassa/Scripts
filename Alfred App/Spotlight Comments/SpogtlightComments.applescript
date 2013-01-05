--  Alfred Spoghtlight Comment
-- 
--  Add Spotlight Comments with Alfred
--  For further instructions read the README.md or visit http://palobo.tumblr.com
--
--  Copyright (C) 2013  Pedro Lobo <palobo@gmail.com>
--
--	License: GPLv3
--

-- Set default overwrite method for existing comments
-- Will be used if parameter isn't passed via query
-- append, replace or interactive
property defaultOverwrite : "append"
alfred_script("movies archive")

on alfred_script(q)
	
	tell application "Finder"
		
		set fileList to selection
		
		-- Check to see if a overwrite method parameter 
		-- was passed in the the query and use it
		if item 1 of q is "-" then -- Next item will be considered parameter for overwrite method
			
			set appendMethod to item 2 of q
			
			if appendMethod is "d" then
				repeat with theFile in fileList
					my deleteComment(theFile)
				end repeat
				
			else
				
				if item 3 of q is space then
					set theComment to items 4 thru -1 of q as string
				else
					set theComment to items 3 thru -1 of q as string
				end if
				
				if appendMethod is "a" then
					
					repeat with theFile in fileList
						my appendComment(theFile, theComment)
					end repeat
					
					
				else if appendMethod is "r" then
					
					repeat with theFile in fileList
						my replaceComment(theFile, theComment)
					end repeat
					
				else if appendMethod is "i" then
					repeat with theFile in fileList
						my interactiveComment(theFile, theComment)
					end repeat
					
				end if
			end if
			
		else
			
			-- Use default if no parameter was passed
			set theComment to q
			
			if defaultOverwrite is "append" then
				repeat with theFile in fileList
					my appendComment(theFile, theComment)
				end repeat
			else if defaultOverwrite is "replace" then
				repeat with theFile in fileList
					my replaceComment(theFile, theComment)
				end repeat
			else if defaultOverwrite is "interactive" then
				repeat with theFile in fileList
					my interactiveComment(theFile, theComment)
				end repeat
			end if
		end if
		
	end tell
	
end alfred_script


on appendComment(theFile, theComment)
	tell application "Finder"
		if length of (comment of theFile as text) is not 0 then
			set comment of theFile to (comment of theFile & ", " & theComment)
		else
			set comment of theFile to theComment
		end if
		
	end tell
end appendComment

on replaceComment(theFile, theComment)
	tell application "Finder"
		set comment of theFile to theComment
	end tell
end replaceComment

on deleteComment(theFile)
	tell application "Finder"
		
		set comment of theFile to ""
	end tell
end deleteComment

on interactiveComment(theFile, theComment)
	tell application "Finder"
		if length of (comment of theFile as text) is not 0 then
			
			set oldComment to comment of theFile
			
			display dialog ((name of theFile) as string) & " has the following comment: " & oldComment buttons {"Replace", "Skip", "Append"} default button 3 with title "Set Spotlight Comments"
			
			
			if (button returned of result) is "Replace" then
				my replaceComment(theFile, theComment)
				
			else if (button returned of result) is "Append" then
				my appendComment(theFile, theComment)
			end if
		else
			set comment of theFile to theComment
		end if
	end tell
end interactiveComment

--  This program is free software: you can redistribute it and/or modify
--  it under the terms of the GNU General Public License as published by
--  the Free Software Foundation, either version 3 of the License, or
--  (at your option) any later version.
--
--  This program is distributed in the hope that it will be useful,
--  but WITHOUT ANY WARRANTY; without even the implied warranty of
--  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
--  GNU General Public License for more details.
--
--  You should have received a copy of the GNU General Public License
--  along with this program.  If not, see <http://www.gnu.org/licenses/>.