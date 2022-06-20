import itertools
import random
from random import randint



library = []


class Movie:
    def __init__(self, title, year, genre, views = 0,type_of_content = "movie"):
        self.title = title
        self.year = year
        self.genre = genre
        self.views = views
        self.type_of_content = type_of_content
    def add_content_to_library(self):
        content={"Title":self.title,"year of debut":self.year,"genre":self.genre,"Views":self.views,"type of content": self.type_of_content}
        library.append(content)
    def play(self, times_of_play=1):
        self.views += times_of_play
        return self.views
    def __str__(self):
        return f"{self.title} ({self.year})"

class Series(Movie):
    def __init__(self,title, year, genre , season = 0, episode = 0, views = 0,type_of_content = "serie"):
        super().__init__(title, year, genre, views, type_of_content )
        self.episode = str(episode).zfill(2)
        self.season = str(season).zfill(2)
    def __str__(self):
        return f"{self.title} S{self.season}E{self.episode} "


def get_movies():
    movies = filter(lambda movie: movie["type of content"] == "movie" ,library)
    sorted_movies = sorted(movies, key=lambda d: d['Title'])
    return sorted_movies


def get_series():
    series = filter(lambda serie: serie["type of content"] == "serie", library)
    sorted_series = sorted(series, key=lambda d: d['Title'])
    return list(sorted_series)


def search():
    searched_title = input("Give me title of search serie or movie...")
    found_title = filter(lambda title: title["Title"].lower() == searched_title.lower() ,library)
    return list(found_title)

def generate_views():
    for _ in range (10):
        random_title=random.choice(library)
        random_title["Views"] += randint(1,100)
    return random_title

def top_titles(num_of_top_titles : int, content_type : str):
    match content_type:
        case "all":
            top_titles = sorted(library, key=lambda d: d['Views'],reverse=True)[0:num_of_top_titles]
        case "movies":
            movies = filter(lambda movie: movie["type of content"] == "movie" ,library)
            top_titles = sorted(movies, key=lambda d: d['Views'],reverse=True)[0:num_of_top_titles]
        case "series":
            series = filter(lambda serie: serie["type of content"] == "serie", library)
            top_titles = sorted(series, key=lambda d: d['Views'], reverse=True)[0:num_of_top_titles]
    return top_titles




first_movie=Movie("Doctor Strange:Multiverse of Madness", 2022, "Action")
second_movie = Movie("Pulp Fiction", 1994, "Action")
third_movie = Movie("Alien",1979,"Horror")
first_show = Series("Scrubs",2001,"Comedy",4,3)
second_show = Series("Lost",2004,"Adventure",1,11)


second_movie.play()



first_movie.add_content_to_library()
second_movie.add_content_to_library()
third_movie.add_content_to_library()
first_show.add_content_to_library()
second_show.add_content_to_library()




generate_views()



print(top_titles(3, "series"))

print(library)


