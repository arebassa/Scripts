#!/usr/bin/env python
#coding: UTF-8

#
# Author: Pedro Lobo <palobo@gmail.com>
# License: GPLv3
#
####################################################################################
#
# A simple script to generate App Store Affiliate Link for the provided as argument.
# More details regarding Affiliate Linking and Search API can be found at:
# http://www.apple.com/itunes/affiliates/resources/documentation/linking-to-the-itunes-music-store.html
# http://www.apple.com/itunes/affiliates/resources/documentation/itunes-store-web-service-search-api.html
#

import requests
import sys
import urllib2
import subprocess
import argparse


### Set some variables needed for the script to work.

# Set your affiliate link here.
affiliate_link = "http://click.linksynergy.com/fs-bin/stat?id=kA8hpmfqRAo&offerid=146261&type=3&subid=0&tmpid=1826&RD_PARM1="
itunes_search ='https://itunes.apple.com/search'


def main():
	
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-m", "--mac", help="Mac App", action="store_const", const="macSoftware")
	group.add_argument("-i", "--ipad", help="iPad App", action="store_const", const="iPadSoftware")
	group.add_argument("-s","--software", action="store_const", const="software")
	parser.add_argument('-n','--num',metavar="N",help="Number of results to display",type=int,default=1)
	parser.add_argument('-l','--link',help='Format markdown links',action='store_true')
	parser.add_argument('app_name',metavar="App Name", nargs="+",help = 'Type the Apps Name')
	args = 	parser.parse_args()

	if args.mac:
		# Searches on for Mac Software
		entity=args.mac 					
	
	elif args.ipad:
		# Searches only for iPad Software
		entity=args.ipad					
		
	elif args.software:
		# Search for iOS software?? Unclear from documentation
		entity=args.software				
		
	# Get the name of the App
	app=args.app_name		
	
	# Get the maximum number of results to return
	limit=args.num
	
	# Get the App's Affiliate Link
	result = getLink(entity,app,limit)		
		
	if args.link:
		# Generate Markdown style links
		link=markdownLink(result)	
				
	else:
		# Get simple list of links
		link=simpleLink(result)				
	
	# Copy the result to clipboard
	setClipboardData(link)					



def getLink(entity,app,limit):
	"""Generate a correct Affiliate Link"""

	global itunes_search
	
	search_terms = {'term': app, 'media':'software','entity':entity,'limit':limit}
	r = requests.get(itunes_search, params=search_terms)
	data = r.json()
	
	if data["resultCount"] != 0:
		
		app_data={}
		for entry in data["results"]:
			app_url = urllib2.quote(entry['trackViewUrl'] + "?partnerId=30")
			app_url = urllib2.quote(app_url)
			# According to documentation, the search result must be percent-encoded TWICE.

			app_data[entry["trackCensoredName"]]=app_url
		
		return app_data
		
	else:
		print 'No matches found for "%s"' %(app[0])
		exit()


def markdownLink(data):
	"""Return a markdown formated string with name and URL"""
	global affiliate_link
	link=""
	for name in data:
		link=link+"[%s](%s)\n\n" %(name,affiliate_link + data[name])
	return link

	
def simpleLink(data):
	"""Return a simple string with the results"""
	global affiliate_link
	link=""	
	for name in data:
		link=link + affiliate_link + data[name]+"\n\n"
	return link


def setClipboardData(data):
	"""Place data in Mac OS X clipboard."""
	p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
	p.stdin.write(data)
	p.stdin.close()
	retcode = p.wait()
	print "Link Copied to Clipboard"


if __name__ == "__main__":
	main()