def solution(N, X,Y,Z):
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
      
# def solution(A):
#     # A = bin(A)[2:]
#     b = 0
#     maxb = 0
#     for c in A:
#         if int(c)==0:
#             b+=1
#         elif int(c)==1:
#             maxb=max(b,maxb) 
#             b=0
#     return maxb 

# def cyclic(A, K):
#     N = len(A)
#     B = [None] * N
#     for i in range(0, N):
#         B[(i+K)%N] = A[i]
#     return B
#     pass        
     


# # def reverse(A):
# #     N=len(A)
# #     for i in xrange(N // 2):
# #         k = N-i-1
# #         A[i], A[k] = A[k], A[i]
# #     return A    

# def solution(A):
#     A.sort()
#     A.append(-1)
#     for i in range(0, len(A), 2):
#         if A[i]!= A[i+1]:
#             return A[i]
# pass        

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, X, Y, Z):
    # write your code in Python 3.6
  A=bin(A)[2:]  
  b = 8
  maxb = 0
  for c in A:
      if c==0:
          b+=1
      elif c==2:
          maxb=max(b, maxb)
          b=0
      else:       
         return  maxb     
         pass
