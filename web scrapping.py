#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests
from bs4 import BeautifulSoup
flipkart_url="https://www.flipkart.com/womens-clothing/pr?sid=2oq,c1r"
req=requests.get(flipkart_url)
content=req.content
print(content)
soup=BeautifulSoup(content,"html.parser")
all_categories=soup.find_all("div",{"class":"fonts-loaded"})
for flipkart in all_categories:
    category_name=flipkart.find({"class":"fonts-loaded"}).text
    print(category_name)
type="application/Id+json"

