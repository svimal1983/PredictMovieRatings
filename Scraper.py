
import time
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.common.keys import Keys

#WebScraper for Project

"""
def unNestList(df,target_col,colName):
    temp = df.apply(lambda x: pd.Series(x[target_col]),axis=1).stack().reset_index(level=1, drop=True) 
    temp.name=colName
    
    return temp 
"""

def retrieveMovieHTML(streamingMoviesList):
    for movieUrl in streamingMoviesList:
        html=None
        try:
            #movieUrl = 'https://www.rottentomatoes.com/m/sherlock_gnomes'
            rootDir = 'D:/Smriti MS/BIA660/Final Project/movieHTML/'
            fileName = movieUrl.split('/')[4]+".html"
            print(movieUrl)
            filePath_Name = rootDir+(fileName)
            file,header = urllib.request.urlretrieve(movieUrl,filePath_Name)
            
            #response=requests.get(movieUrl,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
            #if file:
            #   html= open(filePath_Name) # get the html
            
            
        except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
            print ('failed attempt',fileName,e)
            time.sleep(2) # wait 2 secs
    return rootDir
				
		
        
    
    

# Path where you save the webdriver for windows
executable_path = 'C:/Users/gauta/BIA 660_Notebooks/chromedriver_win32/chromedriver.exe'

# log path
service_log_path = 'C:/Users/gauta/BIA 660_Notebooks/chromedriver_win32/chromedriver'

# initiator the webdriver for Firefox browser
driver = webdriver.Chrome(executable_path=executable_path, service_log_path=service_log_path)

# Wait to let webdriver complete the initialization
driver.wait = WebDriverWait(driver, 5)

# send a request
driver.get('https://www.rottentomatoes.com/browse/dvd-streaming-all?minTomato=91&maxTomato=100&services=amazon;hbo_go;itunes;netflix_iw;vudu;amazon_prime;fandango_now&genres=1;2;4;5;6;8;9;10;11;13;18;14&sortBy=release')
#movie_menu = driver.find_elements_by_id("#movieMenu")
#print (movie_menu)
# check if the link can be clicked
try:
        
        
        #movie_menu_link=WebDriverWait(driver, 10).until(\
        #            expected_conditions.element_to_be_clickable((By.ID,'movieMenu')))
   
        #movie_menu_link.click()
    
        #print('clicked')
        movieList=[]
        movies_browse_All=[]
        streamingMoviesList=[]
        countDiv = driver.find_element_by_id('count-link')
        displayedCount = countDiv.text.strip()
        totalCount = countDiv.text.strip()
        #movies = driver.find_elements_by_css_selector('div.mb-movie div.poster_container a')
        #for movie in movies:
        #    movieList.append(movie.get_attribute('href'))
        browse_all=driver.find_elements_by_css_selector('ul.nav-stacked li a')[4]
        browse_all.click()
        # check if the link can be clicked
        try:
            body = driver.find_element_by_css_selector('body')
            more_path = ('div#show-more-btn button')
            # This waits up to 15 seconds before throwing a TimeoutException 
            # unless it finds the clickable element to return within 10 seconds.
            more_link=WebDriverWait(driver, 10).until(\
                    expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, more_path)))
   
        # click the link
            while (more_link):
                # page down
                body.send_keys(Keys.PAGE_DOWN)
                #sleep; wait until pages to be loaded
                time.sleep(2)
                more_link.click()
                print (countDiv.text)
                
            
        except(RuntimeError):
            print("something wrong with more link")
            #driver.quit()
        movies_browse_All = driver.find_elements_by_css_selector('div.mb-movie div.poster_container a')    
        for smovie in movies_browse_All:
                streamingMoviesList.append(smovie.get_attribute('href'))         
   
    
except(RuntimeError):
        print("something wrong")
#print (streamingMoviesList)
rootDir = retrieveMovieHTML(streamingMoviesList)


#tmp1 = unNestList(df,'Genre','Genre')
#tmp2 = unNestList(df,'Director','Director')
#tmp3 = unNestList(df,'Writer','Writer')
#tmp4 = unNestList(df,'Studio','Studio')
#new_df=df.drop('Genre',axis=1).drop('Director',axis=1).drop('Writer',axis=1).drop('Studio',axis=1).join(tmp1).join(tmp2).join(tmp3).join(tmp4)

"""

if __name__=='__main__':
    movieList=['https://www.rottentomatoes.com/m/black_panther_2018','https://www.rottentomatoes.com/m/sherlock_gnomes']
    fetchMovieInfo(movieList)
"""
