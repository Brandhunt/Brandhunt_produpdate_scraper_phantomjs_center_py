#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#  /|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\/|\  
# <   -  Brandhunt Product Update Scraper Module  -   >
#  \|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/

# --- IMPORT SECTION --- #

import os
os.environ['SCRAPERWIKI_DATABASE_NAME'] = 'sqlite:///data.sqlite'

import requests
from requests.exceptions import ConnectionError
import json

jsonmodprods = []
count = 1
loadedjson = ''

orig_offset = os.environ['MORPH_MODULE_OFFSET']
offset_incr = os.environ['MORPH_MODULE_OFFSET_INCR']
offset = orig_offset

while jsonmodprods is not None:
    for prods in jsonmodprods:
        for p_data in prods:
            scraperwiki.sqlite.save(unique_keys=['productid'], data=p_data)
    try:
        while loadedjson:
            if loadedjson != '':
                jsonmodprods.append(json.loads(loadedurl.content))
            mod_url = os.environ['MORPH_MODULE_' + str(count) + '_URL'] + offset
            offset = str(int(offset) + int(offset_incr))
            print('Current offset for module ' + str(count) + ': ' + offset)
            r = requests.get(mod_url)
            loadedjson = json.loads(r.content)
        count = count + 1
        offset = orig_offset
        print('Done importing prod. info from module ' + str(count) + '!')
    except ConnectionError:
        print('MODULE URL NO LONGER FOUND AT COUNT ' + str(count) + ': STOPPING NOW!')
        jsonmodprods = None
    except:
        print(traceback.format_exc())
