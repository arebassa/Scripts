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
	"""Reads arguments and options and executes accordingly"""
	
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-m", "--mac", help="Mac App", action="store_true")
	group.add_argument("-i", "--ipad", help="iPad App", action="store_true")
	parser.add_argument('app_name', help = 'Type the Apps Name')
	args = 	parser.parse_args()

	if args.mac:
		entity="macSoftware" 	# Searches on for Mac Software
	
	elif args.ipad:
		entity="iPadSoftware"	# Searches only for iPad Software
		
	term=args.app_name			# Get the name of the App
	
	get_link(entity,term)		# Get the App's Affiliate Link
		

def get_link(entity,term):
	"""Generate a correct Affiliate Link"""
	
	global affiliate_link
	global itunes_search
	
	# Limit:1 will return only 1 result, usually the most accurate.
	search_terms = {'term': term, 'media':'software','entity':entity,'limit':1}
	
	r = requests.get(itunes_search, params=search_terms)
	data = r.json()

	app_url = urllib2.quote(data["results"][0]['trackViewUrl'] + "?partnerId=30",'')
	app_url = urllib2.quote(app_url, '')
	# According to documentation, the search result must be percent-encoded TWICE.

	link = affiliate_link + app_url		# Create the final link
		
	setClipboardData(link)				# Copy to clipboard


def setClipboardData(data):
	"""Place data in Mac OS X clipboard."""
	
	p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
	p.stdin.write(data)
	p.stdin.close()
	retcode = p.wait()
	
	print "Link Copied to Clipboard"


if __name__ == "__main__":
	main()
