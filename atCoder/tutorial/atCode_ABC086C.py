import sys
N = int(input())
points = [ list(map(int, input().split())) for i in range(N) ]

for i in range(N):
    if i == 0:
        p = 0
        x = points[i][1]
        y = points[i][2]
    else:
        p = points[i-1][0]
        x = abs(points[i][1] - points[i-1][1])
        y = abs(points[i][2] - points[i-1][2])
    
    if x+y+p > points[i][0]:
        print("No")
        sys.exit()
    elif x+y+p < points[i][0]:
        if (p-x+y) % 2 != 0:
            print("No")
            sys.exit()

print("Yes")
