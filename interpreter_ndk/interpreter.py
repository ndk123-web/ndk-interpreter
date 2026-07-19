from ast_ndk.print_node import PrintNode
from ast_ndk.define_identifier import DefineIdentifierNode
from ast_ndk.addition_node import AdditionNode


class InterpreterNdk:

    def __init__(self):
        self.global_scope = {}

    def run(self, ast):

        for line in ast:
            if isinstance(line, PrintNode):
                print(line.value)

            elif isinstance(line, DefineIdentifierNode):
                self.global_scope[line.identifier_name] = line.value

            elif isinstance(line, AdditionNode):
                result = line.left + line.right
                self.global_scope[line.identifier_name] = result

            else:
                raise Exception(f"Unexpected AST node: {line}")

    def get_global_scope(self):
        return self.global_scope
