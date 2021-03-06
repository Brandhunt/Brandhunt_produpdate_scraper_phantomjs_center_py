#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#  /|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\  
# <   -  Brandhunt Product Update Scraper Module  -   >
#  \|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/

# --- IMPORT SECTION --- #


import json
import os
os.environ['SCRAPERWIKI_DATABASE_NAME'] = 'sqlite:///data.sqlite'
import requests
from requests.exceptions import ConnectionError
import scraperwiki
import time
import traceback

jsonmodprods = []
count = int(os.environ['MORPH_MODULE_NUM_OFFSET'])
maxcount = int(os.environ['MORPH_MODULE_MAXNUM_OFFSET'])
loadedjson = 'HEPP'

orig_offset = os.environ['MORPH_MODULE_OFFSET']
offset_incr = os.environ['MORPH_MODULE_OFFSET_INCR']
offset = orig_offset

while jsonmodprods is not None:
    #for prods in jsonmodprods:
    #    for p_data in prods:
    #        scraperwiki.sqlite.save(unique_keys=['productid'], data=p_data)
    #jsonmodprods = []
    try:
        while loadedjson:
            if loadedjson != 'HEPP':
                #jsonmodprods.append(loadedjson)
                for prod in loadedjson:
                    scraperwiki.sqlite.save(unique_keys=['productid'], data=prod)
                time.sleep(1)
            mod_url = os.environ['MORPH_MODULE_' + str(count) + '_URL'] + offset
            offset = str(int(offset) + int(offset_incr))
            #print('Current offset for module ' + str(count) + ': ' + offset)
            r = requests.get(mod_url)
            loadedjson = json.loads(r.content)
        print('Done importing products from module ' + str(count) + '!')
        count = count + 1
        if count >= maxcount and maxcount > 0:
            break
        offset = orig_offset
        loadedjson = 'HEPP'
    except ConnectionError:
        print('MODULE URL NO LONGER FOUND AT COUNT ' + str(count) + ': STOPPING NOW!')
        jsonmodprods = None
    except:
        print(traceback.format_exc())
