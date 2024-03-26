def solution(str1, str2):
    result = ''
    for i in range(0,len(str1)):
        a = str1[i] + str2[i]
        result += a
    return result