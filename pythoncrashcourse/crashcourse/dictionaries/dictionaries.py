# simple dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
# accessing the values of dictionary
print(alien_0['color'])
print(alien_0['points'])
# adding the new key value pairs to the dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# empty dictionary
alien_0 = {}
alien_0['color'] = 'blue'
alien_0['points'] = 10
print(alien_0)
# modifying the dictionaries
alien_0 ={'color': 'yellow'}
print("the modified  color is:"+alien_0['color']+"!")
alien_0 ={'color': 'green'}
print("the modified  color is:"+alien_0['color']+"!")

alien_0 = {'x_position':0, 'y_position':0, 'speed':'medium'}
print("Orginal position is:"+str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2 
else:
    increment   = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(str(alien_0['x_position']))  

# looping trough key values
   
user_0 = {
       'name': 'Kirloskar',
       'fName': 'Kidnapper',
       'lName': 'kid',
   }

for key,value in user_0.items():
    print("\nKey:", key)
    print("\nValue", value)
    