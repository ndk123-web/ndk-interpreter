def read_string(source_code, position):
    size = len(source_code)
    word = ""

    position+=1
    while position < size and source_code[position] != '"':
        word+= source_code[position]
        position+=1 
    
    return (position, word)