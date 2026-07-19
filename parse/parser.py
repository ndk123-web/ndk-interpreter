from ast_ndk.print_node import PrintNode
from ast_ndk.define_identifier import DefineIdentifierNode
from ast_ndk.addition_node import AdditionNode

from .parse_print import parse_print
from .parse_identifier import parse_identifier
from .parse_add import parser_addition


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
            
            if tokens[position + 4][0] == "+" or tokens[position + 4][0] == "-" or tokens[position + 4][0] == "*" or tokens[position + 4][0] == "/":
                identifier_name, value_of_identifier_1, value_of_identifier_2, pos = parser_addition(tokens, position)
                position = pos
                ast.append(AdditionNode(value_of_identifier_1, value_of_identifier_2, identifier_name))
                
            # if let a = 20 for here we dont need any addition or any other operation, so we will just parse it as a normal identifier and add it to the ast.
            
            
            
            else:
                identifier_name, value_of_identifier, pos = parse_identifier(
                tokens, position
                )
                position = pos
                ast.append(DefineIdentifierNode(identifier_name, value_of_identifier))

        else:
            raise Exception(f"Unexpected token: {tokens[position]}")

    # print("AST: \n", ast)
    return ast
