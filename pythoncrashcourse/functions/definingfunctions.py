# defining the function
def Hello():
    print('Welcome to the python')
#calling the function 
Hello()

# passing information to the function 
def Hello(username):
    print("Hello, "+username.title()+"!")   
Hello('Dumbo')    

# Exercise example
def display_message():
    print("Im learning python")
display_message()    

def  fav_book(book):
    print("One of my favorite books is, " +book.title()+"!")
fav_book('David CopperField')  

# Positional Agruements
def cricketer(batsmen_type, batsmen_name):
    print("\n I have a cricketer " +batsmen_type+" !")
    print("\n I have a cricketer " +batsmen_type + "  name is  "+batsmen_name+"!")
    
cricketer('Right Handed Batsmen', 'Rahul Dravid')      
    
#Multiple functions
def cricketer(batsmen_type, batsmen_name):
    print("\n I have a cricketer " +batsmen_type+" !")
    print("\n My Cricketer name is " +batsmen_type + "  name is  "+batsmen_name+"!")
    
cricketer('Right Handed Batsmen', 'Rahul Dravid')     
cricketer('Right Handed Batsmen', 'Sachin Tendulkar')       

# keyword arguements
def cricketer(batsmen_type, batsmen_name):
    print("\n I have a batsmen type  " +batsmen_type+ " .")
    print("I have a allrounder " +batsmen_type+" and the name is  " +batsmen_name.title()+".")
    
cricketer(batsmen_type='allrounder', batsmen_name ='KQ')    

# default values
def cricketer(batsmen_type, batsmen_name='KQ'):
    print("\n i have a cricketer"+batsmen_type+"!")
    print("My fav cricketer is  " +batsmen_type+ "name is " +batsmen_name+"!")
    
cricketer(batsmen_type='right handed batsmen')  

# returning values
def name(first_name, last_name):
    full_name = first_name +'  ' + last_name
    return full_name.title()
cricketer = name('Sachin','Tendulkar')
print(cricketer)

# Arguement Optionals
def name(first_name,middle_name,last_name):
    full_name = first_name +'  '+middle_name+'  '+last_name
    return full_name.title()
cricketer = name('Sachin','Ramesh','Tendulkar')
print(cricketer)

def name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name +' '+middle_name+' '+last_name
    else:
        full_name = first_name +'  '+last_name
    return full_name.title()
cricketer = name('Sachin', 'Tendulkar')
print(cricketer)

cricketer = name('Sachin', 'Ramesh', 'Tendulkar')  
print(cricketer)  

# function in the dictionary that

def person(first_name, last_name):
    person={'first_name':first_name, 'last_name':last_name}
    return person
boxer = person('Muhammad', 'ali')
print(boxer)

def person(first_name, last_name,age=''):
    person={'first_name': first_name, 'last_name': last_name}
    if age:
        person['age'] = age
    return person
boxer = person('Muhamad','Ali', age='27')
print(boxer) 

# passing lists

def users(names):
    for name in names:
           msg = "Hello, " +name.title()+ "!"
           print(msg)
usernames = ['a','b','c','d']
users(usernames)           
 

            