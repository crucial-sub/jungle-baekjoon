from collections import defaultdict,Counter

def solution(want, number, discount):
    
    answer = 0
    len_d = len(discount)
    
    for i in range(len_d-9):
        discounts = discount[i:i+10]
        if set(want) != set(discounts):
            continue
        
        # cnt_discount = defaultdict(int)
        # for d in discounts:
        #     cnt_discount[d] += 1
        cnt_discount = Counter(discounts)
        
        passed = True
        for j,w in enumerate(want):
            if cnt_discount[w] != number[j]:
                passed = False
                break
                
        if passed:
            answer += 1
        
    return answer