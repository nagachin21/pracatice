N = input()
cards = sorted(list( map(int, input().split()) ), reverse=True)

print(sum(cards[0::2]) - sum(cards[1::2]))