def main():
    a, b = map(int, input().split())

    if a%3 == (b+1)%3: print('A')
    else: print('B') 

main()
