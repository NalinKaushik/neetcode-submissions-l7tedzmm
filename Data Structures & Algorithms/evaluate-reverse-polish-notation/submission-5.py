from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arth = {    '*':lambda x,y: x * y,
                    '/':lambda x,y: x / y,
                    '+':lambda x,y: x + y,
                    '-':lambda x,y: x - y
                    }
        stack = deque()
        for i in tokens:
            if i not in arth:
                stack.append(i)
            else:
                num1 = int(stack.pop())
                num2  = int(stack.pop())
                arthematic = arth[i](num2,num1)
                stack.append(arthematic)
        
        return int((stack.pop()))
                