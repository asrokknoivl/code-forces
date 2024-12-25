# https://codeforces.com/contest/2048/problem/B

n_tests = int(input())

for _ in range(n_tests):
    n, k = map(int, input().split())
    perm_n = list(range(1, n + 1))
    counter = 1
    while len(perm_n) != 0:
        if (counter == k):
            print(f"{perm_n.pop(0)} ", end="")
            counter = 1
        else:
            print(f"{perm_n.pop(-1)} ", end="")
            counter += 1
    print()
