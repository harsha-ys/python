if __name__ == '__main__':
    records = []
    low=100
    seclow=100
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        records.append([name,score])
        if score>low and score < seclow :
            seclow = score
        elif score < low:
            seclow=low
            low = score
    
    new_list=[x[0] for x in records if x[1]==seclow]
    new_list.sort()
    for x in new_list:
            print(x)
            
