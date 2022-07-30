import collections

def main():
    for t in range(1, int(input())+1):
        v, e, a, b = map(int, input().split())
        from_tos = list(map(int, input().split()))
        root = 1
        tree = collections.defaultdict(list)
        for i in range(e):
            tree[from_tos[2*i]].append(from_tos[2*i+1])
            tree[from_tos[2*i+1]].append(from_tos[2*i])
        
        print("#" + str(t), solution(tree, root, a, b))

def solution(tree, root, a, b):
    level = {root: 1}
    stack = [root]
    while stack:
        tmp = []
        for curr_node in stack:
            for next_node in tree[curr_node]:
                if next_node not in level:
                    level[next_node] = level[curr_node] + 1
                    tmp.append(next_node)
        stack = tmp
    
    older = a if level[a] < level[b] else b
    younger = b if older == a else a

    while level[older] != level[younger]:
        younger = get_parent(tree, level, younger)
    
    while younger != older:
        older = get_parent(tree, level, older)
        younger = get_parent(tree, level, younger)

    common_ancestor = younger

    return str(common_ancestor) + " " + str(get_tree_size(tree, level, common_ancestor))

def get_parent(tree, level, younger):
    for node in tree[younger]:
        if level[node] == level[younger] - 1: 
            return node

def get_tree_size(tree, level, start):
    visited = {start}
    stack = [start]
    ans = 1

    if get_parent(tree, level, start):
        visited.add(get_parent(tree, level, start))

    while stack:
        for node in tree[stack.pop()]:
            if node not in visited:
                visited.add(node)
                stack.append(node)
                ans += 1

    return ans

main()

'''
10
13 12 8 13
1 2 1 3 2 4 3 5 3 6 4 7 7 12 5 9 5 8 6 10 6 11 11 13
10 9 2 10
1 2 1 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10
'''
