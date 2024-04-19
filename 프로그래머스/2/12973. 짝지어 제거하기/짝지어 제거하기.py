
def solution(s):
    stack = []
    for output in range(len(s)):
        if not stack:
            stack.append(s[output])
        else:
            if s[output] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[output])
    if stack: 
        return 0
    else:  
        return 1
    
    













