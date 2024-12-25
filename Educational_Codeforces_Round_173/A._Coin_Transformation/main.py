
nt = int(input())
for _ in range(nt):
    x = int(input())
    max_coins = 1
    while (x > 3):
        max_coins *= 2
        x //= 4
    print(max_coins)