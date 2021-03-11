from Web_Scrp_Task1 import *
from Web_Scrp_Task4 import *
from pprint import pprint

NumberOfMovie=int(input("enter of movie:"))
all_movie_dic=Top_Movies
def movie_list(movie):
    details={}
    listUrl=[]
    movieList=movie
    return movieList

movies_detail_list=movie_list(all_movie_dic[:NumberOfMovie])


listofUrl=[]
for i in movies_detail_list:
    url=i["url"]
    listofUrl.append(url)
data_of_movie_list=[]

i=0
while i<len(listofUrl):
    movie_details=scrape_movie_details(listofUrl[i])
    data_of_movie_list.append(movie_details)
    i=i+1

get_movie_details=data_of_movie_list
#pprint(get_movie_details)

# def get_movie_list_details( movie_list):
#     movies_detail_list=[]
#     for i in movie_list:
#         detail=scrape_movie_details(i["url"])
#         movies_detail_list.append(detail)
#     return movies_detail_list

# get_movie_details=get_movie_list_details(Top_Movies)
# pprint(get_movie_details)










    
