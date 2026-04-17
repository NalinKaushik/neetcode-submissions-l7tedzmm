from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        brackets = {'(':')',
                    '{':'}',
                    '[':']'
                    }
        for i in s:
            if i in brackets:
                stack.append(i)
            
            else:
                if len(stack) == 0:
                    return False

                popelem = stack.pop()
                if brackets[popelem] != i:
                    return False
        
        if len(stack)!=0:
            return False
        
        else:
            return True