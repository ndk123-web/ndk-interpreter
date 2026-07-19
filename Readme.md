# Ndk-Interpreter

- It supports:
    1. string/int/float/double declarations
    2. arithmetic operations (+,-,/,*)
    3. can print normal string directly
    4. can print the variable that is in global enviroment/ global scope

## Flow

examples/example.ndk -> lexer (assigning tokens) -> parser (grammar & syntax checking) -> ast (converting each statement into meaning) -> Interpreter (takes each line and runs immediately same kind of like python does)
