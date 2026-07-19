from lexer.lexer import lexer
from parse.parser import parser
from interpreter_ndk.interpreter import InterpreterNdk

if __name__ == "__main__":

    with open("examples/example.ndk", "r") as f:
        source_code = f.read()
        tokens = lexer(source_code=source_code)
        print("Tokens: ", tokens)

        print() 
        
        ast = parser(tokens)
        print("AST: ", ast)

        print() 
        
        ipr = InterpreterNdk()
        ipr.run(ast)

        print("Global Scope: ", ipr.get_global_scope())
