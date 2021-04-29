N, Y = map(int, input().split())

ans = []

if Y > 10000*N:
    ans.extend([-1, -1, -1])
else:
    for i in range(N+1):
        if Y - 10000*i >= 0:
            for j in range( N-i+1 ):
                if 10000*i + 5000*j + 1000*(N-i-j) == Y:
                    ans.extend([i, j , N-i-j])
                    break
        elif i == N:
            ans.extend([-1, -1, -1])
        
        if len(ans) > 0:
            break

print(*ans)


