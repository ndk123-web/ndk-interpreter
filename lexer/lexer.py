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

    def flush_word():
        nonlocal word
        if word == "":
            return

        if word in keywords:
            tokens.append((word, keywords[word]))
        elif word[0].isalpha() or word[0] == "_":
            tokens.append((word, "IDENTIFIER"))

        word = ""

    while position < size:

        ch = source_code[position]

        # if the character is a forward slash and the next character is also a forward slash, we have a comment, so we skip it
        if ch == "/" and position + 1 < size and source_code[position + 1] == "/":
            flush_word()
            position += 2

            while position < size and source_code[position] != "\n":
                position += 1

            continue

        if ch.isalpha():
            word += ch

        elif ch.isdigit():
            pos, digit_in_str = read_number(source_code, position)
            # print("NUMBER: ", digit_in_str)
            tokens.append((int(digit_in_str), "NUMBER"))
            position = pos
            continue

        elif ch in {
            " ",
            "\t",
            "\n",
            "\r",
            ")",
            "(",
            ";",
            "=",
            ",",
            ":",
            "+",
            "-",
            "*",
            "/",
        }:
            flush_word()

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

        elif ch == "-":
            tokens.append((ch, keywords[ch]))

        elif ch == "*":
            tokens.append((ch, keywords[ch]))

        elif ch == "/":
            tokens.append((ch, keywords[ch]))

        position += 1

    flush_word()

    # print(tokens)
    return tokens
