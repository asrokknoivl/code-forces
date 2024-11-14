# https://codeforces.com/gym/105493/problem/A

# n = int(input('insert n: '))
# a = int(input('insert a: '))
# b = int(input('insert b: '))
# c = int(input('insert c: '))
# d = int(input('insert d: '))

n = int(input())
a,b = (int(x) for x in input().split(' '))
c,d = (int(x) for x in input().split(' '))

if a == c:
    print(d-b)
else:
    print(((c-a-1)*n) + (n-b) + d + (1 * (c-a)))
