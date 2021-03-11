from pprint import pprint
from Web_Scrp_Task1 import*
import json
import os



all_movie=Top_Movies
i=0
all_url=[]
all_name=[]
while i < len(all_movie):
    movie_name=all_movie[i]["name"]
    all_name.append(movie_name)
    url=all_movie[i]["url"]
    all_url.append(url)
    i=i+1



user_movie=int(input("enter a movie index :"))
print(all_name[user_movie-1])


def scrape_movie_details(movie_url):

    movie_id=''
    for _id in movie_url[27:]:
        if '/' not in _id:
            movie_id=movie_id+_id
        else:
            break
    name_file=movie_id+" .json"
    #return name_file

    text=None
    if os.path.exists(name_file):
        print("cashing data")
        f=open(name_file)
        text=f.read()
        text=json.loads(text)

        return text
    if text is None:
        print("Non cashing data")
        page=requests.get(movie_url)
        soup=BeautifulSoup(page.text,"html.parser")

        title_div=soup.find('div',class_="title_wrapper").h1.get_text()
        movie_name=" "
        for i in title_div:
            if "(" not in i:
                movie_name=(movie_name+i).strip()
            else:
                break


        sub_div=soup.find('div',class_="subtext")
        runtime=sub_div.find('time').get_text().strip()
        runtime_hours=int(runtime[0])*60
        #movie_runtime=0
        if "min"in runtime:

            runtime_minutes=int(runtime[3:].strip('min'))
            movie_runtime=runtime_hours+runtime_minutes
        else:
            movie_runtime=runtime_hours
        gener=sub_div.find_all("a")
        gener.pop()
        movie_gener=[i.get_text() for i in gener]
        summary=soup.find('div',class_="plot_summary")

        movie_bio=summary.find('div',class_="summary_text").get_text().strip()
        director=summary.find('div',class_="credit_summary_item")
        director_list=director.find_all('a')
        movie_directors=[i.get_text().strip()for i in director_list]

        extra_details=soup.find("div",attrs={"class":"article","id":"titleDetails"})
        list_of_divs=extra_details.find_all('div')
        for div in list_of_divs:
            tag_h4=div.find_all('h4')
            for text in tag_h4:
                if "Language:" in text:
                    tag_anchor=div.find_all('a')
                    movie_language=[language.get_text()for language in tag_anchor]
                elif "Country:" in text:
                    tag_anchor=div.find_all('a')
                    movie_country=''.join([country.get_text() for country in tag_anchor])

        movie_poster_link=soup.find('div',class_="poster").a['href']
        movie_poster="https://www.imdb.com"+movie_poster_link

        movie_detail_dic={"name": '',"director": '',"runtime":'',"bio":'',"gener":'',"language":'' , "country":'',"poster_img_url":''}

        movie_detail_dic["name"]=movie_name
        movie_detail_dic["director"]=movie_directors
        movie_detail_dic["runtime"]=movie_runtime
        movie_detail_dic["bio"]=movie_bio
        movie_detail_dic["gener"]=movie_gener
        movie_detail_dic["language"]=movie_language
        movie_detail_dic["country"]=movie_country
        movie_detail_dic["poster_img_url"]=movie_poster

        #return movie_detail_dic

        file1=open(name_file,"w")
        row=json.dumps(movie_detail_dic)
        file1.write(row)
        file1.close()
        return movie_detail_dic

url=all_movie[user_movie-1]["url"]

movie_details=scrape_movie_details(url)
#pprint(movie_details)
       



