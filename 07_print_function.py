def print_to_n(n) :
    if  not n :
        return
    print_to_n(n-1)
    print(n,end="")

if __name__ == '__main__':
    n = int(input())
    print_to_n(n)
