FILENAME = "movies.txt"

def write_movies(movies):
    with open(FILENAME, "w")as file:
     for movie in movies:
         file.write(f"{movies}\n")

def read_movies():
    movies = []
    with open (FILENAME) as file:
        for line in file:
            line = line.replace("\n","")
            movies.append(line)
    return movies

def list_movies(movies):
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie}")
        print()

def add_movie(movies):
    movie = input("Movies: ")
    movies.append(movie)
    write_movies(movies)
    print(f"{mpvie} was added. \n")

def delete_movie(movies):
    index = int(input("Number: "))
    if index < 1 or index > len(movies):
        print("Invalid movie number. \n")
    else:
        movie = movies.pop(index - 1) 
        write_movies(movies)
        print(f"{movie} was deleted. \n")

def display_menu():
    print("The Movie List Program ")
    print()
    print("COMMAND MENU")
    print('list - list all movies')