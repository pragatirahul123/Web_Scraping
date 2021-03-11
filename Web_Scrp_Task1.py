import requests
from pprint import pprint
from bs4 import BeautifulSoup


response = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
res =response.text
# print(res)
soup = BeautifulSoup(res, 'html.parser')




def scrape_top_list():

    results = soup.find('div',class_="lister")
    res1=results.find('tbody',class_='lister-list')
    #print(res1)
    ts=res1.find_all('tr')
    #print(ts)
    list_name=[]
    list_year=[]
    list_rating=[]
    list_position=[]
    list_link=[]
    position=1

    for trs in ts:
        list_position.append(position)
        position +=1


        name=trs.find("td",class_= "titleColumn")
        list_name.append(name.a.get_text().strip())


        year=trs.find('span',class_="secondaryInfo")
        list_year.append(year.get_text().strip())


        rating=trs.find("td",class_= "ratingColumn imdbRating") 
        list_rating.append(rating.get_text().strip())


        link=trs.find("td" ,class_= "titleColumn")
        link1=trs.find("a")
        list_link.append(link1.get("href"))
        
    Main_list=[]
    i=0
    for x in list_name:
        Dict={}
        Dict["name"] = list_name[i]
        list_year[i]=list_year[i][1:5]
        Dict["year"] = int(list_year[i])
        Dict["position"]=list_position[i]
        Dict["rating"]=float(list_rating[i])
        Dict["url"]="https://www.imdb.com" + list_link[i]
        Main_list.append(Dict)
        i=i+1
    return Main_list



Top_Movies=scrape_top_list()
#pprint(Top_Movies)









