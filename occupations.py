import csv
import random

hi = open("occupations.csv", "rb")
reader = csv.reader(hi)
dic = {}
L = []

def listify(L, readin):
    for occupation in readin:
        L.append(occupation)
    return L[1:len(L)-1]

def addToDict(L,D):
    for item in L:
        D[item[0]] = int(float(item[1]) * 10)
    return D

#out of 998
def modList(dic):
    master = []
    for key in dic:
         master += [key]*dic[key]
    return master

def randomizer(alist):
    random.shuffle(alist)
    return alist[random.randint(0,len(alist)-1)] 

L = listify(L, reader) #list of occ
dic = addToDict(L, dic) #dict
randomVal = randomizer(modList(dic)) #holds random occ

