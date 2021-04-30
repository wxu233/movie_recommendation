from difflib import SequenceMatcher
from manager.objClasses import WatchList

import ast
import os
import csv
##time and datetime have been used to choose the best solution, measuring the execution time
##of the method used to rank the movies
import time
import datetime




##Method removeWatchList
##input param movieList,watchList
##remove the movies contained into the watchList from the movieList
def removeWatchList(movieList,watchList):
    if(len(watchList)>0):
        #print(len(movieList))
        for listed in watchList:
            for movie in movieList:
                if(str(movie.getId())==str(listed.getId())):
                    movieList.remove(movie)
        #print(len(movieList))




##Method getYesNo
##input param string
##util method that obliges you to answer with a Y or N.
##Loops until receiving one of those two
def getYesNo(string):
    inputString=None
    while (inputString!='Y' or inputString !='N'):
        inputString=input(string+"    ")
        inputString.upper()
        if(inputString.upper()=='Y' or inputString.upper()=='N'):
            return inputString.upper()




##Method intoList
##input param topList,choice
##checks if the choice value checks with any of the list's id
##if so returns True. It uses the ValueError exception to avoid being stuck
##in case it tries to convert a string
##works both for movies and worklist since both have a getId() method
##and Worklist is just a compact version of the movie object
def intoList(objList,choice):
    try:
        for obj in objList:
            #print("Test"+movie.getId())
            if((int(str(obj.getId()).strip())==int(choice.strip()))):
                return True
    except ValueError:
        return False

##Method printListFromTo
##input param list,topList,lineStart,lineEnd
##scans the list from the lineStart row to the lineEnd row and 
##fills the lineStart list with those elements
##in case it tries to convert a string
def printListFromTo(orderedmoviesList,topList,lineStart,lineEnd,found,watchList):
    count=0
    elemStart=0
    if(lineStart==0):
        elemStart=1
    else:
        elemStart=lineStart
    print("Top "+str(elemStart)+"-->"+str(lineEnd))
    for movie in orderedmoviesList:
        if(movie.getId()==found.getId()):
            if(intoList(watchList,found.getId())!=True):
                count+=1
                if count>=lineStart:
                    print(repr(movie)+" (your favourite movie, it's not in the watchlist)")
                    topList.append(movie)
        else:
            count+=1
            if count>=lineStart:
                print(repr(movie))
                topList.append(movie)
        
        if count == lineEnd:
            break


