# myFile = open("movies.txt", "a")
# more = "yes"
# while more.lower()=="yes":
#     movie = input("Please enter a movie title: ")
#     myFile.write(movie + "\n")
#     more = input("Would you like to add another item? Enter 'yes' or 'no'.")
# myFile.close()
text = open("movies.txt", "r").readlines()
search = input("Would you like to search for a movie by entering the position number? (yes/no) >")
if(search.lower() == "yes"):
    position = input("What number is the movie? >")
    print(text[int(position)-1])
else:
    movie = input("What movie do you want to see the position of? >")
    if(movie in text):
        print(text.index(movie+"\n")+1)
    else:
        print(movie+" is not in the directory")
