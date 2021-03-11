from Web_Scrp_Task5 import *
from pprint import pprint

def analyse_language_and_directors(movie_list):

    directors_dic={}
    for movie in movie_list: 
        for director in movie['director']:
            directors_dic[director] = {}
    #print(directors_dic)


    for i in range(len(movie_list)):
        for director in directors_dic:

            if director in movie_list[i]['director']:
                   for launguage in movie_list[i]['launguage']:
                        directors_dic[director][launguage]=0
    #print(directors_dic)
                
    for i in range(len(movie_list)):
        for director in directors_dic:
            if director in movie_list[i]['director']:
                for launguage in movie_list[i]['launguage']:
                    directors_dic[director][launguage]=+1

    return directors_dic
director_by_language = analyse_language_and_directors(get_movie_details)
#pprint(director_by_language)
