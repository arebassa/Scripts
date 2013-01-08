#!/usr/bin/env python
#coding: UTF-8

import requests
import sys
import urllib2
import subprocess
import argparse



affiliate_link = "http://click.linksynergy.com/fs-bin/stat?id=kA8hpmfqRAo&offerid=146261&type=3&subid=0&tmpid=1826&RD_PARM1="
itunes_search ='https://itunes.apple.com/search'


def main():
	
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-m", "--mac", help="Mac App", action="store_true")
	group.add_argument("-i", "--ipad", help="iPad App", action="store_true")
	parser.add_argument('app_name', help = 'Type the Apps Name')
	args = 	parser.parse_args()

	if args.mac:
		entity="macSoftware"
	
	elif args.ipad:
		entity="iPadSoftware"
		
	term=args.app_name
	
	get_link(entity,term)
		

def get_link(entity,term):
	
	global affiliate_link
	global itunes_search
	
	
	payload = {'term': term, 'media':'software','entity':entity,'limit':1}
	
	r = requests.get(itunes_search, params=payload)
	data = r.json()

	appURL = urllib2.quote(data["results"][0]['trackViewUrl'] + "?partnerId=30",'')

	link = affiliate_link + appURL
	
	setClipboardData(link)


def setClipboardData(data):
	p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE) 
	p.stdin.write(data) 
	p.stdin.close() 
	retcode = p.wait()


if __name__ == "__main__":
	main()
