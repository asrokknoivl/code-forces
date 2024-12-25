import math
n_tests = int(input())

for _ in range(n_tests):
    n, d = map(int, input().split())
    fact_n = math.factorial(n)
    
    print(1)
    if (fact_n % 3 == 0 or d % 3 == 0):
        print(3)
    if (d % 5 == 0):
        print(5)
    if (fact_n % 7 == 0 or d % 7 == 0):
        print(7)
    if (fact_n % 9 == 0 or d % 9 == 0):
        print(9)