from  Web_Scrp_Task1 import*
from Web_Scrp_Task4 import*
from Web_Scrp_Task5 import*
from pprint import pprint



def analyse_movies_genre(movies_list):
    i=0
    list_of_gener=[]
    while i<len(movies_list):
        language=(movies_list[i]['gener'])
        list_of_gener.append(language)
        i=i+1

    all_gener=list_of_gener
    #print(all_genre)

    gener_list=all_gener
    each_gener_list=[]
    for sublist in gener_list:
        for item in sublist:
            each_gener_list.append(item)
    #pprint(each_gener_list)


    main_gener_list=each_gener_list
    i=0
    new_list=[]
    while i<len(main_gener_list):
        j=0
        count=0
        while j<len(main_gener_list):
            if main_gener_list[i]==main_gener_list[j]:
                count=count+1
            j=j+1
        if [main_gener_list[i],count] not in new_list:
            new_list.append([main_gener_list[i],count])
        i=i+1

    main_gener_dic=dict(new_list)
    return(main_gener_dic)

gener_analysis=analyse_movies_genre(get_movie_details)
#pprint(gener_analysis)
