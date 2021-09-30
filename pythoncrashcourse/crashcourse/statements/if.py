cars =['audi', 'benz','chevrolet','ford']

for car in cars:
    if car == 'audi':
        print(car.upper())
    else:
        print(car.title())    

# simple if condtion
 
num = 1
print("num == 1 gives the condition", num==1)
if num == 1:
    print("the block is executed")
print("condition ends")    

# if else
num = 1
print("num == 1 gives hte condition", num==1)
if num == 1:
    print("if statements  are executed")
else:
    print("else statements is execuuted")  
    
# checking the values in the list
banned_users = ['a','b', 'c']
user = 'delta'
if user not in banned_users:
    print(user.title()+" you are free to post")
else:
    print("no access")
    
#if elif else
print("Enter the number from  0 to 4 ")
x=int(input("enter number"))
if x == 0:
    print("the value entered is:", x)
elif x == 1:
    print("the value entered is:", x)
elif x == 2:
    print("the value entered is:", x)
elif x == 3:
    print("the value entered is:", x)
elif x == 4:
    print("the value entered is:", x)
else:
    print("the value is out of range")    

# positive o negative number
# positive o negative number

x = int(input("Enter the number"))

if(x<0):
    print("the number is negative")
else:
    print("the number is positive")  

# username validation
user_name ="deltas"
x = input("enter the username")
if user_name == x:
    print("user name is valid")
else:
    print("username not valid")    
    
    
# multiple conditions

requested_toppings = ['pepperoni', 'mushroom']

if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if  'cheese' in requested_toppings:
    print("adding chese") 
if 'mushroom' in requested_toppings:
    print("Adding mushrooms")
    
print(" \n finished adding on pizza ")     

requested_toppings = ['pepperoni', 'mushroom']

if 'pepperoni' in requested_toppings:
    print("Adding perrporoni")
elif 'mushrooms' in requested_toppings:
    print("adding mushrooms")
else:
    print("None")        
    
# Aliens game
alien_color = ['green', 'yellow', 'red']
input("enter the alien_color")
if alien_color =='green':
    print("The player got 8 points")
elif alien_color == 'yellow':
    print("The player got  4 points")
elif  alien_color == 'red':
    print("the player got two pints")        
else:
    print("no points")
 
# aliens_color = ['green', 'yellow', 'red']
# input("Enter the alien_color")
# if 'green' in aliens_color:
#     print("the player got 8 points")
# elif 'yellow' in aliens_color:
#     print("the player got 4 points")
# elif 'red' in aliens_color:
#     print("the player got 2 points")
# else:
#     print("the player got no points")             
  
# greats numbers
x = int(input("Enter the  first number"))
y = int(input("Enter second number"))

if x>y:
    print("Biggest number is", x)
else:
    print("Biggest number is", y) 
       
  
x = int(input("Enter the first number :"))
y = int(input("Enter the first number :"))
z = int(input("Enter the first number :"))

if x>y:
    print("The biggest number is", x)
elif y>z:
    print("the biggest number is", y) 
else:
    print("the biggest number is", z)             
    
       
password = input("Create a Password ")
print("Welcome to the Portal")    
password_check = input("Enter the  password")

if password_check == password:
    print("Password check successful, Welcome Back") 
else:
    print("Invalid password")    
    

      
               
               
               
    
 
        
    
  
    