#!/usr/bin/env python3

import requests

x = requests.get('https://www.google.com')

if x.status_code == 200:
 print('yay Loading case -1!')
else:
 print('uh-oh Loading case -1!')
