import sys
input = sys.stdin.readline

text = list(input().strip())
text_bomb = list(input().strip())

stack =[]

for t in text:
    stack.append(t)

    if stack[-len(text_bomb):] == text_bomb:
        del stack[-len(text_bomb):]

if stack:
    print(''.join(stack))
else:
    print("FRULA")