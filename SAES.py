# Round 1 : plain text xor with key0
# Round 2 : substitute using sbox and the shift 2nd and 4th bit

sbox = [9, 4, 10, 11, 13, 1, 8, 5, 6, 2, 0, 3, 12, 14, 15, 7]


def bintodec(arr):
    for i in range(4):
        arr[i] = list(map(int, arr[i]))
        arr[i] = arr[i][0] * 8 + arr[i][1] * 4 + arr[i][2] * 2 + arr[i][3]
    return [arr[0], arr[1], arr[2], arr[3]]


def addround(text, key):
    k = bintodec([key[:4], key[4:8], key[8:12], key[12:]])
    t = bintodec([text[:4], text[4:8], text[8:12], text[12:]])
    res = [k[0] ^ t[0], k[1] ^ t[1], k[2] ^ t[2], k[3] ^ t[3]]
    return res


def subs(a):
    s = list()
    for i in range(4):
        s.append(sbox[a[i]])
    return s


def shift(a):
    temp = a[3]
    a[3] = a[1]
    a[1] = temp
    return a


if __name__ == "__main__":
    text = input("Enter plain text : ")
    key = input("Enter key value : ")
    print(" ")
    print("------------------------------")
    res = addround(text, key)
    s = " "
    print("After add round key operation : " + str(res))
    print(" ")
    print("------------------------------")
    sub = subs(res)
    print("After substitution using s-box : " + str(sub))
    print(" ")
    print("------------------------------")
    sft = shift(sub)
    print("After Shift : " + str(sft))
