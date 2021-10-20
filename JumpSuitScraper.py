#!/usr/bin/env python
# coding: utf-8

# In[85]:


import re
import csv
import pandas as pd
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver= webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.shoppersstop.com/search?text=jumpsuits')

def data(i):
    
    final = []

    #Present Division
    divi = driver.find_element(By.XPATH,f'//li[@data-pageid][{i}]')
    
    #Product Name
    try:
        productname = divi.find_element(By.XPATH,'.//div[@class="pro-name"]').text
    except:
        productname = ' '

    #URL
    try:
        url = divi.find_element(By.XPATH,'.//div[@class="pro-info"]/a').get_attribute("href")
    except:
        url = ' '
    
    #Brand Name
    try:
        brandname = divi.find_element(By.XPATH,'.//div[@class="Brand-name"]').text
    except:
        brandname = ' '

    #Price
    try:
        prod = divi.find_element(By.XPATH,'.//div[@class="price"]').text
        temp = re.findall(r'\d+', prod)
        price = list(map(int, temp))
        price = price[0]
    except:
        price = ' '
    
    #Image URL
    try:
        image = divi.find_element(By.XPATH,'.//img').get_attribute("data-src")
    except:
        image = ' '


    final = [productname,url,brandname,price,image]
    
    return final


def main():
    
    #Get Data
    dat = []
    try:
        for i in range(1,207):
            dat.append(data(i))
    except:
        pass
    
    #Using Pandas
    df = pd.DataFrame(dat)
    df.to_csv("JumpSuit.csv",index=False,header=["ProductName", "URL",  "Brand" ,"Price" , "ImageURL"])
      
    #Using CSV
    with open('ShoppersJumpsuit.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(dat)
        
if __name__ == "__main__":
    main()

