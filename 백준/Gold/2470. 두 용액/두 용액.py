import sys
input = sys.stdin.readline

def main():
    N = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = []
    if l[0] > 0:
        ans.extend(l[:2])
    elif l[-1] < 0:
        ans.extend(l[-2:])
    else:
        left = 0
        right = len(l)-1
        min_dif = float('inf')
        while left < right:
            diff = l[left] + l[right]
            if abs(diff) < min_dif:
                ans = [l[left],l[right]]
                min_dif = abs(diff)
            if diff > 0:
                right -= 1
            elif diff < 0:
                left += 1
            else: 
                break
    print(*ans)



if __name__ == "__main__":
    main()