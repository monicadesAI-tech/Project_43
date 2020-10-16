#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Installing Library
#pip install requests
#pip install beautifulsoup4



# Basic Web-Scraping Concepts

import requests
import bs4

# Task: Formatting messy and un-structured HTML code using URL provided by user
url = input("Enter URL: ")
response = requests.get(url)

#print(type(response))
#print(response.text)

filename = "New_Scraped_Contents.html"
bs = bs4.BeautifulSoup(response.text,"html.parser")

formatted_text = bs.prettify()
#print(formatted_text)

# Saving the formatted HTML Code in a file
with open(filename,"w+") as f:
    f.write(formatted_text)
    
# Finding Number of images present on website page
list_imgs = bs.find_all('img')
#print(list_imgs)

no_of_imgs = len(list_imgs)

# Finding Number of Anchor Tags/hyperlinks present on website page
list_as = bs.find_all('a')
no_of_as = len(list_as)

print("Number of Images :",no_of_imgs)
print("Number of Anchor Tags :",no_of_as)

# https://www.onlyjavatech.com
# https://www.techsoftindia.co.in

