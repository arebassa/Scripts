from xml.etree import ElementTree as ET
import urllib2
import string
from json import loads as LD
import tempfile as temp
from os import fdopen
import argparse
import requests
#import requests_cache


#affiliate_link = "http://click.linksynergy.com/fs-bin/stat?id=kA8hpmfqRAo&offerid=146261&type=3&subid=0&tmpid=1826&RD_PARM1="
itunes_search ='https://itunes.apple.com/search'

#requests_cache.configure('data_cache')

def list_apps(entity,app,country):
    global itunes_search

    search_terms = {
        'term': app,
        'media':'software',
        'entity':entity,
        'country':country
    }
    r = requests.get(itunes_search, params=search_terms)
    data = r.json()
    return data['results']


def dlicon(url):
    try:
        f = urllib2.urlopen(url)
        (fd, fname)= temp.mkstemp('.png')

        with fdopen(fd, "wb") as local_file:
            local_file.write(f.read())
    except urllib2.HTTPError, e:
        print "HTTP Error:", e.code, url
    except urllib2.URLError, e:
        print "URL Error:", e.reason, url

    return fname


def parse_item(item):
    icon = dlicon(item['artworkUrl60'])
    app_url = urllib2.quote(item['trackViewUrl'] + "?partnerId=30")
    app_url = urllib2.quote(app_url)

    return {
        'uid': item['trackName'],
        'arg': '%s' % (item['trackId']),
        'title': item['trackName'],
        'subtitle': '%s by %s (Price: %s)' % (item['trackName'],
            item['sellerName'],
            item['formattedPrice']),
        'icon': icon
    }


def list():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-m", "--mac", help="Mac App", action="store_const", const="macSoftware")
    group.add_argument("-i", "--ipad", help="iPad App", action="store_const", const="iPadSoftware")
    group.add_argument("-s","--software", action="store_const", const="software")
    parser.add_argument('-c','--country', help = '2 Letter Country Code')
    parser.add_argument('-a','--aff_link',metavar="Affiliate Link", help = 'Your Affiliate Link')
    parser.add_argument('app_name',metavar="App Name", nargs="+",help = 'Type the Apps Name')
    args = parser.parse_args()

    if args.mac:
        entity = args.mac
    elif args.ipad:
        entity = args.ipad
    elif args.software:
        entity = args.software
    else:
        entity = "macSoftware"


    app=urllib2.quote(' '.join(args.app_name))
    country=args.country
    aff_link=args.aff_link

    if (len(app) > 2):
        items = map(lambda x: parse_item(x), list_apps(entity,app,country))
        xml_items = ET.Element('items')
        for item in items:
            xml_item = ET.SubElement(xml_items, 'item')
            for key in item.keys():
                if key is 'uid' or key is 'arg':
                    xml_item.set(key, item[key])
                else:
                    child = ET.SubElement(xml_item, key)
                    child.text = item[key]
        print ET.tostring(xml_items)

if __name__ == '__main__':
    list()
