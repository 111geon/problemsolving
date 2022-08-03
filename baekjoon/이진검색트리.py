import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    nums = []
    while True:
        try:
            nums.append(int(input()))
        except:
            break
    
    start, end = 0, len(nums)-1
    postorder(nums, start, end)

def postorder(nums, start, end):
    if start > end: return

    root = nums[start]
    mid = start + 1
    while mid <= end and nums[mid] <= root: mid += 1

    postorder(nums, start+1, mid-1)
    postorder(nums, mid, end)
    print(root)


# def main():
#     root = Node(int(input()))
#     try:
#         while True:
#             root.add(Node(int(input())))
#     except: 
#         pass
    
#     postorder(root)

# def postorder(node):
#     if node.left: postorder(node.left)
#     if node.right: postorder(node.right)
#     print(node)


# class Node:
#     def __init__(self, value) -> None:
#         self.value = value
#         self.left = None
#         self.right = None
    
#     def __repr__(self) -> str:
#         return str(self.value)
    
#     def add(self, node) -> None:
#         if node.value < self.value:
#             if self.left: return self.left.add(node)
#             self.left = node
#         else:
#             if self.right: return self.right.add(node)
#             self.right = node

main()
