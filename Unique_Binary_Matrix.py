"""

PROBLEM STATEMENT
Points: 30

Pulkit is really good at maths. Recently, he came to know about a problem on matrices. Amazed by the problem he got, he asked Ashish the same problem. Ashish also being good at maths solved the problem within 5 minutes. Now, its your time to solve the problem.

You will be given n*m binary matrix. You need to tell if it is possible to delete a column such that after deleting that column, rows of the matrix will be unique. If yes than print "Yes" else print "No".

[Input]
First line contains an integer t denoting no.of test cases.
Next line contains 2 integers n and m denoting no.of rows and columns.
Next n line contains binary string of length m each.

[Output]
For each test case output "Yes" or "No".

[Constraints]
1<=t<=100
1<=n<=1000
2<=m<=1000

Input
2
3 3
101
000
100
2 2
11
11

Output
Yes
No

"""

for i in range(int(input())):
    M,N=map(int,input().split())
    arr=[]
    for i in range(M):
        arr.append(input())
    if(len(set(arr))==len(arr)):
        print("Yes")
    else:
        print("No")
