import requests
from pprint import pprint
from bs4 import BeautifulSoup
from Web_Scrp_Task1 import *



def scrape_movie_details(movie_url):
    page=requests.get(movie_url)
    soup=BeautifulSoup(page.text,'html.parser')
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

    gener=sub_div.find_all('a')
    gener.pop()
    movie_gener=[i.get_text()for i in gener]
    summary=soup.find("div",class_="plot_summary")
    movie_bio=summary.find('div',class_='summary_text').get_text().strip()

    director=summary.find('div',class_="credit_summary_item")
    director_list=director.find_all("a")
    movie_directors=[i.get_text().strip()for i in director_list]
    extra_details=soup.find('div',attrs={"class":"article","id":"titleDetails"})
    list_div=extra_details.find_all('div')
    for div in list_div:
        tag_4=div.find_all('h4')
        for text in tag_4:
            if "Language:" in text:
                tag_anchor=div.find_all('a')
                movie_launguage=[launguage.get_text() for launguage in tag_anchor]
            elif "Country:" in text:
                tag_anchor=div.find_all('a')
                movie_country=''.join([country.get_text() for country in tag_anchor])
    movie_poster_link=soup.find('div',class_="poster").a["href"]
    movie_poster="https://www.imdb.com" + movie_poster_link
    movie_detail_dic={}

    movie_detail_dic['name']=movie_name
    movie_detail_dic['director']=movie_directors
    movie_detail_dic['bio']=movie_bio
    movie_detail_dic['runtime']=movie_runtime
    movie_detail_dic['gener']=movie_gener
    movie_detail_dic['launguage']=movie_launguage
    movie_detail_dic['country']=movie_country
    movie_detail_dic['poster_img_url']=movie_poster_link
    return movie_detail_dic


user_url=int(input("enter a url choice : "))
correct_url=Top_Movies[user_url-1]["url"]
moviedetail=scrape_movie_details(correct_url)

#pprint(moviedetail)













       






