from lexer.read_string import read_string
from lexer.read_number import read_number

keywords = {
    "print": "PRINT",
    "(": "LPAREN",
    ")": "RPAREN",
    ";": "DELIMITER",
    "let": "LET",
    "=": "EQUAL",
    ",": "COMMA",
    ":": "COLON",
    "+": "PLUS",
    "-": "MINUS",
    "*": "MULTIPLY",
    "/": "DIVIDE",
}


def lexer(source_code: str):

    size = len(source_code)
    position = 0
    tokens = []
    word = ""

    while position < size:

        ch = source_code[position]

        if ch.isalpha():
            word += ch

        elif ch.isdigit():
            pos, digit_in_str = read_number(source_code, position)
            # print("NUMBER: ", digit_in_str)
            tokens.append((int(digit_in_str), "NUMBER"))
            position = pos
            continue

        if ch == '"':
            pos, w = read_string(source_code, position)
            tokens.append(("STRING", w))
            position = pos

        elif ch == "(":
            tokens.append((ch, keywords[ch]))

        elif ch == ")":
            tokens.append((ch, keywords[ch]))

        elif ch == ";":
            tokens.append((ch, keywords[ch]))

        elif ch == "=":
            tokens.append((ch, keywords[ch]))

        elif ch == ",":
            tokens.append((ch, keywords[ch]))

        elif ch == ":":
            tokens.append((ch, keywords[ch]))

        elif ch == "+":
            tokens.append((ch, keywords[ch]))

        elif word in keywords:
            tokens.append((word, keywords[word]))
            word = ""

        # if ch == " " and word != "" and word not in keywords: meaning that if we encounter a space and the word is not empty and the word is not a keyword, then we can consider it as an identifier. So we will add it to the tokens list as an identifier and reset the word to an empty string for the next token.
        elif ch == " " and word != "" and word not in keywords:

            # if the first character of the word is an alphabet or underscore, then we can consider it as an identifier. So we will add it to the tokens list as an identifier and reset the word to an empty string for the next token.
            if word[0].isalpha() or word[0] == "_":
                # print("IDENTIFIER: ", word)
                tokens.append((word, "IDENTIFIER"))
                word = ""

        position += 1

    # print(tokens)
    return tokens
