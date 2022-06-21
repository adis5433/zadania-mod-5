import itertools
import random
from random import randint
from datetime import date


library = []
fliter_by_movies = filter(lambda movie: movie["type of content"] == "movie" ,library)
filter_by_series = filter(lambda serie: serie("type of content") == "serie", library)

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
    def __init__(self,title, year, genre ,seasons = [], season = 0, episode = 0, views = 0,type_of_content = "serie"):
        super().__init__(title, year, genre, views, type_of_content )
        self.seasons = []
        self.episode = str(episode).zfill(2)
        self.season = str(season).zfill(2)
    def __str__(self):
        return f"{self.title} S{self.season}E{self.episode} "
    def add_content_to_library(self):
        content={"Title":self.title,"year of debut":self.year,"genre":self.genre,'seasons':self.seasons,"Views":self.views,"type of content": self.type_of_content}
        library.append(content)



def get_movies():
    movies = filter(lambda movie: movie["type of content"] == "movie" ,library)
    sorted_movies = sorted(movies, key=lambda d: d['Title'])
    return sorted_movies


def get_series():
    series = filter(lambda serie: serie("type of content") == "serie", library)
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

def top_titles(num_of_top_titles : int, content_type = "all"):
    match content_type:
        case "all":
            top_titles = sorted(library, key=lambda d: d['Views'],reverse=True)[0:num_of_top_titles]
            titles = [title["Title"] for title in top_titles]
        case "movies":
            movies = filter(lambda movie: movie["type of content"] == "movie" ,library)
            top_titles = sorted(movies, key=lambda d: d['Views'],reverse=True)[0:num_of_top_titles]
            titles = [title["Title"] for title in top_titles]
        case "series":
            series = filter(lambda serie: serie["type of content"] == "serie", library)
            top_titles = sorted(series, key=lambda d: d['Views'], reverse=True)[0:num_of_top_titles]
            titles = [title["Title"] for title in top_titles]
    return titles


def add_episodes(title ,season: int, num_of_episodes:int,relese_year):
    num_of_season = f"Season {season} (Relese year: {relese_year}) "
    episodes = []
    for episode in range(1, num_of_episodes + 1):
        episodes.append(str(episode).zfill(2))
    full_episode_record = {num_of_season: episodes}
    for i in library:
        if i['Title'] == title:
            i['seasons'].append(full_episode_record)



first_movie=Movie("Doctor Strange:Multiverse of Madness", 2022, "Action")
second_movie = Movie("Pulp Fiction", 1994, "Action")
third_movie = Movie("Alien",1979,"Horror")
first_serie = Series("Scrubs",2001,"Comedy",4,3)
second_serie = Series("Lost",2004,"Adventure",1,11)
third_serie = Series("Firends",1994,"Comedy",3,7)


print(type(second_serie))



first_movie.add_content_to_library()
second_movie.add_content_to_library()
third_movie.add_content_to_library()
first_serie.add_content_to_library()
second_serie.add_content_to_library()
third_serie.add_content_to_library()

print(third_serie)

generate_views()

add_episodes("Scrubs",1,24,2001)

print(top_titles(4))



def top_three_popular_content_for_today():
    today = date.today()
    top_three = top_titles(3, "all")
    print(f"Top 3 most popular content for {today}: "
          f"{top_three}")


if __name__ == "__main__":
    top_three_popular_content_for_today()



#type szczgółowe
#