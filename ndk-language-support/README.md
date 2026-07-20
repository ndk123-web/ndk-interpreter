# Ndk-Interpreter

- It supports:
    1. string/int/float/double declarations
    2. arithmetic operations (+,-,/,*)
    3. can print normal string directly
    4. can print the variable that is in global enviroment/ global scope

## Flow

examples/example.ndk -> lexer (assigning tokens) -> parser (grammar & syntax checking) -> ast (converting each statement into meaning) -> Interpreter (takes each line and runs immediately same kind of like python does)

```ndk
// Normal string printing in stdout
print("Hello I am ndk")

// declaring string and integers values 
let a = 10;
let s = "hello this is string not print yet";

// arithmetic operations 
let add = 20+10;
let sub = 20-10;
let mul = 1*3;
let div = 3/2;

// print variables from global enviroment
print(add);
print(s);
```

# Code change

1. vsce package
    - bundles the vs extension into `vsix` like `zip` for folders

1. code --install-extension ndk-0.0.1.vsix --force
    - Extract all folders/files from `vsix` and paste into .vscode/extension/ folders so that it will work in real time vs code enviroment

# Reload VS Code
