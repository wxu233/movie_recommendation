from manager import frontController
from manager.objClasses import Movie
from manager.objClasses import WatchList
from manager.objClasses import MovieList
import json

#initializing
moviesList = MovieList.MovieList()
moviesList.loader()
#program start
print('Welcome to MovieGenie')
print(r"""
        _.---.__
      .'        `-.
     /      .--.   |
     \/  / /    |_/
      `\/|/    _(_)
   ___  /|_.--'    `.   .
   \  `--' .---.     \ /|
    )   `       \     //|
    | __    __   |   '/||
    |/  \  /  \      / ||
    ||  |  |   \     \  |
    \|  |  |   /        |
   __\\@/  |@ | ___ \--'
  (     /' `--'  __)|
 __>   (  .  .--' &"\
/   `--|_/--'     &  |
|                 #. |
|                 q# |
 \              ,ad#'
  `.________.ad####'
    `#####""""""''
     `&#"
      &# "&
      "#ba"
                """)
confirm='N'
skip=''
##this loop avoids the user to exit without asking to do so
while confirm=='N':
    ##cleans and loads on each cycle the watchlist
    watchList = WatchList.WatchList()
    watchList.loader()
    resultList=MovieList.MovieList()
    ##asks what is the favourite movie title and searchs it based on similarity
    favourite = input("what is your favourite movie?    ")
    moviesList.searchMovie(favourite,resultList)
    if(len(resultList)==0):
        found=None
    elif(len(resultList)==1):
        found=resultList[0]
        ##prints the movie infos and asks for confirm
        print(str(found))
        confirm= frontController.getYesNo("Is this the movie you told me about? Y/N")
    else:
        resultChoice='0'
        confirmChoice='N'
        while str(confirmChoice).upper()!='Y':
            for movie in resultList:
                print(movie.getTitle()+" (year "+movie.getReleaseDate()+") , code '"+movie.getId()+"'")
            while frontController.intoList(resultList,resultChoice) is not True:
                resultChoice=input("What movie did you meant? input its code to see the details: ")
            chosen=moviesList.getMovie(resultChoice)
            print(str(chosen))
            confirmChoice= frontController.getYesNo("Is this the movie you told me about? Y/N")
            if(confirmChoice=='Y'):
                found=chosen
                confirm='Y'
            else:
                resultChoice='0'
                confirmChoice= frontController.getYesNo("Exit from MovieGenie? Y/N")
                if(str(confirmChoice).upper()=='Y'):
                    found=None
                    skip='Y'
                
    if found is not None:
        if(confirm=='Y'):
            ##duplicates the list of movies, so that, if asked, it can remove from there whatever is inside the watchlist
            ##it's important to use the .copy() method and not the simply =, because otherwise every change done to orderedmoviesList will
            ##be done also to moviesList
            orderedmoviesList=MovieList.MovieList(moviesList)
            print("I'm looking for more movies you could like, give me a bit so i can be sure you won't be complaining.")
            if(len(watchList)>0):
                confirmW= frontController.getYesNo("Want me to avoid considering what's already inside your Watchlist? Y/N    ")
                if(confirmW=='Y'):
                    frontController.removeWatchList(orderedmoviesList,watchList)
            ##scans the entire list setting the rank value according to the evaluation criteria, and then sorts the list
            orderedmoviesList.setPopularityIndexMultithread(found)
            orderedmoviesList.sort(key=lambda x: x.getRank(), reverse=True)
            count=0
            ##initializes the navigation parameters on the top5 lists
            fromRow=0
            toRow=5
            confirmI=""
            ##cycles on the list until told to exit
            while str(confirmI).upper()!="E":
                topList=MovieList.MovieList()
                frontController.printListFromTo(orderedmoviesList,topList,fromRow,toRow,found,watchList)
                ##makes you choose if you want the details about a movie, if you want to see the next 5 or the previous 5 movies or if you want to exit
                ##it's managed with 2 lists so that you can't go backwards if you haven't gone forward onece.
                choichesIStart=['D','N','E','W']
                choichesI=['D','N','P','E','W']
                if fromRow==0:
                    print("Does any of the movies i told you about interest you?")
                    print("TYPE 'D' get details about one of the movies and eventually add it to your watchlist (type 'W' to print it), 'N' to get the next 5 movies, and 'E' to exit")    
                    while confirmI.upper() not in choichesIStart:
                        confirmI= input("")
                else:
                    print("Does any of the movies i told you about interest you?")
                    print("TYPE 'D' get details about one of the movies and eventually add it to your watchlist (type 'W' to print it), 'N' to get the next 5 movies, 'P' to get the previous 5 movies, and 'E' to exit")    
                    while confirmI.upper() not in choichesI:
                        confirmI= input("")
    
                if str(confirmI).upper()=='D':
                    choice=input("Type the code of one of the previous movies, or 'B' in case you don't want anymore    ")
                    check_choice=False
                    first_run=True
                    ##checks the choice or provides the occasion to exit and try again
                    while(check_choice==False):
                        if(first_run==False):
                            choice=input("The code you entered wasn't valid, type the code of one of the previous movies, or 'B' in case you want to go back to the List    ")
                        if(choice.upper()=='B'):
                            #confirm= frontController.getYesNo("Exit from MovieGenie? Y/N")
                            check_choice=True
                            confirmI=""
                        elif(frontController.intoList(topList,choice)==True):
                            check_choice=True
                            print(str(orderedmoviesList.getMovie(choice)))
                            confirmAdd= frontController.getYesNo("Add this movie to your watchlist? Y/N")
                            if confirmAdd=='Y':
                                ##once you add a movie to the watchlist, you go back to the start of the list, without that movie.
                                ##It would be pointless to give you the chance to add it again to the watchlist
                                if(frontController.intoList(watchList,choice)!=True):
                                    watchList.writeWatchList(topList,choice)
                                    print("Ok, the movie is in your watchList, and it has been removed from the list of suggested movies")
                                    
                                else:
                                    print("The movie was already in your watchList, it would have been pointless to add it again. I've removed it from the list of suggested movies")
                                removeWL=MovieList.MovieList()
                                removeWL.append(orderedmoviesList.getMovie(choice))
                                frontController.removeWatchList(orderedmoviesList,removeWL)
                                confirmI=""
                                fromRow=0
                                toRow=5
                            else:
                                check_choice=True
                                confirmI=""
                            #confirm= frontController.getYesNo("Exit from MovieGenie? Y/N")
                        else:
                            first_run=False
                elif str(confirmI).upper()=='N':
                    fromRow+=5
                    toRow+=5
                    confirmI=""
                elif str(confirmI).upper()=='P':
                    fromRow-=5
                    toRow-=5
                    confirmI=""
                elif str(confirmI).upper()=='E':
                    ##case in which the title is not what was wanted
                    confirm= frontController.getYesNo("Exit from MovieGenie? Y/N")
                elif str(confirmI).upper()=='W':
                    if len(watchList)>0:
                        print('------------------------------')
                        print('Watchlist:')
                        print('------------------------------')
                        for watch in watchList:
                            print(str(watch))
                        print('------------------------------')
                    else:
                        print('------------------------------')
                        print('Sorry, your watchlist is empty')
                        print('------------------------------')
                    confirmI=""

    else:
        ##case in which the title wasn't found
        if skip=='Y':
            confirm='Y'
        else:
            print("Sorry i don't know that movie")
            confirm= frontController.getYesNo("Exit from MovieGenie? Y/N")
