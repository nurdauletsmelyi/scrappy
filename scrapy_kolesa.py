from urllib.request import urlopen
from urllib.error import HTTPError
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2


cities = ['nur-sultan/']
vl1 = 'https://'
vl2 = 'kolesa.kz/cars/'
main = vl1 + 'kolesa.kz'
urls = []
for city in cities:
    c = vl1 + vl2 + city
    urls.append(c)
print(c)
print(main)

page = requests.get(c)


page_links=[]
for i in range(6): 
    page_link =  c +"?page={}".format(i)
    
    page_links.append(page_link)   
    
print(page_links) 

##cars link 1st pag
links = []
for page_link in page_links: 
    page = requests.get(page_link)
    soup = bs(page.content, 'html.parser')
    for a in soup.find_all('a',class_ = 'list-link ddl_product_link',  href=True):
        links.append(main + a['href'] )
links = set(links)
    #links = '\n'.join(links)
print(links)   

carslist = []
for link in links: 
    #testlink = 'https://kolesa.kz/a/show/121687956'
    r = requests.get(link)
    soup = bs(r.content)
    print(soup.find('h1', class_= 'offer__title').text)
    brand = (soup.find(itemprop='brand').text)
    name = (soup.find(itemprop='name').text)
    year = (soup.find('span', class_ ='year').text)
    price = (soup.find('div', class_='offer__price').text)
    cars = {
        'brand': brand,
        'name': name, 
        'year': year, 
        'price': price
    }
    carslist.append(cars)
print(carslist)


data  = df  
client = pymongo.MongoClient('mongodb+srv://noserzhauyn:<password>@cluster0.m0abm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.db.data
# database
db = client["instashopkz"]
# collection
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y_%H:%M:%S")
company= db[dt_string]

# data = data.reset_index(inplace=True)
data_dict = data.to_dict("records")
# data_dict = {x.replace('.', ' '): v for x, v in data_dict} 
print(data_dict)
company._insert(data_dict, check_keys=False)


# schedule.every(5).minutes.do(job)
# # schedule.every().hour.do(job)
# # schedule.every().day.at('13:58').do(job)
# # schedule.every(5).to(10).minutes.do(job)
# # schedule.every().monday.do(job)
# # schedule.every().wednesday.at("13:15").do(job)
# # schedule.every().minute.at(":17").do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1) # wait one minute     