import re
s = input()

diff = 1
while diff > 0:
    pre = s
    for char in ["dreamer+$", "dream+$", "eraser+$", "erase+$"]:
        s = re.sub(char, '', s)
    diff = len(pre) - len(s)


if len(s) == 0:
    print("YES")
else:
    print("NO")