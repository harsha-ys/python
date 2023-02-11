base_word=""

def create_base(size):
    global base_word
    for ch in range(size-1):base_word+= chr(97 + ch) +"-"
    base_word+=chr(96+size)

def print_rangoli(size):
    # your code goes here
    global base_word
    if not base_word : create_base(size)
    if (size ==1 ): print( base_word[1:][::-1] + base_word )
    else: 
        one = base_word[(size*2-2):]
        de = "-"*(size*2-2) + one[1:][::-1] + one + "-"*(size*2-2)  
        print(de)
        print_rangoli(size-1)
        print(de)
    
