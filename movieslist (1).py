# creating a list of movie

movies = ["IRONMAN","I","CARS","MIRAI","FREEGUY"]
print(movies)

# add a movie in the 3rd position
movies.insert(2,"THOR")
print(movies)

# removing an 1 movies from the list
movies.remove("I")
print(movies)

# sorting the list
movies.sort()
print("sorted list", movies)

movies.reverse()
print("reverse list", movies)

# modify the list
movies[3]= "AVENGERS"
print(movies)