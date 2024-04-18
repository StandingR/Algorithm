def is_valid_brackets(s):
    stack = []
    for char in s:
        if len(stack) == 0:
            stack.append(char)
        else:
            if char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(char)
    return True if len(stack) == 0 else False

def solution(s):
    valid_count = 0
    for _ in range(len(s)):
        if is_valid_brackets(s):
            valid_count += 1
        # Rotate the string by one character to the left
        s = s[1:] + s[:1]
    return valid_count

