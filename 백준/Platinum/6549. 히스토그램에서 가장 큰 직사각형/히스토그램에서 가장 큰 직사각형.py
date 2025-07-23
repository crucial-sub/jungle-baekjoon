import sys
input = sys.stdin.readline

def solve_histogram(heights, n):
    """스택을 이용하여 히스토그램의 최대 직사각형 넓이를 계산합니다."""
    
    # 각 막대의 인덱스를 저장할 스택
    stack = []
    max_area = 0
    
    for i in range(n):
        # Case 2: 현재 막대가 스택 top의 막대보다 낮은 경우
        # 스택이 비어있지 않고, 스택 top의 높이가 현재 높이보다 크면 계속 pop
        while stack and heights[stack[-1]] > heights[i]:
            # 넓이를 계산할 막대의 높이
            height = heights[stack.pop()]
            
            # 너비 계산
            # 스택이 비었다면, pop된 막대가 가장 왼쪽 막대였다는 의미
            width = i if not stack else i - stack[-1] - 1
            
            max_area = max(max_area, height * width)

        # Case 1: 현재 막대가 스택 top의 막대보다 높거나 같은 경우
        stack.append(i)

    # 순회가 끝난 후 스택에 남아있는 막대들을 처리
    while stack:
        height = heights[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, height * width)
        
    return max_area

def main():
    while True:
        line = list(map(int, input().split()))
        n = line[0]
        
        if n == 0:
            break
        
        heights = line[1:]
        
        print(solve_histogram(heights, n))

if __name__ == "__main__":
    main()