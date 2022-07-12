import sys; sysinput = sys.stdin.readline

def main():
    test_cases = get_inputs()
    for test_case in test_cases:
        solution(*test_case)

def get_inputs():
    t = int(sysinput())

    test_cases = []
    for _ in range(t):
        p = sysinput().strip()
        n = int(sysinput())
        if n == 0: x = []; sysinput()
        else: x = list(map(int, sysinput().strip().strip("[]").split(",")))
        test_cases.append((p, n, x))

    return test_cases

def solution(p, n, x):
    if p.count("D") > n: 
        print("error")
        return

    pre_cut = 0
    post_cut = 0
    is_reversed = False
    for rd in p:
        if rd == 'R':
            is_reversed = not is_reversed
        else:
            if is_reversed: post_cut += 1
            else: pre_cut += 1
    
    x = x[pre_cut:len(x)-post_cut]
    if is_reversed: x = list(reversed(x))

    print("[" + ",".join(map(str, x)) + "]")
    return

main()