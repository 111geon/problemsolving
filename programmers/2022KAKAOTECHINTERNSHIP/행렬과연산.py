from collections import deque

def solution(rc, operations):
    matrix = Matrix(rc)
    
    for operation in operations:
        matrix.operate(operation)
        
    return matrix.tolist()

class Matrix:
    operation_dict = {"Rotate": "rotate", "ShiftRow": "shiftrow"}
    
    def __init__(self, rc):
        self.leftcol = deque()
        self.rightcol = deque()
        self.rows = deque()
        
        for row in rc:
            self.leftcol.append(row[0])
            self.rightcol.append(row[-1])
            self.rows.append(deque(row[1:-1]))
    
    def operate(self, operation):
        getattr(self, Matrix.operation_dict[operation])()
    
    def shiftrow(self):
        for q in [self.leftcol, self.rightcol, self.rows]:   
            q.appendleft(q.pop())
    
    def rotate(self):
        self.rows[0].appendleft(self.leftcol.popleft())
        self.rightcol.appendleft(self.rows[0].pop())
        self.rows[-1].append(self.rightcol.pop())
        self.leftcol.append(self.rows[-1].popleft())
        
    def tolist(self):
        answer = [[] for _ in range(len(self.rows))]
        
        for i, left in enumerate(self.leftcol):
            answer[i].append(left)
        for i, mid in enumerate(self.rows):
            answer[i].extend(list(mid))
        for i, right in enumerate(self.rightcol):
            answer[i].append(right)
            
        return answer

"""
- deque
- 행렬을 제일 왼쪽 열, 오른쪽 열, 중간의 행들로 나누고 deque로 만들면 shiftrow, rotate 연산을 O(1)에 할 수 있다.
"""
