# elements in list
x = [1, 2, 3, "Sports"]

for a in  x:
    print(a)
    
# printing the characters
a = "Kickboxing"
for ch in a:
    print(ch)
    
# gst the
items = [10,20,30]
gst = 3
for x in items:
    print(x+gst)
    
#  range
for x in  range(1,15):
    print(x)
    
cost = [10,20,30]
print(cost)
sum = 0
for x in cost:
    sum = sum + x
print(sum)    
        
#nested loops

# rows = range(1,5)
# for x in rows:
#     for star in range(1,x+1):
#         print('* ', end='')
#     print()    
    
# rows = range(2,10)
# for a in rows:
#     for star in range(2, x+2):
#         print('* ', end='')
#     print()    
         
rows = range(0,5)
for x in rows:
    for j in range(0, x+1):
        print('* ', end="")
    print()     
          
for i in range(0,10):
    for j in range(0, i+1):
        print('* ', end="") 
    print()             
    
a = int(input("Enter the number a :"))
for b in range(a):
    print(" "*(a-b-1), end="")
    for c in range(b+1):
        print(b+1,"",end="")
    print()    