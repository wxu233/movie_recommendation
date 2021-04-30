import datetime
import ast
from manager.objClasses import Resource
class Movie(Resource.Resource):
    ##Method __init__
    ##constructor for object class Movie
    ##builds the Movie Object from the columns of the csv file
    def __init__(self,adult,belongsToCollection,budget,genres,homepage,id,imdbId,originalLanguage,originalTitle,overview,popularity,posterPath,productionCompanies,productionCountries,releaseDate,revenue,runtime,spokenLanguages,status,tagline,title,video,voteAverage,voteCount,cast,crew):
        super( Movie, self ).__init__(title,id)
        self.__adult = adult
        self.__belongsToCollection = belongsToCollection
        self.__budget = budget
        self.__genres = genres
        self.__homepage = homepage
        self.__imdbId = imdbId
        self.__originalLanguage = originalLanguage
        self.__originalTitle = originalTitle
        self.__overview = overview
        self.__popularity = popularity
        self.__posterPath = posterPath
        self.__productionCompanies = productionCompanies
        self.__productionCountries = productionCountries
        self.__releaseDate = releaseDate
        self.__revenue = revenue
        self.__runtime = runtime
        self.__spokenLanguages = spokenLanguages
        self.__status = status
        self.__tagline = tagline
        self.__video = video
        self.__voteAverage = voteAverage
        self.__voteCount = voteCount
        self.__cast = cast
        self.__crew = crew
        self.__rank=0
    ##Getter and setter Methods
    ##standard methods to get singular values and set those to a provide value
    def getAdult(self):
        return self.__adult
    def setAdult(self,adult):
        self.__adult=adult
    
    def getBelongsToCollection(self):
        return self.__belongsToCollection
    def setBelongsToCollection(self,belongsToCollection):
        self.__belongsToCollection=belongsToCollection

    def getBudget(self):
        return self.__budget
    def setBudget(self,budget):
        self.__budget=budget

    def getGenres(self):
        return self.__genres
    def setGenres(self,genres):
        self.__genres=genres

    def getHomepage(self):
        return self.__homepage
    def setHomepage(self,homepage):
        self.__homepage=homepage
    
    def getImdbId(self):
        return self.__imdbId
    def setImdbId(self,imdbId):
        self.__imdbId=imdbId
    
    def getOriginalLanguage(self):
        return self.__originalLanguage
    def setOriginalLanguage(self,originalLanguage):
        self.__originalLanguage=originalLanguage

    def getOriginalTitle(self):
        return self.__originalTitle
    def setOriginalTitle(self,originalTitle):
        self.__originalTitle=originalTitle

    def getOverview(self):
        return self.__overview
    def setOverview(self,overview):
        self.__overview=overview

    def getPopularity(self):
        return self.__popularity
    def setPopularity(self,popularity):
        self.__popularity=popularity

    def getPosterPath(self):
        return self.__posterPath
    def setPosterPath(self,posterPath):
        self.__posterPath=posterPath
    
    def getProductionCompanies(self):
        return self.__productionCompanies
    def setProductionCompanies(self,productionCompanies):
        self.__productionCompanies=productionCompanies

    def getProductionCountries(self):
        return self.__productionCountries
    def setProductionCountries(self,productionCountries):
        self.__productionCountries=productionCountries

    def getReleaseDate(self):
        return self.__releaseDate
    def setReleaseDate(self,releaseDate):
        self.__releaseDate=releaseDate

    def getRevenue(self):
        return self.__revenue
    def setRevenue(self,revenue):
        self.__revenue=revenue

    def getRuntime(self):
        return self.__runtime
    def setRuntime(self,runtime):
        self.__runtime=runtime

    def getSpokenLanguages(self):
        return self.__spokenLanguages
    def setSpokenLanguages(self,spokenLanguages):
        self.__spokenLanguages=spokenLanguages

    def getStatus(self):
        return self.__status
    def setStatus(self,status):
        self.__status=status

    def getTagline(self):
        return self.__tagline
    def setTagline(self,tagline):
        self.__tagline=tagline

    def getVideo(self):
        return self.__video
    def setVideo(self,video):
        self.__video=video

    def getVoteAverage(self):
        return self.__voteAverage
    def setVoteAverage(self,voteAverage):
        self.__voteAverage=voteAverage

    def getVoteCount(self):
        return self.__voteCount
    def setVoteCount(self,voteCount):
        self.__voteCount=voteCount
    
    def getRank(self):
        return self.__rank
    def setRank(self,rank):
        self.__rank=rank

    ##Methods plus and minusRank
    ##these methods aid increasing or decreasing the rank value
    ##used mainly to provide the top5
    def plusRank(self):
        self.__rank+=+1
    def minusRank(self):
        self.__rank-=1

    def getCast(self):
        return self.__cast
    def setCast(self,cast):
        self.__cast=cast
    
    def getCrew(self):
        return self.__crew
    def setCrew(self,crew):
        self.__crew=crew

    ##Method that prints the whole movie info if called the function str() on the movie object
    def __str__(self):
        title="Title: "+super().getTitle()
        oTitle="Original Title: "+self.__originalTitle
        text=""
        adult=""
        if(self.__adult=='True'):
            adult="Rating: Adult Only"
        oLanguage=""
        if(self.__originalLanguage!=""):
            oLanguage=self.__originalLanguage
            
        overview=self.__overview
        
        collection=""
        if(self.__belongsToCollection!=""):
            data = ast.literal_eval(self.__belongsToCollection)
            collection="Collection: "+data['name']
        budget=""
        
        ##the format function is used to print neatly the budget.
        if(int(self.__budget)>0):
            budget="Budget: "+("{:,}".format(int(self.__budget)))
        genres=""
        if(self.__genres!=""):
            data = ast.literal_eval(self.__genres)
            genres+="Genres: "
            for count in range(0,len(data)):
                if count<len(data)-1:
                    genres+=data[count]['name']+", "
                else:
                    genres+=data[count]['name']
        homepage=""
        if(self.__homepage!=""):
            homepage="Website: "+self.__homepage

        prodComp=""
        if(self.__productionCompanies!=""):
            data = ast.literal_eval(self.__productionCompanies)
            prodComp+="Produced by: "
            for count in range(0,len(data)):
                if count<len(data)-1:
                    prodComp+=data[count]['name']+", "
                else:
                    prodComp+=data[count]['name']

        prodCount=""
        if(self.__productionCountries!=""):
            data = ast.literal_eval(self.__productionCountries)
            prodCount+="Produced in these countries: "
            for count in range(0,len(data)):
                if count<len(data)-1:
                    prodCount+=data[count]['name']+", "
                else:
                    prodCount+=data[count]['name']
                    
        release="Release on "+self.__releaseDate
        revenue="Revenue: "+self.__revenue
        ##datetime is used to format it as a readable time format
        runtime="Runtime: "+str(datetime.timedelta(minutes=float(self.__runtime)))

        spoken=""
        if(self.__spokenLanguages!=""):
            data = ast.literal_eval(self.__spokenLanguages)
            spoken+="Spoken Languages: "
            for count in range(0,len(data)):
                if count<len(data)-1:
                    spoken+=data[count]['name']+", "
                else:
                    spoken+=data[count]['name']
        
        status="Status: "+self.getStatus()
        votes="N. of votes: "+self.getVoteCount()
        rating="Average rating: "+self.getVoteAverage()

        cast=""
        if(self.__cast!=""):
            data = ast.literal_eval(self.__cast)
            cast+="Cast: "
            for count in range(0,len(data)):
                if count<len(data)-1:
                    cast+=data[count]['name']+", "
                else:
                    cast+=data[count]['name']
        
        crew=""
        if(self.__crew!=""):
            data = ast.literal_eval(self.__crew)
            crew+="Crew: "
            for count in range(0,len(data)):
                if count<len(data)-1:
                    crew+=data[count]['name']+", "
                else:
                    crew+=data[count]['name']
        ##it's important to keep this format so that it can print every object in the right way
        text=f"""{title}
{oTitle}
{adult}
{oLanguage}
{overview}
{collection}
{budget}
{genres}
{homepage}
{prodComp}
{prodCount}
{release}
{revenue}
{runtime}
{spoken}
{status}
{votes}
{rating}
{cast}
{crew}"""
        return text

    
