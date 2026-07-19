from ast_ndk.print_node import PrintNode
from ast_ndk.define_identifier import DefineIdentifierNode
from ast_ndk.addition_node import AdditionNode
from ast_ndk.substraction_node import SubstractionNode
from ast_ndk.multiplication_node import MultiplicationNode
from ast_ndk.division_node import DivisionNode

class InterpreterNdk:

    def __init__(self):
        self.global_scope = {}

    def run(self, ast):

        for line in ast:
            
            if isinstance(line, PrintNode):
                # either normal string or identifier_name 
                if line.identifier is not None:
                    if line.identifier in self.global_scope:
                        print(self.global_scope[line.identifier])
                    else:
                        raise Exception(f"Undefined identifier: {line.identifier}")
                else:
                    print(line.value)

            elif isinstance(line, DefineIdentifierNode):
                self.global_scope[line.identifier_name] = line.value

            elif isinstance(line, AdditionNode):
                result = line.left + line.right
                self.global_scope[line.identifier_name] = result
            
            elif isinstance(line, SubstractionNode):
                result = line.left - line.right
                self.global_scope[line.identifier_name] = result
            
            elif isinstance(line, MultiplicationNode):
                result = line.left * line.right
                self.global_scope[line.identifier_name] = result
            
            elif isinstance(line, DivisionNode):
                if line.right == 0:
                    raise Exception("Division by zero is not allowed.")
                result = line.left / line.right
                self.global_scope[line.identifier_name] = result

            else:
                raise Exception(f"Unexpected AST node: {line}")

    def get_global_scope(self):
        return self.global_scope
