from manager.objClasses import Resource
import os
import csv
class WatchList(list):
    ##Method initWatchList
    ##loads the watchlist from the csv, building every time the WatchList object
    def loader(self):
        __location__ = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        with open(os.path.join(__location__,'files/watchList.csv'), mode="r", encoding="UTF-8",newline="\n") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            line_count = 0
            for line in csv_reader:
                if line_count>0 and line!='':
                    tmp_watchList=Resource.Resource(line[0],line[1])
                    self.append(tmp_watchList)
                line_count=line_count+1
            #print(f'Processed {line_count} lines.')
    ##Method writeWatchList
    ##input param topList,choice
    ##provides the top5 list from which it writes onto the watchlist csv the
    ##choosen movie, which id is in the choice param
    def writeWatchList(self,topList,choice):
        __location__ = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        with open(os.path.join(__location__,'files/watchList.csv'), mode='a', encoding="UTF-8", newline="\n") as watchList_file:
            movie_writer = csv.writer(watchList_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            for movie in topList:
                if (movie.getId()==choice):
                    movie_writer.writerow([movie.getTitle(),movie.getId()])
                    tmp_watchList=Resource.Resource(movie.getTitle(),movie.getId())
                    self.append(tmp_watchList)

        
    
