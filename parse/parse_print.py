def parse_print(tokens, position):
    value, _ = tokens[position]

    if value != "print":
        raise Exception("print required")
    position += 1

    value, _ = tokens[position]
    if value != "(":
        raise Exception("( required")
    position += 1

    value, string_value = tokens[position]
    if value != "STRING":
        raise Exception("String required")

    position += 1

    value, _ = tokens[position]
    if value != ")":
        raise Exception(") required")

    position += 1

    # Its Optional for delimiter to be present, so we check if it is there or not
    if position < len(tokens):
        value, _ = tokens[position]

        if value == ";":
            position += 1

        elif value == "\n":
            position += 1

    # EOF or next statement -> do nothing

    return (string_value, position)
