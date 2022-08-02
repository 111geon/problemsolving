import sys; input = sys.stdin.readline

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return self.val

def main():
    n = int(input())
    nodes = {}
    for i in range(n):
        nodes[chr(ord("A")+i)] = Node(chr(ord("A")+i))

    for _ in range(n):
        curr, left, right = input().split()
        if left != ".": nodes[curr].left = nodes[left]
        if right != ".": nodes[curr].right = nodes[right]
    
    start = nodes["A"]

    preorder(nodes, start)
    print()
    inorder(nodes, start)
    print()
    postorder(nodes, start)

def preorder(nodes, start):
    print(start, end="")
    if start.left: preorder(nodes, start.left)
    if start.right: preorder(nodes, start.right)

def inorder(nodes, start):
    if start.left: inorder(nodes, start.left)
    print(start, end="")
    if start.right: inorder(nodes, start.right)

def postorder(nodes, start):
    if start.left: postorder(nodes, start.left)
    if start.right: postorder(nodes, start.right)
    print(start, end="")

main()
