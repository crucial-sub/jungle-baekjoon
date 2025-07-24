import sys
input = sys.stdin.readline

def main():
    N = int(input())
    cards = list(map(int,input().split()))
    cards.sort()
    M = int(input())
    nums = map(int,input().split())

    ans = []
    for num in nums:
        left = 0
        right = len(cards)-1
        is_find = False

        while left <= right:
            mid = (left+right)//2
            target = cards[mid]

            if num == target:
                ans.append(1)
                is_find = True
                break
            elif num > target:
                left = mid + 1
            else:
                right = mid - 1
        if not is_find:
            ans.append(0)

    print(*ans)
    

if __name__ == "__main__":
    main()