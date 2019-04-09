import requests
from bs4 import BeautifulSoup
import csv

url='https://www.infibeam.com/Mobiles/search?mobiletype=smart-phone'
res=requests.get(url).text
result=BeautifulSoup(res,"lxml")

with open('infibeam.csv','w',newline='') as f:
    f=csv.writer(f)
    f.writerow(['Title','Url'])
    for title in result.find_all("div",class_="title"):
        get_title=title.a.text
            
        url=title.a.get("href")
        url='https://www.infibeam.com'+url
        
        
        print(get_title)
        print(url)
        f.writerow([get_title,url])
        
            
        
      
        
                
    
    


