# NDK Language Support

`ndk-language-support` is a VS Code extension that provides editor support for NDK language `.ndk` files.

## What It Is

This extension is mainly for the following:

1. Recognizing `.ndk` files
2. Providing syntax highlighting
3. Making NDK code easier to read and write in the editor
4. Improving the VS Code experience for the NDK language

## Install

You can install the extension from the VS Code Marketplace:

<https://marketplace.visualstudio.com/items?itemName=ndkdev.ndk-lang-support>

## How It Relates To The Interpreter

This extension is not a replacement for the interpreter. It only provides editor support.

- `ndk-language-support` = support for `.ndk` files in VS Code
- `ndk-interpreter` = the project that actually processes and runs `.ndk` code

## Language Flow

The processing flow for NDK code is generally:

`example.ndk` -> `lexer` -> `parser` -> `AST` -> `interpreter`

1. The `lexer` breaks source code into tokens.
2. The `parser` checks grammar and syntax rules.
3. The `AST` converts statements into a structured representation.
4. The `interpreter` executes that structure and produces output.

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

## Packaging

Use `vsce package` to generate the extension package. This creates a `.vsix` file, which can then be installed in VS Code.
