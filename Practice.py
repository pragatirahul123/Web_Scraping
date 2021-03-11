import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint


url=requests.get("https://www.youtube.com/channel/UC0RhatS1pyxInC00YKjjBqQ")
res=url.text
#pprint(res)


soup = BeautifulSoup(res, 'html.parser')
titles = soup.findAll('a', id='video-title') 
#print(titles)

views = soup.findAll( 
            'span', class_='style-scope ytd-grid-video-renderer') 
video_urls = soup.findAll('a', id='video-title') 
print('Channel: {}'.format(url)) 
