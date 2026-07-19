def parse_identifier(tokens, position):

    value, _ = tokens[position]
    if value != "let":
        raise Exception("let required")
    position += 1

    identifier_name, token_type = tokens[position]
    if token_type != "IDENTIFIER":
        raise Exception("Identifier required")
    position += 1

    value, _ = tokens[position]
    if value != "=":
        raise Exception("= required")
    position += 1

    value, value_of_identifier = tokens[position]
    if value != "STRING" and value_of_identifier != "NUMBER":
        raise Exception("String or Number required")

    literal_value = value_of_identifier if value == "STRING" else value
    position += 1

    # Its Optional for delimiter to be present, so we check if it is there or not
    if position < len(tokens):
        value, _ = tokens[position]

        if value == ";":
            position += 1

        elif value == "\n":
            position += 1
    # EOF or next statement -> do nothing

    return (identifier_name, literal_value, position)
