def minion_game(string):
    # your code goes here
    l=len(string)
    number_of_words = l*(l+1)/2
    vowels=['A', 'E', 'I', 'O', 'U']
    kevin = sum([ l-i for i in range(l) if string[i] in vowels ])
    stuart = number_of_words - kevin
    print( "Stuart " +str(int(stuart)) if stuart>kevin else "Kevin " +str(int(kevin)) if kevin>stuart else "Draw" )
    

