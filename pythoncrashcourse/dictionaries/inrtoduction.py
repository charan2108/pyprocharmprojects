# simple dicitonary
      # key   value pair  
alfa ={'key':'value'}
print(alfa)
# example 
alien_0 ={'color':'green', 'points':15}
print(alien_0)
# accesing the values in the dicitonary
print(alien_0['color'])
print(alien_0['points'])
# adding or accesing points
new_points =alien_0['points']
print("congratualtions you have won the " +str(new_points) + " points " )
# adding new keyvalue pairs 
alien_0 ={'color':'green', 'points':15}
alien_0['x_position'] = 0
alien_0['y_position'] = 0
print(alien_0)
# emptydictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points']=  15
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# modifying the calues in the dicitonary
alien_0 = {'color':'green'}
print("the alien color is" +alien_0['color'] +"!")
alien_0={'color':'red'}
print("the alien color is " +alien_0['color']+"!")

alien_0={'color': 'green', 'points': 15, 'x_position': 0, 'y_position': 25 , 'speed':'medium'}   
print(alien_0)
print("the x orginal position is" +str(alien_0['x_position'])+"!")

if alien_0['speed'] == 'slow':
    x_increment = 5
elif alien_0['speed'] == 'medium':
    x_increment = 10
else:
    x_increment = 15
alien_0['x_position'] = alien_0['x_position']+ x_increment
print("the new x position is" +str(alien_0['x_position'])+"!")

# Dictionary of similar objects
fav_shows ={
    'alfa':'amrutham',
    'beta':'amrutham',
    'charlie':'amrutham'
       
}
print("Alfa's fav_shows is " +fav_shows['alfa'].title()+'!')
# looping trough dictionary
user = {
    'username': 'gottam',
    'first_name': 'gokku',
    'last_name': 'ko'
}
for k, v in user.items():
    print("\nKey :" +k)
    print("Value :" +v)

fav_shows ={
    'alfa':'amrutham',
    'beta':'amrutham',
    'charlie':'amrutham'
       
}

for name,fav_show in fav_shows.items():
    print(name.title() +"favorite how is"+fav_show.title() )
    
for name in fav_shows.keys():
    print(name.title())    

# for fav_shows in fav_shows.keys():
#     print(fav_shows.title())  

           
           


