# NDK Interpreter

NDK Interpreter is a small custom language project that reads `.ndk` files and processes them through lexical analysis, parsing, and execution. Its goal is to clearly demonstrate simple language concepts such as tokenization, grammar checking, AST creation, and interpretation.

## What It Does

This interpreter currently supports:

1. `string`, `int`, `float`, aur `double` declarations
2. arithmetic operations: `+`, `-`, `*`, `/`
3. direct string printing
4. printing variables from the global scope / global environment

## NDK Language Support Extension

This project also includes a VS Code extension: **ndk-language-support**.

- Extension name: `ndk-lang-support`
- Publisher: `ndkdev`
- Marketplace link: <https://marketplace.visualstudio.com/items?itemName=ndkdev.ndk-lang-support>

This extension provides language support for `.ndk` files, including syntax highlighting and basic editor support. You can download and install it from the VS Code Marketplace.

## How It Works

The project flow is simple:

`example.ndk` -> `lexer` -> `parser` -> `AST` -> `interpreter`

1. The `lexer` breaks source code into tokens.
2. The `parser` checks the tokens against grammar rules.
3. The `AST` converts each statement into a meaningful structure.
4. The `interpreter` executes the AST and produces output.

This flow shows how language code is processed step by step, similar to a small compiler/interpreter pipeline.

## Example

```ndk
// Normal string printing in stdout
print("Hello I am ndk")

// declaring string and integer values
let a = 10;
let s = "hello this is string not print yet";

// arithmetic operations
let add = 20 + 10;
let sub = 20 - 10;
let mul = 1 * 3;
let div = 3 / 2;

// print variables from the global environment
print(add);
print(s);
```

## Notes

- `.ndk` files are the source files for this language.
- The interpreter is intentionally simple and educational.
- You can use the VS Code extension to edit `.ndk` files more easily.
