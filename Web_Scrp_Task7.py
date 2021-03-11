
from Web_Scrp_Task1 import*
from Web_Scrp_Task4 import *
from Web_Scrp_Task5 import*
from pprint import pprint


def analyse_movies_directors(movies_list):
    i=0
    director_list=[]
    while i<len(movies_list):
        language=(movies_list[i]["director"])
        director_list.append(language)
        i=i+1

    all=director_list
    #pprint(all)

    var=all
    new_list=[]
    for sublist in var:
        for item in sublist:
            new_list.append(item)
    #pprint(new_list)



    char_list=new_list
    i=0
    new_list_new=[]
    while i<len(char_list):
        j=0
        count=0
        while j<len(char_list):
            if char_list[i]==char_list[j]:
                count=count+1
            j=j+1
        if [char_list[i],count] not in new_list_new:
            new_list_new.append([char_list[i],count])
        i=i+1
    Main_dict=dict(new_list_new)
    return (Main_dict)

director_analysis=analyse_movies_directors(get_movie_details)
#pprint(director_analysis)






