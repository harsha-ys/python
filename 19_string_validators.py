def check(string,L,already_changed):
    if string =="" : return L
    if len(set(already_changed))==1 and already_changed[0]: return L
    if not already_changed[0] :
        if string[0].isalnum() :
            L[0] = True 
            already_changed[0] = True     
    if not already_changed[1] : 
        if string[0].isalpha() :
            L[1] = True 
            already_changed[1] = True 
    if not already_changed[2] : 
        if string[0].isdigit() :
            L[2] = True 
            already_changed[2] = True 
    if not already_changed[3] : 
        if string[0].islower() :
            L[3] = True 
            already_changed[3] = True 
    if not already_changed[4] : 
        if string[0].isupper() :
            L[4] = True 
            already_changed[4] = True 
    return check(string[1:],L,already_changed)
    

if __name__ == '__main__':
    s = input()   
    already_changed =[False, False, False, False, False]
    L=[False, False, False, False, False]
    
    a= check(s,L,already_changed)
    print (a[0])
    print (a[1])
    print (a[2])
    print (a[3])
    print (a[4])
