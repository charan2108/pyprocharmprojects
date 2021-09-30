cars = ['audi', 'benz', 'cheverolet', 'etiga','ferrai']
print(cars)
print("\n")
if cars == 'audi':
    print(cars.upper())  
# adding else statement
if cars == 'audi':
    print(cars.upper())
else:
    print(cars)         
    
# checking for inequality
requested_cars = 'mercedes'
if requested_cars != 'ferrari':
    print("Hold the mercedes") 
# checking a user is in banned list or not
banned_users = ['a','b', 'c']
user = 'e'
if user not in banned_users:
    print(user.title() + "  you can post the response or post"+"!") 

# factor to determine the voting age

age = eval(input("Enter your age"))
if age>=18:
    print("Eligible to vote") 
else:
    print("Register to voye when you turn 18")    
    
#School Admission

age = eval(input("Enter your age"))
if age <=12:
    print("The admission is free")
elif age <=18:
    print("The admission cost is 5 $") 
else:
    print("The admision cost is 100$")        
     
     
requested_toppings = ['mushrooms', 'macroni', 'cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'macroni' in requested_toppings:
    print(' Addming macroni')   

print(" added the toppings in the pizza")   
        
pizza_toppings = input("Enter the toppings")
avaialable_toppings = ['mushrooms', 'pepper', 'pepporoni', 'cheese', 'pineapple', 'tomato']
requested_toppings=['mushrooms', 'pepper', 'pepporoni', 'cheese']
for requested_topping in requested_toppings:
    if requested_topping in avaialable_toppings:
        print("Adding " + requested_topping +"!")
    else:
        print("Sorry the requested toppings is not avaialbale!")    
print("\n finished making the requested pizza")        