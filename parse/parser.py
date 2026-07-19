from ast_ndk.print_node import PrintNode
from ast_ndk.define_identifier import DefineIdentifierNode
from ast_ndk.addition_node import AdditionNode
from ast_ndk.substraction_node import SubstractionNode
from ast_ndk.multiplication_node import MultiplicationNode
from ast_ndk.division_node import DivisionNode

from .parse_print import parse_print
from .parse_identifier import parse_identifier
from .parse_arithmetics import parse_arithmetics


def parser(tokens):
    ast = []
    size = len(tokens)
    position = 0

    while position < size:
        if tokens[position][0] == "print":
            s, pos = parse_print(tokens, position)
            position = pos
            ast.append(PrintNode(s))

        elif tokens[position][0] == "let":
            operator_position = position + 4

            if operator_position < size and tokens[operator_position][0] in {"+", "-", "*", "/"}:
                arithmetic_operator = tokens[operator_position][0]
                identifier_name, value_of_identifier_1, value_of_identifier_2, pos = parse_arithmetics(
                    tokens, position, arithmetic_operator
                )
                position = pos

                if arithmetic_operator == "+":
                    ast.append(AdditionNode(value_of_identifier_1, value_of_identifier_2, identifier_name))
                elif arithmetic_operator == "-":
                    ast.append(SubstractionNode(value_of_identifier_1, value_of_identifier_2, identifier_name))
                elif arithmetic_operator == "*":
                    ast.append(MultiplicationNode(value_of_identifier_1, value_of_identifier_2, identifier_name))
                elif arithmetic_operator == "/":
                    ast.append(DivisionNode(value_of_identifier_1, value_of_identifier_2, identifier_name))

            else:
                identifier_name, value_of_identifier, pos = parse_identifier(tokens, position)
                position = pos
                ast.append(DefineIdentifierNode(identifier_name, value_of_identifier))

        else:
            raise Exception(f"Unexpected token: {tokens[position]}")

    return ast
                            

