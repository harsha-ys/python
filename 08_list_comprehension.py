if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    list=[[x1,y1,z1]  for x1 in range(x+1) for y1 in  range(y+1) for z1 in range(z+1) if ((x1+y1+z1) != n) ]
    print(list)
