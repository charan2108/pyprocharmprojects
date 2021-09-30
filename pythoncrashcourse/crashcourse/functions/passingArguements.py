# Positional Arguements
def batsmen(batsmen_type, batsmen_name):
    print("\n I Have a"+batsmen_type+".")
    print("\n I Have a "+batsmen_type+" batsmen name is " +batsmen_name+"!")
batsmen('Rhb', 'Sachin')    
batsmen('lhb', 'S.G')

# Keywords
def batsmen(batsmen_type, batsmen_name):
    print("\n I Have a"+batsmen_type+".")
    print("\n I Have a "+batsmen_type+" batsmen name is " +batsmen_name+"!")
batsmen(batsmen_type='Rhb', batsmen_name = 'Sachin')

# default values
def batsmen(batsmen_name, batsmen_type='Rhb' ):
    print("\n I Have a"+batsmen_type+".")
    print("\n I Have a "+batsmen_type+" batsmen name is " +batsmen_name+"!")
batsmen(batsmen_name = 'sachin')    

def make_shirt(shirt_color, shirt_size):
    print("\n I have a new shirt color"+shirt_color+"!")
    print("\n I have a new shirt color"+shirt_color+"  and the szoe of the shirt is"+shirt_size+"!")
make_shirt('lightgreen', 'M')    
def make_shirt(shirt_color, shirt_size):
    print("\n I have a new shirt color"+shirt_color+"!")
    print("\n I have a new shirt color"+shirt_color+"  and the szoe of the shirt is"+shirt_size+"!")
make_shirt(shirt_color='light green',shirt_size= 'M')

def make_shirt(shirt_color, shirt_size='M'):
    print("\n I have a new shirt color"+shirt_color+"!")
    print("\n I have a new shirt color"+shirt_color+"  and the szoe of the shirt is"+shirt_size+"!")
make_shirt(shirt_color='lightgreen')
def make_shirt(shirt_color, shirt_size ='L'):
    print("\n I have a new shirt color"+shirt_color+"!")
    print("\n I have a new shirt color"+shirt_color+"  and the szoe of the shirt is"+shirt_size+"!")
make_shirt(shirt_color='lightgreen')


    
