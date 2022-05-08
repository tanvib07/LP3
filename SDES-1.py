# We will need 3 funtions to
# Permute 10 bits
# Permute 8 bits
# Shift bits
# to get K1,K2 from 2 rounds

def per10(k):
    print("Before 10 bit Permutation")
    key = list(k)
    s=" "
    print(s.join(key))
    #3 5 2 7 4 10 1 9 8 6
    p = list()
    p.insert(0, key[8])
    p.insert(1, key[3])
    p.insert(2, key[9])
    p.insert(3, key[4])
    p.insert(4, key[7])
    p.insert(5, key[0])
    p.insert(6, key[5])
    p.insert(7, key[1])
    p.insert(8, key[6])
    p.insert(9, key[2])
    print("After 10 bit Permutation")
    s=" "
    print(s.join(p))
    print(" ")
    print("------------------------------")
    return p

def rotate(l,n):
    return l[n:]+l[:n]

def leftshift(key,num):
    l_key, r_key = rotate(key[0:5],num), rotate(key[5:],num)
    final_key = l_key+r_key
    s=" "
    print("After Left Shift for Round "+str(num))
    print(s.join(final_key))
    print(" ")
    print("------------------------------")
    return final_key

def per8(key):
    print("Before 8 bit Permutation")
    s = " "
    print(s.join(key))
    #6 3 7 4 8 5 10 9
    p = list()
    p.insert(0, key[8])
    p.insert(1, key[2])
    p.insert(2, key[5])
    p.insert(3, key[7])
    p.insert(4, key[3])
    p.insert(5, key[6])
    p.insert(6, key[4])
    p.insert(7, key[9])

    print("After 8 bit Permutation")
    s = " "
    print(s.join(p))
    print(" ")
    print("------------------------------")
    return p

if __name__ == "__main__" :
    print("Enter 10 bit key")
    k = input()
    #Round1 for K1
    p_key = per10(k) #10 bit permutation
    num=1
    s_key = leftshift(p_key,num) #shift by 1 and get the key
    K1 = per8(s_key) #8bit permutation
    num=2
    s1_key = leftshift(s_key,num) #shift by 2
    K2 = per8(s1_key) #8bit permutation
    s=" "
    print("K1 = "+str(s.join(K1)) +" and K2 = "+str(s.join(K2)))




