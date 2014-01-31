# TaskPaper Bundle for MailMate

[Download](http://d.pr/f/cgwG), uncompress and place `TaskPaper.mmBundle` in `/Applications/MailMate.app/Contents/SharedSupport/Bundles`

## Usage
Simply select an email and hit ^⇧A. There are two options:

1. Send to Frontmost;
2. Send to Default.

### Send to Frontmost
This will create a task (email subject) and a note (message:// url) inside a project named Inbox (this needs to exist). If TaskPaper isn’t open, the script will open it and therefore, the last active document will be the destination for the task.

### Send to Default  
This will create a task (email subject) and note (message:// url) in a document of your choosing. There are 3 possible variables which need to be set: 

**TaskPaper Path:**  

	defaults write com.freron.MailMate MmDefaultTaskPaperPath -string "/Users/pedro/Dropbox/Apps/TaskAgent"

**TaskPaper File:**  

	defaults write com.freron.MailMate MmDefaultTaskPaperFile -string "Work.taskpaper"

**TaskPaper Project:**  
The projecy where the task will be created. It can be any of your hoosing and it doesn’t require adding the semicollons.

	defaults write com.freron.MailMate MmDefaultTaskPaperProject -string "Inbox"

You just need to set these once. If you want/need to change any default, then simply issue a new defaults write.