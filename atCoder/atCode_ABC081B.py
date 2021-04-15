def check_list(num_list):
    for item in num_list:
        if item % 2 != 0:
            return False
    return True


n = int(input())
num_list = list(map(int, input().split()))
count = 0

while check_list(num_list):
    num_list = list(map(lambda x: int(x / 2) ,num_list))
    count += 1

print(count)



