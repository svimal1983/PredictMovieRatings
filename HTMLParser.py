# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 01:01:16 2018

@author: svimal

"""
from bs4 import BeautifulSoup
import pandas as pd
import os
from urllib.request import urlopen
import glob

def collectData(rootDir,folderName):
    masterList = set(['On Disc/Streaming','In Theaters','Genre','Rating','Directed By','Written By','Box Office','Runtime','Studio'])
    dictInfo={}
    name=[]
    critic_rating =[]
    audience_rating=[]
    rating=[]
    genre=[]
    director=[]
    writer=[]
    box_office=[]
    run_time=[]
    studio=[]
    intheatres=[]
    ondiscstreaming=[]
    streamingOptions=[]
    casts=[]
    release_year=[]
    critic_reviews=[]
    audience_reviews=[]
  
    fileList = glob.glob("D:\\Smriti MS\\BIA660\\Final Project\\movieHTML\\"+folderName+"\\*.html")
    for f in fileList:
       castSet=[]
       attributeList=set()
       valueList=[]
       streamingOpts=[]
       #fileName = os.path.join(rootDir, f)
       #fileName = fileName.strip('\'"')
       html =urlopen('file:'+f).read()
       #html =urlopen('https://www.rottentomatoes.com/m/love_simon').read()
       soup = BeautifulSoup(html,"lxml") # parse the html
       title = soup.select('h1.title')[0].text.strip()
       year = soup.select('h1.title span')[0].text.strip()
       if year:  
           yearCln=year
       else: 
           yearCln='NA'
       release_year.append(yearCln)
       finalTitle = "".join(title.rsplit(year))
       criticRating,audienceRating = 'NA'
        
       movieName = finalTitle
       print(movieName)
       criticRatingElem = soup.select("#tomato_meter_link")
       audRatingElem = soup.find("div",{'class':'audience-score'})
       #print (audRatingElem)
       if len(audRatingElem)>0 and (audRatingElem.div.text!='No Score Yet'): 
                audienceRating = audRatingElem.span.text.replace('%','').strip()
       if (len(criticRatingElem)>0):
                criticRating = criticRatingElem[0].text.replace('%','').strip()
       critic_rating.append(criticRating)
       audience_rating.append(audienceRating)
       name.append(movieName)
       
       #movie_info =soup.findAll('li', {'class':'meta-row clearfix'})
       #infoDiv = soup.findAll('li',{'class':'meta-row clearfix'})   
       infoDiv=soup.findAll('li', {'class': ['meta-row clearfix','js-theater-release-dates']})
       #valueDivs = info.findAll ('div',{'class':'meta-value'})
       for info in infoDiv:
           #print (info)
           attribute=''
           attrValues=''
           attrs = info.find('div',{'class':'meta-label'})
           values = info.find('div',{'class':'meta-value'})
           attribute = attrs.text.strip().replace(':','')
           #print (attrs)
           attrValues=values.text.replace('\n','').strip()
           attrValues=' '.join(attrValues.split())
           attributeList.add(attribute)           
           valueList.append(attrValues) 
           if attribute=='Genre':
                    genre.append(attrValues)
           elif attribute =='Rating':
                    rating.append(attrValues)
           elif attribute == 'Directed By':
                    director.append(attrValues)
           elif attribute == 'Written By':
                    writer.append(attrValues)
           elif attribute == 'Box Office':
                    box_office.append(attrValues)
           elif attribute == 'Runtime':
                    run_time.append(attrValues)
           elif attribute == 'Studio':
                    studio.append(attrValues)
           elif attribute == 'In Theaters':
                    intheatres.append(attrValues)
           elif attribute == 'On Disc/Streaming':
                    ondiscstreaming.append(attrValues)
       missingInfo = masterList-attributeList
       #print (missingInfo)
       if (missingInfo)!=set():
                for attribute in missingInfo:
                        if attribute=='Genre':
                            genre.append('NA')
                        elif attribute =='Rating':
                            rating.append('NA')
                        elif attribute == 'Directed By':
                            director.append('NA')
                        elif attribute == 'Written By':
                            writer.append('NA')
                        elif attribute == 'Box Office':
                            box_office.append('NA')
                        elif attribute == 'Runtime':
                            run_time.append('NA')
                        elif attribute == 'Studio':
                            studio.append('NA')
                        elif attribute == 'In Theaters':
                            intheatres.append('NA')
                        elif attribute == 'On Disc/Streaming':
                            ondiscstreaming.append('NA')
            
       #streaming options
       streaming_opts = soup.find('div',{'class':'movie_links'})
       streamingName='NA'
       streamingStr=[]
       if (streaming_opts):
           streamList = streaming_opts.findAll('a')
           
           for streamOpt in streamList:
             tmp = streamOpt.get('href')
             streamingName=tmp.split('//')[1].split('.')[1]
             streamingStr.append(streamingName)
       else:
            streamingStr.append(streamingName)
            
        #   print (opt.get('onclick'))#,{'attribute':'onclick'}))
       
       streamingOptions.append(streamingStr)
       
       
       castList=soup.find_all('div',{'class':'cast-item'})
       for cast in castList:
           castName=cast.span.text
           if castName:
               castName=castName.strip()
           castSet.append(castName)
       casts.append(castSet)
       
       movAudReviews=[]
       movCriticReviews=[]   
       
       audience_revs = soup.find('section',{'id':'audience_reviews'})
       if audience_revs: reviews = audience_revs.findAll('p',{'class':'comment'})
       if reviews:
           
           for review in reviews:
               if review:
                   #print(review.text)
                   movAudReviews.append(review.text.strip())
       else:
           movAudReviews.append('NA')
       audience_reviews.append(movAudReviews) 
       
       critic_revs = soup.find('section',{'id':'contentReviews'})
       if critic_revs: criticreviews = critic_revs.findAll('div',{'class':'review_quote'})
       if criticreviews:
           for creview in criticreviews:
               if creview:
                   #print(creview.p.text)
                   movCriticReviews.append(creview.p.text.strip())
       else:
            movCriticReviews.append('NA')
       critic_reviews.append(movCriticReviews)    
            
           
    
    dictInfo['Cast']=casts
    dictInfo['Audience_Reviews']=audience_reviews
    dictInfo['Critic_Reviews']=critic_reviews
    dictInfo['StreamingOptions']=streamingOptions
    dictInfo['Audience_Rating']=audience_rating    
    dictInfo['Name']=name   
    dictInfo['Critic_Rating'] = critic_rating
    dictInfo['Genre'] = genre
    dictInfo['Rating'] = rating
    dictInfo['Director'] = director
    dictInfo['Writer'] = writer
    dictInfo['Box_Office'] = box_office
    dictInfo['Studio'] = studio
    dictInfo['Run_Time'] = run_time
    dictInfo['In_Theaters_Date']=intheatres
    dictInfo['On_Disc_Streaming']=ondiscstreaming
    dictInfo['Release_Year']=release_year
    
    final_df = pd.DataFrame.from_dict(dictInfo)
    excelName='movie'+folderName+'.xls'
    final_df.to_excel('D:/Smriti MS/BIA660/Final Project/movieHTML/'+folderName+'/'+excelName)
    print (folderName+'DONE')
#if __name__=='__main__':



if __name__ == "__main__": 
    dictFolder={}
    dictFolder[0]='0-10'
    dictFolder[1]='11-20'
    dictFolder[2]='21-30'
    dictFolder[3]='31-40' 
    dictFolder[4]='41-50'
    dictFolder[5]='51-60'
    dictFolder[6]='61-70'
    dictFolder[7]='71-80'
    dictFolder[8]='81-90'
    dictFolder[9]='91-100'
    
    for key in dictFolder.keys():
        collectData('D:/Smriti MS/BIA660/Final Project/movieHTML/',dictFolder[key])
            
        
