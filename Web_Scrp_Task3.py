from Web_Scrp_Task1 import *
from Web_Scrp_Task2 import *
from pprint import pprint

def group_by_decade(movies):
    moviedec={}
    list=[]
    for index in movies:
        mod=index%10
        decade=index-mod
        if decade not in list:
            list.append(decade)
    list.sort()
    #print(list)
    for i in list:
        moviedec[i]=[]
    for i in moviedec:
        dec=i+9
        for x in movies:
            if x<=dec and x>=i:
                for v in movies[x]:
                    moviedec[i].append(v)
    return(moviedec)
group_dec=(group_by_decade(year_movie))
#pprint(group_dec)

