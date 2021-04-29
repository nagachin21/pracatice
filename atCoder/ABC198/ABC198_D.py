import itertools

def assign():
    D = [-1] * 26
    for char, num in zip(chars, per):
        D[char] = num
    
    h1, h2, h3 = l1[-1], l2[-1], l3[-1]
    if D[h1] == 0 or D[h2] == 0 or D[h3] == 0:
        return False, D
    return True, D

def convert():
    n1, n2, n3 = 0, 0, 0
    for i, num in enumerate(l1):
        n1 += D[num] * 10 ** i
    for i, num in enumerate(l2):
        n2 += D[num] * 10 ** i
    for i, num in enumerate(l3):
        n3 += D[num] * 10 ** i
    
    return n1, n2, n3


s1 = list(input())[::-1]
s2 = list(input())[::-1]
s3 = list(input())[::-1]

l1 = [ord(char) - ord('a') for char in s1]
l2 = [ord(char) - ord('a') for char in s2]
l3 = [ord(char) - ord('a') for char in s3]

chars = set()
chars.update(l1, l2, l3)

if len(chars) > 10:
    print("UNSOLVABLE")
    exit()
else:
    for per in itertools.permutations(range(10), r=len(chars)):
        flg, D = assign()
        if not flg:
            continue
        else:
            n1, n2, n3 = convert()
            if n1 + n2 == n3:
                print(n1)
                print(n2)
                print(n3)
                exit()


print("UNSOLVABLE")