# Enter your code here. Read input from STDIN. Print output to STDOUT
A = list( map(int, input().strip().split()) )
B = list(map(int, input().strip().split()))
c=[(x, y) for x in A for y in B]
for i in c: print(i, end=" ")
