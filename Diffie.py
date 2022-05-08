import math

q = 11
alp = 2 #alpha
Xa = 8
Xb = 4

#For exchanging keys

x = pow(alp,Xa) % q
y = pow(alp,Xb) % q

A = pow(y,Xa) % q
B = pow(x,Xb) % q

if A==B:
    print("The key generated is : "+str(A))