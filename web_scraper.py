import requests
from bs4 import BeautifulSoup

#send the mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#system date and time manipulation
import datetime
# import time

now = datetime.datetime.now()

#email content placeholder

content = ' '

#extracting news story

def extract_news(url):
    print("Extracting News. . . ")
    cnt = ' '
    response=requests.get(url)
    content=response.content   
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('h2',attrs={'class':'home-title'})):
        cnt = cnt+ str(i+1) +" : "+tag.text + "\n" 
    return cnt



    #https://thehackernews.com/


cnt=extract_news('https://thehackernews.com')
print(cnt)
# time.sleep(200022)