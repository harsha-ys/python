# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
x, k = input().split()
for i in permutations(sorted(x), int(k)):
    print("".join(i))
