# name= "adam carry"
# print(name.title())

# # lowercase
# name = "Adam carry"
# print(name.lower())
# # uppercase
# print(name.upper())
def solution(N):
    N = bin(N)[2:]
    b = 0
    maxb = 0
    for a in N:
        if int(a)==0:
            b+=1
        elif int(a)==1:
            maxb=max(b,maxb) 
            b=0
    return maxb  