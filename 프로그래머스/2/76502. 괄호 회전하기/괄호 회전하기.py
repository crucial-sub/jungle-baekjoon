def solution(s):
    answer = 0
    open_p = ["[","{","("]
    close_p = ["]","}",")"]
    pair = {
        "]":"[",
        "}":"{",
        ")":"("
    }
    
    len_s = len(s)
    
    def rotateX(s,x):
        if x == 0:
            return s
        return s[x:] + ''.join(s[:x])
    
    def check_validate(s):
        if s[0] in close_p or s[-1] in open_p:
            return False
        stack = []
        for p in s:
            if p in open_p:
                stack.append(p)
            else:
                if not stack:
                    return False
                poped = stack.pop()
                if pair[p] != poped:
                    return False
        if len(stack) != 0:
            return False
        return True

    for x in range(len_s):
        rotated_s = rotateX(s,x)
        if check_validate(rotated_s):
            answer += 1
    
    return answer