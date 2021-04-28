import sys

N = input()
if N == N[::-1]:
    print("Yes")
    sys.exit()

for i in range(9):
    N = "0" + N
    if N == N[::-1]:
        print("Yes")
        sys.exit()

print("No")