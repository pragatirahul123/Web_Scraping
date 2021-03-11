from pprint import pprint
from Web_Scrp_Task1 import*
from bs4 import BeautifulSoup
import requests
import json 
import os 


all_movie_dic=Top_Movies
def movie_list(movie):
    details={}
    listUrl=[]
    movieList=movie
    return movieList

movies_detail_list=movie_list(all_movie_dic)
#pprint(movies_detail_list)

listofUrl=[]
for i in movies_detail_list:
    url=i["url"]
    listofUrl.append(url)

def scrape_movie_cast(movie_caste_url):
    movie_id=''
    for _id in movie_caste_url[27:]:
        if '/' not in _id:
            movie_id=movie_id + _id
        else:
            break
    name_file=movie_id+" _cast.json"
    #print(file_name)

    text=None
    if os.path.exists(name_file):
        print("cashing data")
        f=open(name_file)
        text=f.read()
        text=json.loads(text)

        return text
    if text is None:
        #print("Non cashing data")

        row=requests.get(movie_caste_url)
        soup=BeautifulSoup(row.text,"html.parser")

        table_data=soup.find('table',class_='cast_list')
        actors=table_data.find_all('td',class_='')
        cast_list=[]
        for actor in actors:
            actor_dict={}

            imdb_id=actor.find('a').get('href')[6:15]
            name=actor.get_text().strip()
            actor_dict['imdb_id']=imdb_id
            actor_dict['name']=name
            cast_list.append(actor_dict.copy())
        all_director=cast_list
        with open(name_file,"w") as outfile:
            json.dump(all_director,outfile,indent=4)
        return all_director

user_scrp_cast=int(input("movie index:"))
user_of_scrp_cast=(listofUrl[user_scrp_cast-1])
user_url=(str(user_of_scrp_cast))
#pprint(user_url)

print("Movie Name:",movies_detail_list[user_scrp_cast-1]["name"])
main_url=user_url+"fullcredits?ref_=tr_cl_sm#cast"
result=scrape_movie_cast(main_url)
pprint(result)

                