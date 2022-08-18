import sys; input = sys.stdin.readline
import collections

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        tree = collections.defaultdict(list)
        parent_dict = dict()
        finding_root = set([i for i in range(1, n+1)])

        for _ in range(n-1):
            parent, child = map(int, input().split())
            tree[parent].append(child)
            parent_dict[child] = parent
            finding_root.remove(child)
        
        root = list(finding_root)[0]

        a, b = map(int, input().split())

        a_level = find_level(parent_dict, a, root)
        b_level = find_level(parent_dict, b, root)
        
        while a_level != b_level:
            if a_level > b_level:
                a_level -= 1
                a = parent_dict[a]
            else:
                b_level -= 1
                b = parent_dict[b]

        while a != b:
            a = parent_dict[a]
            b = parent_dict[b]

        print(a)

def find_level(parent_dict, node, root):
    level = 0
    while node != root:
        level += 1
        node = parent_dict[node]
    return level

main()

"""
- tree와 {child: parent} 정보를 각각 저장한다.
- 주어진 두 노드 a, b를 각각 거슬러 올라가며 각각의 깊이를 찾는다
- 두 노드의 깊이가 같아질 때 까지 더 깊은 쪽을 끌어 올린다.
- a, b를 함께 깊이 한단계씩 올라가며 공통 조상을 찾는다.
"""
