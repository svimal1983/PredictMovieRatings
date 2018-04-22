# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 00:01:08 2018

@author: svimal
"""
import pandas as pd
import os
import requests
from itertools import chain
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
import simplejson as JSON
import re
# Path where you save the webdriver for windows
executable_path = 'C:/Users/gauta/BIA 660_Notebooks/chromedriver_win32/chromedriver.exe'
# log path
service_log_path = 'C:/Users/gauta/BIA 660_Notebooks/chromedriver_win32/chromedriver'


filenames=[]
path ='D:/Smriti MS/BIA660/Final Project/movieHTML/'
for folders, sub_folders, file in os.walk(path):  
   for name in file:
       if name.endswith(".xls"):           
           filename = os.path.join(folders, name)
           filename=filename.replace("\\","/")
           filenames.append(filename)
       else:
           continue
          
all_data = pd.DataFrame()
for f in filenames:
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)

def exploratoryAnalysis():
    movies=all_data['Name']
    str(all_data)
    all_data.describe()
    all_data.head()
    all_data.tail()
    all_data.isnull().sum()
    all_data=all_data.dropna()  
    
    print(len(all_data.Name.unique()))
    
def processCast():
    uniqueCast=[]
    movie_cast=[]
    castDict={}
    castList = all_data['Cast']
    
    movies=all_data['Name']
   
    for index,movie in movies.iteritems():
        print (movie)
        movie_cast.append((movie)+'==='+str(all_data.loc[all_data['Name'] == movie, 'Cast']))
        
    for index,movieCast in castList.iteritems():
        actors=movieCast.strip('"').split(',')
        i=0
        for actor in actors:
            
            actor=actor.replace('[','').replace(']','')
            actor=actor.replace('\'','')
            actor.strip()
            i=i+1
            if (i==5):
                break
            if(actor not in uniqueCast):
                uniqueCast.append(actor)
            else:
                continue
    #loginToIMDB (uniqueCast)
    # initiator the webdriver for Firefox browser
    
    uniqueCast=['Stanley Baker', 'Jack Hawkins']
    """, 'Ulla Jacobsson', 'James Booth', 'Michael Caine', 'Nigel Green', 'Ivor Emmanuel', 'Paul Daneman', 'Glynn Edwards', 'Neil McCarthy', 'David Kernan', 'Gary Bond', 'Peter Gill', 'Tom Gerrard', 'Patrick Magee', 'Richard Davies', 'Dafydd Havard', 'Denys Graham', 'Dickie Owen', 'Larry Taylor', 'Joe Powell', 'John Sullivan', 'Harvey Hall', 'Gert Van Den Bergh', 'Dennis Folbigge', 'Kerry Jordan', 'Ronald Hill', 'Chief Buthelezi', 'Daniel Tshabalala', 'Ephraim Mbhele', 'Simon Sabela', 'David Kerman', 'Richard Burton']
"""
    idList=[]
    for cast in uniqueCast:
         # send a request
         print(cast.strip())
         # initiator the webdriver for Firefox browser
         driver = webdriver.Chrome(executable_path=executable_path, service_log_path=service_log_path)               
         # Wait to let webdriver complete the initialization
         driver.wait = WebDriverWait(driver, 5)
         driver.get('http://u01.unigraph.rocks/?q=%7B%0A++subjects(property%3A+%22label%22%2C+text%3A+"'+cast.strip()+'"%2C+lang%3A+%22en%22)+%7B%0A++++uid%0A++++date_of_birth%0A++++label.en%0A++++url%0A++++imdb_id+%40propagate%0A++++instance_of(filter%3A+%22%240+%3D%3D+%6012f97bdf%60%22)+%40propagate%0A++%7D%0A%7D%0A')
         try:
            runButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'run')))
            runButtonFound=driver.find_element_by_id('run')
            runButtonFound.click()
            
            responseScreen = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'response')))
            responseFound=driver.find_element_by_xpath('//*[@id="response"]')
            driver.wait = WebDriverWait(driver, 10)
            response1=responseFound.get_attribute('innerHTML')
            actorID='NA'
            imdb_id=[]
            imdb_id=re.findall(r'\bnm\w+', response1)
            print (imdb_id)
            if(imdb_id):
                actorID=imdb_id[0]
            idList.append(actorID)
            driver.quit()
         except TimeoutException:
            print ("Taking too much time")              
         
    
def loginToIMDB(actorList):
    
    
    # send a request
    driver.get('https://secure.imdb.com/ap/signin?clientContext=130-7482126-9519763&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.imdb.com%2Fap-signin-handler&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=imdb_pro_us&openid.mode=checkid_setup&siteState=eyJvcGVuaWQuYXNzb2NfaGFuZGxlIjoiaW1kYl9wcm9fdXMiLCJyZWRpcmVjdFRvIjoiaHR0cDovL3Byby1sYWJzLmltZGIuY29tLz9yZj1jb25zX25iX2htJnJlZl89c3BsX3N0a3loZHJfbG9naW4ifQ&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&imdbPageAction=login')
    #movie_menu = driver.find_elements_by_id("#movieMenu")
    #print (movie_menu)
    # check if the link can be clicked
    username='gautam.vikas.83@gmail.com'
    passwordText="city@ide1"
    try:
        amazonLogIn=WebDriverWait(driver, 10).until(\
                    expected_conditions.element_to_be_clickable((By.ID,'auth-lwa-button')))
   
        amazonLogIn.click()
    
        try:
            myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ap_email')))
        except TimeoutException:
            print ("Taking too much time")

        
        #find and fill the password box
        email=driver.find_element_by_id('ap_email')
        email.send_keys(username)


        #find and click the login button
        password=driver.find_element_by_id('ap_password')
        password.send_keys(passwordText)
        button=driver.find_element_by_id('signInSubmit')
        button.click()  
        
        try:
            myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'searchField')))
            if myElem:
                print('Search button found')
                for actorName in actorList[0]:
                    myElem.send_keys(actorName)
                    hiddenlist=driver.find_element_by_id('instantSearch')
                    actorLists=hiddenlist.findAll('li')
                    elem=actorLists[1]
                    try:
                        actorFound = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'searchField')))
                        elem.click()
                    except:
                        print ('actor not found')
                        
                    
                    
                    
                    
        except TimeoutException:
            print ("Taking too much time")
            
    except TimeoutException:
        print("Unable to Login")
    

        
    
