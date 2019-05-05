import sys

def isBalanced(s):
    stack = []
    helper = {'(': ')', '{': '}', '[': ']'}
    for i in s:
        if stack:
            if helper.get(stack[-1]) == i:
                stack.pop()
                continue
        stack.append(i)
    return "NO" if stack else "YES"


t=int(input().strip())

for _ in range(t):
    s=input().strip();
    result=isBalanced(s);
    print(result)