# Plain text is permuted
# then perform expansion and permutation on right half
# K1 xor with new key
# K2 xor with new key

def per8(text):
    t = list(text)
    s=" "
    print("------------------------------")
    p = list()
    p.insert(0, t[7])
    p.insert(1, t[2])
    p.insert(2, t[6])
    p.insert(3, t[3])
    p.insert(4, t[5])
    p.insert(5, t[1])
    p.insert(6, t[4])
    p.insert(7, t[0])
    print("After Permutation")
    print(s.join(p))
    print(" ")
    print("------------------------------")
    return p

def split_exp_per(p_text):
    t = p_text[4:]
    p = list()
    s=" "
    print("Right half is "+str(s.join(t)))
    p.insert(0, t[1])
    p.insert(1, t[2])
    p.insert(2, t[3])
    p.insert(3, t[0])
    p.insert(4, t[2])
    p.insert(5, t[1])
    p.insert(6, t[3])
    p.insert(7, t[0])
    print("After Expantion and Permutation on right half ")
    print(s.join(p))
    print(" ")
    print("------------------------------")
    return p


if __name__ == "__main__":
    print("Enter K1 key")
    k1 = list(map(int,input()))
    print("Enter K2 key")
    k2 = list(map(int,input()))
    print("Enter plain text")
    text = input()
    p_text = per8(text)
    output = split_exp_per(p_text)
    output = [int(i) for i in output]
    s=" "
    #XOR with k1
    result1 = list(map(str, (a ^ b for a, b in zip(k1, output))))

    print("XOR with K1 : "+str(s.join(result1)))
    print(" ")
    print("------------------------------")
    # XOR with k2
    result2 = list(map(str, (a ^ b for a, b in zip(k2, output))))
    print("XOR with K2 : "+ str(s.join(result2)))
