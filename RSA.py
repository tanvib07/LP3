# n = p*q
# e is public key i.e. 1<e<fi
# fi=p-1 * q-1
# d = (fi*k)+1/e ==int for any k value ,d is private key
# C = P^e mod n
# D = C^d mod n

import math

p = 11
q = 7
n = p*q
e = 37
P = 15

C = pow(P,e) % n
print("RSA encrypted cipher text is : "+str(C))