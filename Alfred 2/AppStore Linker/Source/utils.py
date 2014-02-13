import urllib2
from json import loads as LD
from os import fdopen
import argparse
from subprocess import Popen, PIPE

# Set the appropriate affiliate link
affiliate_link = "http://click.linksynergy.com/fs-bin/stat?id=kA8hpmfqRAo&offerid=146261&type=3&subid=0&tmpid=1826&RD_PARM1="


def setClipboardData(data):
    """Place data in Mac OS X clipboard."""
    p = Popen(['pbcopy'], stdin=PIPE)
    p.stdin.write(data.encode('utf8'))
    p.stdin.close()
    retcode = p.wait()
    

def markdownLink(id):
    global affiliate_link
    
    url = 'https://itunes.apple.com/lookup?id=%s' %(id)
    response = urllib2.urlopen(url)
    response_items = response.read()
    data = LD(response_items)['results'][0]
    app_url = urllib2.quote(data['trackViewUrl'] + "?partnerId=30")
    app_url = urllib2.quote(app_url)
    link = "[%s](%s)" % (data["trackName"], affiliate_link + app_url)
    setClipboardData(link)
    
    
def simpleLink(id):
    global affiliate_link
    
    url = 'https://itunes.apple.com/lookup?id=%s' %(id)
    response = urllib2.urlopen(url)
    response_items = response.read()
    data = LD(response_items)['results'][0]
    app_url = urllib2.quote(data['trackViewUrl'] + "?partnerId=30")
    app_url = urllib2.quote(app_url)
    link=affiliate_link + app_url
    setClipboardData(link)
    
def main():
    pass
    
if __name__ == '__main__':
    main()