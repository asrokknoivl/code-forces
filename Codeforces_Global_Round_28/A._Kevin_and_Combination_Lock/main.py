

#https://codeforces.com/contest/2048/problem/A

solution = 33


def compute(n: int):
    if (n%solution == 0):
        return True
    else:
        if ("33" in str(n)):
            return compute(int(str(n).replace("33", "")))
        else:
            return False

n_tests = int(input())
for i in range(n_tests):
    x = int(input())
    print("YES") if (compute(x)) else print("NO")
