if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    runup= -100
    winner= -100
    for x in arr : 
        if x>runup and x< winner :
            runup=x
        elif x> winner :
            runup=winner
            winner=x
    print(runup)
