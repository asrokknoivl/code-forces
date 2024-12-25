


n_tests = int(input())
for i in range(n_tests):
    x = input()
    l1 = 1
    r1 = len(x)
    l2 = 1
    r2 = len(x)
    
    l1_c = 0
    r2_c = len(x)-1
    l2_c = 0
    r2_c = len(x)-1
    
    while (r2 != l2):
        if(x[l1_c] == x[l2_c]):
            l1_c += 1
            r2 -= 1
        else:
            break
    print(f"{l1} {r1} {l2} {r2}")
    
