           <-------------------------------Lists------------------------------->                              
bicycles=['trek', 'krek','brek', 'deck']
print(bicycles)

print("-------------------------------------------------------------------")

print("accessing elements in the lists \n")
print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])

print("-------------------------------------------------------------------")

print("using the name and index with title\n") 
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[2].title())
print(bicycles[3].title())

print("-------------------------------------------------------------------")

print("index positions\n")

print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])

print("-------------------------------------------------------------------")

print("reverse index \n")
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])
print(bicycles[-4])

print("-------------------------------------------------------------------")

print("individual values \n")

message = "my first bicylce was"+bicycles[0].title()+"."
print(message)

print("-------------------------------------------------------------------")

print("modyfying the lists \n")

bikes =['Ducati', 'yamha','Harley',"triumph"]
print(bikes)
print(bikes[0])
print(bikes[1])
print(bikes[2])
print(bikes[3])

print("-------------------------------------------------------------------")

print("replacing the name\n")
bikes[0]= 'dogrouh'
print(bikes)

print("-------------------------------------------------------------------")

print("adding the elements \n")

print("-------------------------------------------------------------------")

bikes.append("sunbeam")
print(bikes)

print("-------------------------------------------------------------------")

print("empty lists\n")
bike = []
print(bike)
bike.append("Harley")
bike.append("David")
bike.append("Westin")
bike.append("Hellcat")
bike.append("H")
print(bike)
print("-------------------------------------------------------------------")

print("pop\n")
popped_bike = bike.pop()
print(popped_bike)

print("-------------------------------------------------------------------")

print("Organising lists \n") 
cars = ['chevrolet', 'benz', 'audi', 'ferrari', 'buggatti']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

print("-------------------------------------------------------------------")

print("reverse")
cars.reverse()
print(cars)

print("-------------------------------------------------------------------")

print("Length of the list")
print(len(cars))

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

print("Working with lists \n")

print("----------------------------------------------------------")

sports = ['cricket', 'chess', 'Basketball']
for sport in sports:
    print("The best sports is  "+sport.title()+".")
    
print("----------------------------------------------------------")

cricketers = ['s.t', 'c.k', 'd.b']
print(cricketers)
for cricketer in cricketers:
    print("THe best cricketer is " +cricketer.title()+".")
    print("That was a good on"+cricketer.title()+".")
print("The question was a toughest one")    

print("----------------------------------------------------------")

pizzas = ['pineapple pizza', 'cheese pizza', 'pepperoni pizza', 'macroni pizza'] 
for pizza in pizzas:
    print("My favrite pizza is "+pizza.title()+".")
    print("THe best pizza is "+pizza.title()+".")
print("Tht was good one will eat it next time ," +pizza.title()+".") 

print("----------------------------------------------------------")

print("Numerical lists \n")
print("----------------------------------------------------------")

a = 5
for a in range (1,10):
    print(a)
print("----------------------------------------------------------")

b = 20
for b in range (1,25):
    print(b)
print("----------------------------------------------------------")
              
numbers = list(range(1,10))
print(numbers)

print("----------------------------------------------------------")

even_numbers =list(range(2, 11 , 2))
print(even_numbers)
odd_numbers =list(range(1, 11 , 2))
print(odd_numbers)

print("----------------------------------------------------------")

squares = []

for a in range(1,11):
    square = a ** 2
    squares.append(square)
print(squares)     
cubes = []

for a in range(1,11):
    cube = a ** 3
    cubes.append(cube)
print(cubes)     
    
print("----------------------------------------------------------")
      
#exercises
for a in range(1,20):
    print(a)
print("----------------------------------------------------------")

odd_numbers  = list(range(1,21,2))
print(odd_numbers)

print("----------------------------------------------------------")
for a in range(1,30):
    if a % 3 == 0:
          print(a)
          
print("----------------------------------------------------------")

#Slicing
players = ["Alfa", "Beta", "Charlie", "Delta", "Echo"] 
print(players[0])  
print(players[1])  
print(players[2])  
print(players[3])  
print(players[4])  
print("----------------------------------------------------------")

print(players[0:1])
print(players[0:2])
print(players[0:3])
print(players[0:4])
print("----------------------------------------------------------")

print(players[1:0])
print(players[1:1])
print(players[1:2])
print(players[1:3])
print(players[1:4])
print("----------------------------------------------------------")

print(players[2:0])
print(players[2:1])
print(players[2:2])
print(players[2:3])
print(players[2:4])
print("----------------------------------------------------------")

print(players[3:0])
print(players[3:1])
print(players[3:2])
print(players[3:3])
print(players[3:4])
print("----------------------------------------------------------")

print(players[4:0])
print(players[4:1])
print(players[4:2])
print(players[4:3])
print(players[4:4])
print("----------------------------------------------------------")

# copyinhg the lists
pizzas = ['pineapple pizza', 'cheese pizza', 'pepperoni pizza', 'macroni pizza'] 

my_pizzas = pizzas[:]
print("My pizzas r", my_pizzas)



          
    
    