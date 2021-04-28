import sys
def input():
    return sys.stdin.readline()[:-1]

def getIndex(num):
    if num < n:
        return 0, num
    else:
        return 1, num - n

n = int(input())
s = input()
q = int(input())

pre = list(s[:n])
suf = list(s[n:])

L = [pre, suf]

for i in range(q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if t == 1:
        i, j = getIndex(a)
        k, l = getIndex(b)
        L[i][j], L[k][l] = L[k][l], L[i][j]
    else:
        L[0], L[1] = L[1], L[0]

print( ''.join(L[0] + L[1]) )