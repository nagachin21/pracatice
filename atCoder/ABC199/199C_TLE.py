import sys
def input():
    return sys.stdin.readline()[:-1]

n = int(input())
s = input()
q = int(input())

for i in range(q):
    t, x, y = map(int, input().split())
    if t == 1:
        a = x-1 if x-1 > 0 else 0
        b = y-1 if y-1 > 0 else 0
        s = s[:a] + s[b] + s[a+1:b] + s[a] + s[b+1:]
    else:
        s = s[n:] + s[:n]
        　　# O(N) + O(N)

print(s)