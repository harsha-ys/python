import sys
sys.setrecursionlimit(10**6)
def merge_the_tools(string, k):
    # your code goes here
    if not string: return
    sub = ""
    for i in range(k):
        c=string[i]
        if not c in sub:
            sub +=c
    print(sub)
    merge_the_tools(string[k:], k)
            

