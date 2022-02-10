# Auto-Headers-Maker
This code will help you make a 'requests headers' to a dictionary in python.

Replace the string = ''' request headers ''' 
Then run the code.



It will automatically copy the full format for scraping the a website. Like importing beautifulSoup, requests, pandas. 

Make the requests headers a json. 

Like:-
input: string = ''' x: y
cookie: sdfhsd,
user-agent : shsdf'''


output:
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests as req

headers = {
'x': 'y',
'cookie':'sdfhsd',
'user-agent':'sdsdf'
}


link = ''   # input the link you want to scrape, here
r = req.get(link,headers = headers)
soup = bs(r.content,'html.parser')
print(soup)
