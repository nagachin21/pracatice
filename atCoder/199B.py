n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = min(b[0:n+1]) - max(a[0:n+1]) + 1
print( ans if ans >= 0 else 0)