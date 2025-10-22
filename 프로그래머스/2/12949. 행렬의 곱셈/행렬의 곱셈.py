def solution(arr1, arr2):
    r_len = len(arr1)
    r2_len = len(arr2)
    c_len = len(arr2[0])
    
    answer = []
    
    # 1 4   3 3     15 15
    # 3 2   3 3     15 15
    # 4 1           15 15
    
    # 232 543   22 22 11
    # 424 241   36 28 18
    # 314 311   29 20 14
    
    # r1c1 r1c2 r1c3
    # r2c1 r2c2 r2c3
    # r3c1 r3c2 r3c3
    
    def multiple(arr1, arr2):
        return sum([a*b for a,b in zip(arr1, arr2)])
    
    for i in range(r_len):
        a = []
        r = arr1[i]
        
        for j in range(c_len):
            c = []
            for k in range(r2_len):
                c.append(arr2[k][j])
            a.append(multiple(r,c))
        answer.append(a)
    
    return answer