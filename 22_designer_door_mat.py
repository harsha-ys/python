# Enter your code here. Read input from STDIN. Print output to STDOUT
N,M=map(int,input().split())

    
def door(N, M, row, plus, or_):
    
    if row == 0:return  
    if row == (N//2 +1) :
        print("-"*int((M-7)/2)+"WELCOME"+"-"*int((M-7)/2))
        door(N, M, row-1, False, or_-2)
        return
    print("-"*int((M-or_*3)/2)+ ".|."*or_+ "-"*int((M-or_*3)/2)) 
    door(N, M, row+1, plus, or_+2) if plus else door(N, M, row-1, plus, or_-2)
    
door(N, M, 1, True, 1)
