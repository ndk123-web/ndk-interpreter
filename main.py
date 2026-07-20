from lexer.lexer import lexer
from parse.parser import parser
from interpreter_ndk.interpreter import InterpreterNdk

if __name__ == "__main__":

    with open("examples/example.ndk", "r") as f:
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