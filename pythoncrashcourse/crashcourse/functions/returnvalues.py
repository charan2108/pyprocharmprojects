def name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()
cricketer = name('Sachin', 'Tendulkar')
print(cricketer)

# optional arguements

def name(first_name, middle_name ,last_name):
    full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()
cricketer = name('Sachin', 'Ramesh' ,'Tendulkar')
print(cricketer)

# using the conditions

def name(first_name ,last_name ,middle_name='' ):
    if middle_name:
        full_name = first_name+" "+ middle_name+" "+ last_name
    else:
        full_name = first_name+" "+ last_name
    return full_name.title()
cricketer = name("Sachin", "Tendulkar") 
print(cricketer)
cricketer = name("Sachin", "Ramesh" ,'Tendulkar')
print(cricketer)   

# return dictionary

def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

shooter = build_person('Jackson', 'Michael')
print(shooter)


def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
shooter = build_person('Jackson', 'Michael', age='27')
print(shooter)

