favourite = []
ratings = []
movie = 0
while quit != "n":
    quit = input("Would you like to quit? y or n")
    if quit == "y":
        movie = input("What is one of your favourite movies?)")
        rating = input("What did you rate the movie?")
        ratings.append(rating)
        favourite.append(movie)
        x = len(movie)
print ("Thanks! You added", x, " movies to the list!")

