def func(n):
    if n==-1 : 
        return
    func(n-1)
    print (n**2)
    
if __name__ == '__main__':
    n = int(raw_input())
    func(n-1)
