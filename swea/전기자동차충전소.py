MAX_INT = 2**63-1

def main():
    tc = int(input())
    for t in range(1, tc+1):
        n = int(input())
        houses = []
        for _ in range(n):
            houses.append(tuple(map(int, input().split())))  # (x, y, d)
        
        ans = helper(houses)

        ans = -1 if ans == MAX_INT else ans
        print("#" + str(t), ans)

def helper(houses):
    ans = MAX_INT
    for cx in range(-15, 16):
        for cy in range(-15, 16):
            temp = 0
            for hx, hy, d in houses:
                cald = abs(hx-cx) + abs(hy-cy)
                if cald == 0 or cald > d: break
                temp += cald
            else:
                ans = min(ans, temp)

    if ans != MAX_INT: return ans

    for cx in range(-15, 16):
        for cy in range(-15, 16):
            for i in range(-15, 16):
                for j in range(-15, 16):
                    temp = 0
                    for hx, hy, d in houses:
                        cald1 = abs(hx-cx) + abs(hy-cy)
                        cald2 = abs(hx-i) + abs(hy-j)
                        if cald1 == 0 or cald2 == 0 or (cald1 > d and cald2 > d): break
                        temp += min(cald1, cald2)
                    else: 
                        ans = min(ans, temp)

    return ans

if __name__ == "__main__":
    main()
