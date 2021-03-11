import requests
from bs4 import BeautifulSoup
url="https://codewithharry.com"

#1. step get the httml

r=requests.get(url)
htmlContent=r.content
#print(htmlContent)

#2.parse html
soup=BeautifulSoup(htmlContent)
#print(soup.prettify)
#print(type(soup))



title=soup.title
#print(type(title))

p=soup.find_all('p')
#print(p)
print(soup.find('p'))
print(soup.find('p')['class'])


ac=soup.find_all('a')
all_links=set()
for link in ac:
    if (link !="#"):
        linkText=("https://codewithharry.com" + link.get("href"))
        all_links.add(link)
        print(linkText)

