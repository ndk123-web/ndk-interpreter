from lexer.lexer import lexer
from parse.parser import parser
from interpreter_ndk.interpreter import InterpreterNdk
import sys

if __name__ == "__main__":

    if len(sys.argv) > 1:

        # might be run
        command = sys.argv[1]

        # get file path/ file name in current directory
        file_path = sys.argv[2]

        if not file_path.endswith(".ndk"):
            print("Error: File must have a .ndk extension")
            sys.exit(1)

        if command == "run" and len(sys.argv) == 3:

            with open(file_path, "r") as f:

                source_code = f.read()
                tokens = lexer(source_code=source_code)
                # print("Tokens: ", tokens)

                ast = parser(tokens)
                # print("AST: ", ast)

                ipr = InterpreterNdk()
                ipr.run(ast)

                # print()
                # print()
                # print()
                # print()
                # print("Global Scope: ", ipr.get_global_scope())
