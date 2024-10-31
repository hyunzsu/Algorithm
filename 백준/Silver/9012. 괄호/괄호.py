import sys
input=sys.stdin.readline
N=int(input())
for i in range(N):
    ps=input().strip()
    stack=[]
    ans=0
    try:
        for j in ps:
            if j=="(":
                stack.append(0)
                ans+=1
            else:
                stack.pop()
                ans-=1
    except:
        print('NO')
    else:
        if ans==0:
            print('YES')
        else:
            print('NO')