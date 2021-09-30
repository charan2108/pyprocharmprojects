cricketers = ['sachin', 'ck', 'don', 'gav']
for cricketer in cricketers:
    print(cricketer.title()+", is a legend")
    print("the best cricketer of the millnieum is,"+cricketer.title())
    
print("it was a good to know about it")    

# range function
for value in range(1,110):
    print(value)
    
# using range creating numbers
numbers = list(range(0,15))
print(numbers)

# squares
squares = []
for a in range(1,12):
    square = a ** 2
    squares.append(square)
print(squares)
# simple method     
squares = [a ** 2 for a in range(1,12)]
print(squares)
# cubes
cubes = []
for b in range(1,12):
    cube = b ** 3
    cubes.append(cube)
print(cubes)    
cubes=[b**3 for b in range(1,12)]
print(cubes) 
# slicing
bikes=['hero', 'hhellcat','tomcat','hae','harley']
print(bikes[0])
print(bikes[1])
print(bikes[2])
print(bikes[3])
print(bikes[4])
print(bikes[0:4])
print(bikes[0:3])
print(bikes[1:4])
print(bikes[:4])
print(bikes[2:])

for bike in bikes[:3]:
    print(bike.title())
# copying
gamelist=['a','b','c','c']
o_gamelist=gamelist[:]
gamelist.append('g')
o_gamelist.append('g')
print(gamelist)
print(o_gamelist)

print(gamelist)
print(o_gamelist)