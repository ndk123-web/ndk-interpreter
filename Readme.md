# NDK Interpreter

NDK Interpreter ek small custom language project hai jo `.ndk` files ko read karke unko lex, parse, aur run karta hai. Iska goal simple language concepts ko clearly show karna hai, jaise tokenization, grammar checking, AST creation, aur interpretation.

## What It Does

Ye interpreter abhi ye cheezein support karta hai:

1. `string`, `int`, `float`, aur `double` declarations
2. arithmetic operations: `+`, `-`, `*`, `/`
3. direct string printing
4. global scope / global environment se variables print karna

## NDK Language Support Extension

Is project ke saath ek VS Code extension bhi hai: **ndk-language-support**.

- Extension name: `ndk-lang-support`
- Publisher: `ndkdev`
- Marketplace link: <https://marketplace.visualstudio.com/items?itemName=ndkdev.ndk-lang-support>

Ye extension `.ndk` files ke liye language support provide karta hai, including syntax highlighting aur basic editor support. Aap isse VS Code Marketplace se download aur install kar sakte ho.

## How It Works

Project ka flow simple hai:

`example.ndk` -> `lexer` -> `parser` -> `AST` -> `interpreter`

1. `lexer` source code ko tokens mein break karta hai.
2. `parser` tokens ko grammar rules ke against check karta hai.
3. `AST` har statement ko meaningful structure mein convert karta hai.
4. `interpreter` AST ko execute karke output deta hai.

Ye flow basically define karta hai ki language ka code kaise step by step process hota hai, bilkul small compiler/interpreter pipeline ki tarah.

## Example

```ndk
// Normal string printing in stdout
print("Hello I am ndk")

// declaring string and integers values
let a = 10;
let s = "hello this is string not print yet";

// arithmetic operations
let add = 20 + 10;
let sub = 20 - 10;
let mul = 1 * 3;
let div = 3 / 2;

// print variables from global environment
print(add);
print(s);
```

## Notes

- `.ndk` files are the source files for this language.
- Interpreter ka current design simple aur educational hai.
- VS Code extension use karke `.ndk` files ko easier way mein edit kiya ja sakta hai.
