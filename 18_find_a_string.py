def count_substring(string, sub_string):
    if len(string)==len(sub_string): return 1 if string == sub_string else 0
    return count_substring(string[1:],sub_string)+1 if string[:len(sub_string)]==sub_string else count_substring(string[1:],sub_string)
    

