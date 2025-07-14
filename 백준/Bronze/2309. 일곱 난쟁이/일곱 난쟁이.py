import sys
data = [int(sys.stdin.readline()) for _ in range(9)]

# n개 중에 r개를 뽑는 조합
def find_combine(arr, r):
    result=[]
    found = False

    def backtrack(start, path, total):
        nonlocal found
        if found: return

        if len(path) == r:
            if total == 100:
                result.extend(path[:])
                found = True
            return

        for i in range(start,len(arr)):
            if total + arr[i] > 100:
                continue
            path.append(arr[i])
            backtrack(i+1,path,total+arr[i])
            path.pop()

    backtrack(0,[],0)
    return sorted(result)

for h in find_combine(data,7):
    print(h)