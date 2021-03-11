import requests
from pprint import pprint
from bs4 import BeautifulSoup
from Web_Scrp_Task1 import *



def group_by_year(movies):
    years=[]
    for i in movies:
        year=i["year"]
        if year not in years:
            years.append(year)
    movie_dict={i:[] for i in years}
    for i in movies:
        year=i["year"]
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(i)
    return(movie_dict)


#pprint(group_by_year(Top_Movies))

year_movie=group_by_year(Top_Movies)
#pprint(year_movie)



