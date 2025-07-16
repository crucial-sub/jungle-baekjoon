import sys
input_data = int(sys.stdin.readline().rstrip())

def get_hansoo(n) :
    if n < 100:
        return n;
    elif n == 1000:
        return 144;
    hansoo = 99;
    a,b,c = map(int,str(n))
    for i in range(1,a+1):
        for n in range(1,10):
            third = 2*n-i
            if((i == a and n > b) or (i == a and n == b and third > c)) : continue;
            if i >= n :
                if third >= 0 :
                    hansoo += 1;
                else: continue;
            else: 
                if third <= 9 :
                    hansoo += 1;
                else: continue;
    return hansoo

ans = get_hansoo(input_data)
print(ans)