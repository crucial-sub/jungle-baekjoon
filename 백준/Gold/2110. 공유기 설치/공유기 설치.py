import sys
input = sys.stdin.readline


# 집 간의 거리를 최소 dist값 만큼 띄우고 공유기를 설치할 때 몇 대까지 설치할 수 있는지 카운팅하는 함수
# 여기서 dist는 최적화됐다고 가정한 거리
def count_C(houses, dist):
    
    base = houses[0] # 첫 base는 첫 번째 집
    cnt = 1

    for house in houses[1:]: # 두 번째 집부터 한 집씩 base와의 거리를 체크
        if house - base >= dist: # 만약 base와의 거리가 dist보다 크거나 같으면 공유기 설치(cnt 증가)
            cnt += 1
            base = house # base를 해당 집으로 재설정 => 다음 house부턴 새로운 base와의 거리를 체크

    return cnt

def main():
    N, C = map(int, input().split())
    arr_x = [int(input()) for _ in range(N)]
    arr_x.sort() # 우선 정렬 때림
    ans = 0

    # 좌표간 거리를 최적화 해야하는 문제이므로 left, right 값도 거리의 최소, 최댓값으로 지정
    left = 1 # x좌표 간 거리의 최솟값은 1
    right = arr_x[-1] - arr_x[0] # 리스트가 정렬돼있으므로 끝 요소에서 처음 요소를 뺀것이 최댓값

    while left <= right: # left가 right보다 커지는 순간이 종료 시점
        mid = (left+right)//2 # 중간값 설정 => while 문이 도는 동안 이 mid 값을 최적화된 x좌표간 거리라 가정할 예정
                                # 즉, x좌표끼리 mid값 만큼 띄워서 공유기를 설치하면 문제 상황을 해결해줄거라고 가정
                                # 여기서 문제 상황은 공유기를 적절한 거리만큼 띄워서 원하는 개수만큼 설치하는 것

        if count_C(arr_x, mid) >= C: # 최소 mid값만큼 거리를 띄우고 공유기를 설치해봤을 때 C개 만큼 설치가 가능한지 체크 
            ans = mid # 체크를 통과한 mid값은 어느정도 최적화가 된것이 확인됐으니 ans에 할당
            left = mid + 1 # 더 최적화된 값(여기선 더 큰 mid값)이 있을 수 있으니
                           # 다음 루프의 mid값을 늘리기 위해 left(시작점)를 mid+1만큼 증가시키고 다시 돌려봄
        else: 
            right = mid - 1 # 체크를 못통과했다는 것은 설치한 공유기 수가 C보다 적다는 뜻이고,
                            # 설치 가능한 공유기 수를 늘리기 위해서는 mid값을 줄일 필요가 있다.
                            # right mid-1만큼 줄이면 자연히 다음 루프의 mid값도 줄어듬 

    print(ans)

if __name__ == "__main__":
    main()