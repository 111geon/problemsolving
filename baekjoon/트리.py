import sys; input = sys.stdin.readline
import collections

def main():
    n = int(input())
    tree = collections.defaultdict(list)
    parent_dict = dict()
    for child, parent in enumerate(map(int, input().split())):
        if parent == -1: root = child
        tree[parent].append(child)
        parent_dict[child] = parent
    
    to_delete = int(input())
    if root == to_delete: 
        print(0)
        return

    tree[parent_dict[to_delete]].remove(to_delete)
    print(get_leaf_num(tree, root))

def get_leaf_num(tree, node):
    if not tree[node]: return 1
    return sum([get_leaf_num(tree, child) for child in tree[node]])

main()

"""
- 인접리스트로 tree를 만들고, 추가로 {child: parent} 정보도 저장해둔다.
- 지울 노드가 루트 노드라면 0을 반환한다.
- tree에서 지울 노드를 끊어내기 위해 지울 노드의 부모를 찾아서 그 노드의 인접리스트에서 지울 노드
  를 삭제해버린다.
- 삭제 후 재귀함수를 이용해 leaf node의 개수를 구한다.
"""
