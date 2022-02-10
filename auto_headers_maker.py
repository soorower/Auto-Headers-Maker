a = 'import pandas as pd' + '\n'+ 'from bs4 import BeautifulSoup as bs'+'\n'+'import requests as req'

string = '''sc_apikey: 391D75C6-01EE-463C-8B51-47B2748F8ACD
exhibitorIds: 65871
pageId: 9bb4ebe0-c60d-4071-8d23-487926e85222'''

k = ''
s = string.split('\n')
for i in s:
    if i[0] == ':':
        n = i[1:].split(':')
        i = "'" + n[0].strip() + "':" + f"'{n[1].strip()}'"
        k = k+ '\n' + i + ','
    else:
        n = i.split(':')
        i = f"'{n[0].strip()}':'{n[1].strip()}'"
        k = k + '\n' + i + ','


b = 'headers = {' + '\n'+ k + '\n'+ '}'
c = "link = ''"
d = 'r = req.get(link,headers = headers)'+'\n'+ "soup = bs(r.content,'html.parser')"
e = 'print(soup)'

import pyperclip
pyperclip.copy(a + '\n'+ b + '\n'+ c + '\n' + d + '\n'+ e)