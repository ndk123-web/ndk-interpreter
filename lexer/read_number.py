def read_number(source_code, position):
    size = len(source_code)
    word = ""

    while position < size:
        ch = source_code[position]

        # if the character is a digit or a dot, we add it to the word and increment the position
        if ch.isdigit() or ch == ".":
            word += ch
            position += 1

        else:
            break

    # print("NUMBER: ", word)
    return (position, word)
