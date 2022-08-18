import sys

input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        string = input().strip()
        print(check(string))

def check(string):
    p = [0, len(string)-1]
    if palindrome(string, p): return 0
    
    start, end = p[0], p[1]
    if palindrome(string, [start+1, end]): return 1
    if palindrome(string, [start, end-1]): return 1

    return 2    

def palindrome(string, p):
    start, end = p[0], p[1]
    while start < end:
        if string[start] != string[end]: 
            p[0], p[1] = start, end
            return False
        start += 1
        end -= 1
    return True

main()

"""
- 앞쪽에서 뒤로 이동하는 포인터와 뒤쪽에서 앞으로 이동하는 포인터를 이용한다.
- 완전회문인지를 검사하는 함수를 작성한다. 이때 start와 end 지점을 확인하고 수정해줄 수 있도록
  p 배열을 인수로 넣는다.
- 처음 완전 회문인지 검사한다. 맞다면 0을 반환
- 완전회문이 아닐 때 현재 start, end 위치에서 start와 end를 한칸씩 전진시켜보고 다시 회문 검사
  를 진행한다. 이때 회문이라도 판정되면 1을 반환
- 모든 조건을 만족하지 못하면 2를 반환
"""
