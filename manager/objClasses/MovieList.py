from manager.objClasses import Movie
from difflib import SequenceMatcher
import threading
import os
import csv
import ast
class MovieList(list):
    ##Method initWatchList
    ##loads the watchlist from the csv, building every time the WatchList object
    def loader(self):
        __location__ = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        with open(os.path.join(__location__,'files/movies.csv'), "r", encoding="UTF-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for line in csv_reader:
                if line_count>0:
                    tmp_movie=Movie.Movie(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25])
                    self.append(tmp_movie)
                line_count=line_count+1
            #print(f'Processed {line_count} lines.')

    ##Method searchMovie
    ##input param movieList,title
    ##the input title is searched into the list by similarity with a coefficent of
    ##0.8, so to return the whole movie object
    def searchMovie(self,title,resultList):
        for movie in self:
            orTitle=movie.getTitle()
            if (( SequenceMatcher(None,str(title).upper(),str(orTitle).upper()).ratio()>0.8) or ((str(title).upper() in str(orTitle).upper()))):
                resultList.append(movie)

    ##Method getMovie
    ##input param moviesList,idFound
    ##method that returns the movie which id is in
    ##the idFound param from the movieList
    def getMovie(self,idFound):
        for movie in self:
            if movie.getId()==idFound:
                return movie

    
    ##Method setPopularityIndexMultithread
    ##input param listMovies,foundMovie
    ##gives a rank to every movie in the listMovies, increasing the rank value
    ##using the object method plusRank() considering different parameters
    ##this method, instead of setPopularityIndex, considers every criteria as a different thread,
    ##defining them as inner methods inside setPopularityIndexMultithread 
    ##and executing them simultaneously instead of one by one, managing them as threads for each movie
    def setPopularityIndexMultithread(self,foundMovie):
        row=0
        #then = time.time()
        def inner_budget(thisMovie,foundMovie):
            #budget
            #print("budget")
            if(foundMovie.getBudget()==thisMovie.getBudget()):
                thisMovie.plusRank()
        
        def inner_popularity(thisMovie,foundMovie):
            #popularity
            #print("popularity")
            if(foundMovie.getPopularity()==thisMovie.getPopularity()):
                thisMovie.plusRank()
        
        def inner_language(thisMovie,foundMovie):
            #original language
            #print("language")
            if(foundMovie.getOriginalLanguage()==thisMovie.getOriginalLanguage()):
                thisMovie.plusRank()
        
        def inner_adult(thisMovie,foundMovie):
            #adult
            #print("adult")
            if(foundMovie.getAdult()==thisMovie.getAdult()):
                thisMovie.plusRank()
        
        def inner_vote(thisMovie,foundMovie):
            #voteAverage
            #print("vote")
            maxVote=int(round(float(foundMovie.getVoteAverage())*100))+1
            minVote=int(round(float(foundMovie.getVoteAverage())*100))-1
            if(float(thisMovie.getVoteAverage())>=minVote and float(thisMovie.getVoteAverage())<=maxVote):
                thisMovie.plusRank()

        def inner_genres(thisMovie,foundMovie):
            #genres
            #print("genres")
            dataThis = ast.literal_eval(thisMovie.getGenres())
            dataIn = ast.literal_eval(foundMovie.getGenres())
            for countIn in range(0,len(dataIn)):
                for countThis in range(0,len(dataThis)):
                    if(dataIn[countIn]['id']==dataThis[countThis]['id']):
                        thisMovie.plusRank()

        def inner_prodCompany(thisMovie,foundMovie):
            #getProductionCompanies
            #print("prodcomp")
            dataThis = ast.literal_eval(thisMovie.getProductionCompanies())
            dataIn = ast.literal_eval(foundMovie.getProductionCompanies())
            for countIn in range(0,len(dataIn)):
                for countThis in range(0,len(dataThis)):
                    if(dataIn[countIn]['id']==dataThis[countThis]['id']):
                        thisMovie.plusRank()

        def inner_cast(thisMovie,foundMovie):
            #cast
            #print("cast")
            if(thisMovie.getCast() is not None and thisMovie.getCast()!=''):
                dataThis = ast.literal_eval(thisMovie.getCast())
                if(foundMovie.getCast() is not None and foundMovie.getCast()!=''):
                    dataIn = ast.literal_eval(foundMovie.getCast())
                    for countIn in range(0,len(dataIn)):
                        for countThis in range(0,len(dataThis)):
                            if(dataIn[countIn]['name']==dataThis[countThis]['name']):
                                thisMovie.plusRank()

        def inner_director(thisMovie,foundMovie):               
            #print("director")
            thisCrew=foundMovie.getCrew()
            if(thisCrew is not None and thisCrew != ''):
                if(thisMovie.getCrew() is not None and thisMovie.getCrew()!=''):
                    #print(thisMovie.getTitle()+" ("+thisMovie.getId()+")")
                    x=getDirectorFromCrew(thisCrew)
                    #print(x)
                    y=getDirectorFromCrew(thisMovie.getCrew())
                    #print(y)
                    if(x==y):
                        #print("compare")
                        thisMovie.plusRank()
        ##Method getDirectorFromCrew
        ##input param crew
        ##loops onto the crew ast to get the one with the role of Director
        def getDirectorFromCrew(crew):
            data = ast.literal_eval(crew)
            for count in range(0,len(data)):
                if(data[count]['job']=="Director"):
                    return data[count]['name']

        for thisMovie in self:
            #if(thisMovie.getId()!=foundMovie.getId()):
            inner_threads = list()
            inner_threads.append(threading.Thread(name="Budget",target=inner_budget, args=(thisMovie,foundMovie,)))
            inner_threads.append(threading.Thread(name="Popularity",target=inner_popularity, args=(thisMovie,foundMovie,)))
            inner_threads.append(threading.Thread(name="Language",target=inner_language, args=(thisMovie,foundMovie,)))
            inner_threads.append(threading.Thread(name="Adult",target=inner_adult, args=(thisMovie,foundMovie,)))
            inner_threads.append(threading.Thread(name="Vote",target=inner_vote, args=(thisMovie,foundMovie,)))
            inner_threads.append(threading.Thread(name="Genres",target=inner_genres, args=(thisMovie,foundMovie,)))
            inner_threads.append(threading.Thread(name="Company",target=inner_prodCompany, args=(thisMovie,foundMovie,)))
            inner_threads.append(threading.Thread(name="Cast",target=inner_cast, args=(thisMovie,foundMovie,)))
            inner_threads.append(threading.Thread(name="Director",target=inner_director, args=(thisMovie,foundMovie,)))
            for cur_thread in inner_threads:
                cur_thread.start()
            for cur_thread in inner_threads:
                cur_thread.join()
            row+=1
            print("Analyzing: "+str(row)+"/"+str(len(self)),end="\r")
        #now = time.time()
        #print("It took: ", str(datetime.timedelta(seconds=(now-then))), " seconds")

        
    
            
    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

