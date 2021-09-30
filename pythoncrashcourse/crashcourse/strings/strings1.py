# empl info in strings
name = "AlfaClors"
emp_id =  30
print("Employee name is ", name)
print("Employee id is ",emp_id)
# empty string
name = ""
print(name)

# indexing
a = "Hello World"
print(a)
print(type(a))
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print(a[7])
print(a[8])
print(a[9])
print(a[10])
print("\n")
# reverse indexing
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])
print(a[-6])
print(a[-7])
print(a[-8])
print(a[-9])
print(a[-10])
print(a[-11])

# character
name = "python"
print(name)
for a in name:
    print(a)
# accessing cases
a = 'SportsBike'
print(a)
# dports[::] accees 0 to last
print(a[::])
print(a[:])
# sccess 0 to 8th element
print(a[0:9:1])
print(a[0:9:2])
print(a[2:4:1])
print(a[2::])
print(a[::2])
print(a[:4:])
# concatenation
a ="Bike"
b = "Wheels"
print(a+b)
# multiplication
a = 'Kick'
b = 14
print(a*b)
# memebership operators
# in operator
print('p' in 'Python')
print('a' in 'Python')
print('ax' in 'Python')
print('n' in 'Python')
print('y' in 'Python')
main = input("Enter the main string")
s = input("Enter substring")
if s in main:
    print(s,"String is found")
else:
    print(s,"String is not found")    
# not in
print(b, 'not apple')

# comparison
s1 = "Hello"
s2 = "Hello World"
if (s1 == s2):
    print("Both r equal")
else:
    print("Not equal")    