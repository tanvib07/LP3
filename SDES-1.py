# We will need 3 funtions to
# Permute 10 bits
# Permute 8 bits
# Shift bits
# to get K1,K2 from 2 rounds

def per(k, per):
    print("Before Permutation")
    key = list(k)
    s=" "
    print(s.join(key))

    p =[]
    for i in per:
        p.append(key[i-1])

    print("After Permutation")
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



if __name__ == "__main__" :
    p8 = [6,3,7,4,8,5,10,9]
    p10= [3,5,2,7,4,10,1,9,8,6]
    print("Enter 10 bit key")
    k = input()
    #Round1 for K1
    p_key = per(k,p10) #10 bit permutation
    num=1
    s_key = leftshift(p_key,num) #shift by 1 and get the key
    K1 = per(s_key, p8) #8bit permutation
    num=2
    s1_key = leftshift(s_key,num) #shift by 2
    K2 = per(s1_key,p8) #8bit permutation
    s=" "
    print("K1 = "+str(s.join(K1)) +" and K2 = "+str(s.join(K2)))




