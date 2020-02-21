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

mod_url = os.environ['MORPH_MODULE_1_URL']
r = requests.get(mod_url)
jsonmodprods = json.loads(r.content)

count = 2
while jsonmodprods:
    for prod in jsonmodprods:
        scraperwiki.sqlite.save(unique_keys=['productid'], data=prod)
    try:
        mod_url = os.environ['MORPH_MODULE_' + str(count) + '_URL']
        r = requests.get(mod_url)
        jsonmodprods = json.loads(r.content)
        count = count + 1
    except ConnectionError:
        jsonmodprods = None
