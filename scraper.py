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
while jsonmodprods is not None:
    for prod in jsonmodprods:
        scraperwiki.sqlite.save(unique_keys=['productid'], data=prod)
    try:
        mod_url = os.environ['MORPH_MODULE_' + str(count) + '_URL']
        r = requests.get(mod_url)
        jsonmodprods = json.loads(r.content)
        count = count + 1
        if count == 6:
            count = 7
    except ConnectionError:
        print('MODULE URL NO LONGER FOUND AT COUNT ' + count + ': STOPPING NOW!')
        jsonmodprods = None
    except:
        print(traceback.format_exc())
