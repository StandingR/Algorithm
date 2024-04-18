def is_valid_brackets(s):
    stack = []
    
    # 문자열 s의 각 문자에 대해 반복
    for char in s:
        if len(stack) == 0:
            stack.append(char)
        else:
            # 현재 문자가 ')'이고, 스택의 가장 위의 문자가 '('인 경우
            if char == ")" and stack[-1] == "(":
                stack.pop()
            # 현재 문자가 ']'이고, 스택의 가장 위의 문자가 '['인 경우
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            # 현재 문자가 '}'이고, 스택의 가장 위의 문자가 '{'인 경우
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            else:
                # 현재 문자가 여는 괄호인 경우 스택에 추가
                stack.append(char)
    
    # 스택이 비어있으면 올바른 괄호 문자열이므로 True 반환, 아니면 False 반환
    return True if len(stack) == 0 else False

# 문자열 돌리기

def solution(s):
    valid_count = 0
    
    # 문자열 s의 길이만큼 반복
    for _ in range(len(s)):
        # 현재 문자열 s가 올바른 괄호 문자열인지 확인하여 카운트 증가
        if is_valid_brackets(s):
            valid_count += 1
        
        # 문자열을 왼쪽으로 한 칸 회전
        s = s[1:] + s[:1]
    
    # 올바른 괄호 문자열의 개수 반환
    return valid_count
