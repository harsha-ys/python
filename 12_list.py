if __name__ == '__main__':
    N = int(raw_input())
    L=[]
    while N>0:
        a = raw_input()
        if a.split()[0] == "insert" : L.insert(int(a.split()[1]),int(a.split()[2])) 
        elif a.split()[0] == "print": print(L) 
        elif a.split()[0] == "remove": L.remove(int(a.split()[1]))  
        elif a.split()[0] == "append": L.append(int(a.split()[1]))  
        elif a.split()[0] == "sort": L.sort()  
        elif a.split()[0] == "pop":  L.pop() 
        elif a.split()[0] == "reverse": L.reverse() 
        N -=1
