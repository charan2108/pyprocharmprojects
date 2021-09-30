for x in range(1,11):
    print(x)

# list of numbers

numbers = list(range(1,100))
print(numbers)
print("\n evennumbers")
# even numbers
even_numbers = list(range(2,50,2))
print(even_numbers)
print("\n oddnumbers")

# oddnumbers
odd_numbers = list(range(1,50,2))
print(odd_numbers)

# squares
squares=[]
for a in range(1,12):
    square = a**2
    squares.append(square)
print(squares)    

squares = []
for a in range(1,10):
    squares.append(a**2)
                  
print(squares)    
#cubes

cubes = []
for a in range(1,12):
    cube = a**3
    cubes.append(cube)
print(cubes)     

cubes = []
for a in range(1,12):
    cubes.append(a**3)
print(cubes)    