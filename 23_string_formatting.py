def print_formatted(number):
    # your code goes here
    sb = len( f"{number:b}" )+1  
    for i in range( 1,number + 1):print(f"{i:>{sb-1}d}{i:>{sb}o}{i:>{sb}X}{i:>{sb}b}")

