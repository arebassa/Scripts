#!/bin/bash
#
# Copyright: (C) 2012  Pedro Lobo <palobo@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.



## Variables ##
TPDIR="/Users/pedro/Dropbox/Notes/Tasks"	# Path to location of TaskPaper Files
TPFILE=$1	# TaskPaper File
TPSEARCH=$2	# Search string to input into Taskpaper


$(open ${TPDIR}/${TPFILE})
sleep 1
exec osascript << EOF
tell application "TaskPaper"
	set the search field string of front document to "$2"
end tell

EOF
