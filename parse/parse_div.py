def parser_division(tokens, position):
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

    value, value_of_identifier_1 = tokens[position]
    operand_1 = value_of_identifier_1 if value == "STRING" else value
    if value != "STRING" and value_of_identifier_1 != "NUMBER":
        raise Exception("String or Number required")
    position += 1

    value, _ = tokens[position]
    if value != "/" and value != "+" and value != "-" and value != "*":
        raise Exception("/, +, -, or * required")
    position += 1

    value, value_of_identifier_2 = tokens[position]
    operand_2 = value_of_identifier_2 if value == "STRING" else value
    if value != "STRING" and value_of_identifier_2 != "NUMBER":
        raise Exception("String or Number required")
    position += 1

    # Its Optional for delimiter to be present, so we check if it is there or not
    if position < len(tokens):
        value, _ = tokens[position]

        if value == ";":
            position += 1

        elif value == "\n":
            position += 1
    # EOF or next statement -> do nothing

    # identifier_name is ideenfier where the result of addition will be stored, value_of_identifier_1 is the first operand, value_of_identifier_2 is the second operand, and position is the current position in the tokens list after parsing the addition statement.
    return (identifier_name, operand_1, operand_2, position)
