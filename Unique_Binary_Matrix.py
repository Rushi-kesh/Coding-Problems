for i in range(int(input())):
    M,N=map(int,input().split())
    arr=[]
    for i in range(M):
        arr.append(input())
    if(len(set(arr))==len(arr)):
        print("Yes")
    else:
        print("No")
