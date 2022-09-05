import sys

class stack:
    def __init__(self, size=100000):
        self.arr = [None] * size
        self.last_index = 0

    def push(self, value):
        self.arr[self.last_index] = value
        self.last_index += 1

    def pop(self):
        # if self.last_index == 0:
        #     return None
        self.last_index = self.last_index - 1
        return self.arr[self.last_index]

    def empty(self):
        if self.last_index == 0:
            return True
        else:
            return False

    def peek(self):
        if self.empty() == 0:
            return -1
            # raise Exception('Stack is empty')
        return self.arr[self.last_index -1]    

answer = 0 # 막대기의 갯수
st = stack()
iron = sys.stdin.readline().rstrip()
#print(len(iron))

for i in range(len(iron)): #입력의 길이만큼
    if iron[i]=='(': #여는괄호라면 일단 push
        st.push('(')
    else: # 닫는괄호라면
        if iron[i-1]=='(': #전에가 여는괄호인지 검사 == (괄호가 인접한 쌍인지)
            #그렇다면 레이저 쏜거니까 걍 pop
            st.pop()
            answer += st.last_index

        else: #레이저가 아니고 막대의 끝이라면
            st.pop()
            answer += 1

print(answer)
    
