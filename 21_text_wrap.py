

def wrap(string, max_width):
    return string if len(string)<=max_width else string[:max_width]+"\n"+wrap(string[max_width:],max_width)

