n_tests = int(input())

for _ in range(n_tests):
    a_size = int(input())
    a_elements = list(map(int, input().split()))
    sums = set()
    i = 0
    j = 1
    while (i < len(a_elements)):
        while (j < len(a_elements)):
            
