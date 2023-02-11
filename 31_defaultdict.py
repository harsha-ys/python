# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = map(int, input().split())
A_with_positions = defaultdict(list)
for i in range(n): A_with_positions[input()].append(str(i+1))
for i in range(m): 
    b = input()
    print(" ".join(A_with_positions[b])) if b in A_with_positions else print(-1)
