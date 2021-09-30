# emptylists
bikes=[]
print(bikes)
bikes.append('ge')
bikes.append('ge')
bikes.append('ge')
bikes.append('ge')
bikes.append('ge')
print(bikes)

# insert

bikes =['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(bikes)

bikes.insert(0, 'r')
print(bikes)

# remove
del bikes[0]
print(bikes)

# pop
bikes = ['a','b','c','d','e','f','g']
print(bikes)

popped_bikes = bikes.pop()
print(popped_bikes)

bikes = ['a','b','c','d','e','f','g']
print('bikes')
popped_bikes = bikes.pop()
print("The fisrt owned bikes was"+popped_bikes.title()+"!")
# removing

bikes.remove('b')