# lists
print("Lists")
print("-------------------------------------------------------------------")
books = ['h.p', 'LOR', 'SH', 'Monnstome']
# priniting bookd
print(books)
print(type(books))
print(id(books))
print("-------------------------------------------------------------------")
# Accessing Elements
print("my fav book is ", books[0].title())
print("my fav book is ", books[0].upper())
print("my fav book is ", books[0].lower())
# indexing
print(books[0])
print(books[1])
print(books[2])
print(books[3])

print("-------------------------------------------------------------------")

# Accessing Elements
code = ("My fav book is", books[0].title())
print(code)
print("-------------------------------------------------------------------")
friends = ['haryy','frodo', 'same','argon','legolas','gimli']
print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])
print("my fav friend is", friends[3].title())
print("greetings", friends[0].title())
print("greetings", friends[1].title())
print("greetings", friends[2].title())
print("greetings", friends[3].title())
print("greetings", friends[4].title())
print("greetings", friends[4].upper())
print("greetings", friends[4].lower())
print("--------------------------------------------------------------  ")
# modifying the list
print("modifying the lists \n")
bikes = ['honda', 'cbz', 'harley', 'Honda', 'triumph']
print(bikes)
bikes[0] = 'ducati'
print(bikes)
# adding bikes
print("adding bikes\n")
bikes = ['honda', 'cbz', 'harley', 'Honda', 'triumph']
bikes.append('ducati')
print(bikes)
# inserting the list into the Elements
print("inserting the bike into the list \n")
bikes = ['honda', 'cbz', 'harley', 'Honda', 'triumph']
bikes.insert(0, 'kwasaki')
print(bikes)
print("----------------------------------------------------------")
print("Empty lists \n")
bike = []
bike.append('Harley')
bike.append('Honda')
bike.append('DUcati')
bike.append('f15')
print(bike)

del bike[0]
print(bike)
print("----------------------------------------------------------")

# popped method
print("pop method \n")
bikes = ['honda', 'cbz', 'harley', 'Honda', 'triumph']
print(bikes)
popped_bikes = bikes.pop()
print(popped_bikes)
print("----------------------------------------------------------")
bikes = ['honda', 'cbz', 'harley', 'Honda', 'triumph']
last_owned = bikes.pop(3)
print("My last owned bike was , "+ last_owned.title() +"." )

print("----------------------------------------------------------")
