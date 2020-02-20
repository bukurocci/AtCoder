n = int(input())
cards = list(map(int, input().split()))

list.sort(cards, reverse=True)

alice = sum(cards[0::2])
bob = sum(cards[1::2])

print("{}".format(alice - bob))
