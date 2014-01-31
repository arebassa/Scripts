#!/usr/bin/osascript
set theSubject to (system attribute "MM_SUBJECT")
set theNote to "message://%3c" & (system attribute "MM_MESSAGE_ID") & "%3e"

tell application "System Events"
    set tpRunning to (count of (every process whose name is "TaskPaper")) > 0
end tell

if not tpRunning then
    tell application "TaskPaper"        
        activate
    end tell
end if

tell application "TaskPaper"
    tell front document
        tell project named "Inbox"
            make new entry with properties {name:theSubject, entry type:task type}
            tell task named theSubject
                make new entry with properties {name:theNote, entry type:note type}
            end tell
        end tell
    end tell
end tell