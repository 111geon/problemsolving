import sys
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(dir_path + "/input.txt", "r")

def main():
    T = int(input())

    for test_case in range(1, T + 1):
        n = int(input())
        board = []

        for _ in range(n):
            board.append(list(map(int, input().split())))
        
        print("#" + str(test_case) + " " +  solution(n, board))

def solution(n, board):
    for row in board:
        print(row)
    return ""

main()
