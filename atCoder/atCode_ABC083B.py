N, A, B = input().split()

some = []
for num in range(int(N)+1):
    numbers = list(str(num))
    x = sum(int(i) for i in numbers)
    if int(A) <= x and x <= int(B):
        some.append(num)

print(sum(some))