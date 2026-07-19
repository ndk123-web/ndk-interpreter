from .parse_add import parser_addition
from .parse_div import parser_division
from .parse_sub import parser_substraction
from .parse_mul import parser_multiply


def parse_arithmetics(tokens, position, arithmetic_operator):
    if arithmetic_operator == "+":
        return parser_addition(tokens, position)
    elif arithmetic_operator == "-":
        return parser_substraction(tokens, position)
    elif arithmetic_operator == "*":
        return parser_multiply(tokens, position)
    elif arithmetic_operator == "/":
        return parser_division(tokens, position)
    else:
        raise Exception(f"Unexpected arithmetic operator: {arithmetic_operator}")
