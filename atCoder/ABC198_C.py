import math

r, x, y = map(int, input().split() )

d = math.sqrt( x ** 2 + y ** 2 )

if d // r > 0:
    # if d % r > 0:
    #     print( int(d // r + 1) )
    # else:
    #     print(int(d // r))
    print(int(d // r + 1) if d % r > 0 else int(d // r))
else:
    print(2)
