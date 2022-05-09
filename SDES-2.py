# Plain text is permuted
# then perform expansion and permutation on right half
# K1 xor with new key
# K2 xor with new key

def per(text,per):
    t = list(text)
    s=" "
    print("------------------------------")
    p = list()

    for i in per:
        p.append(t[i - 1])

    print("After Permutation")
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
    p8 = [2,6,3,1,4,8,5,7]
    exp=[4,1,2,3,2,3,4,1]

    p_text = per(text, p8)
    t = p_text[4:]
    output = per(t, exp)
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
