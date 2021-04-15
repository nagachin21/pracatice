a, b, c, x = map(int, open(0)）

ans = [ 500*i + 100*j + 50*k == x for i in range( a+1 ) for j in range( b+1 ) for k in range( c+1 ) ]
print(sum(ans))