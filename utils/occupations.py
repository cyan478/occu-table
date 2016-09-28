import csv
import random

hi = open("data/occupations.csv", "rb")
reader = csv.reader(hi)
dic = {}
L = []
site = ""

def listify(L, readin):
    for occupation in readin:
        L.append(occupation)
    return L[1:len(L)-1]

def addToDict(L,D):
    for item in L:
        sub = []
        sub.append(int(float(item[1]) * 10))
        sub.append(item[2])
        D[item[0]] = sub
    return D

def modList(dic):
    master = []
    for key in dic:
        sub = []
        sub. append([key] + [dic[key][1]])
        master +=  sub * dic[key][0]
    return master

def randomizer(alist):
    random.shuffle(alist)
    chosen = alist[random.randint(0,len(alist)-1)]
    global site 
    site = chosen[1]
    return chosen[0]

L = listify(L, reader) #list of occ
dic = addToDict(L, dic) #dict
#x = modList(dic)
#print x
randomVal = randomizer(modList(dic)) #holds random occ
#print site

