# NDK Language Support

`ndk-language-support` ek VS Code extension hai jo NDK language ke `.ndk` files ke liye editor support provide karta hai.

## What It Is

Ye extension mainly in cheezon ke liye hai:

1. `.ndk` files ko recognize karna
2. syntax highlighting dena
3. editor mein NDK code ko easier read aur write karna
4. NDK language ke saath VS Code experience ko better banana

## Install

Extension ko VS Code Marketplace se install kiya ja sakta hai:

<https://marketplace.visualstudio.com/items?itemName=ndkdev.ndk-lang-support>

## How It Relates To The Interpreter

Ye extension interpreter ka replacement nahi hai. Ye sirf editor support hai.

- `ndk-language-support` = VS Code mein `.ndk` files ke liye support
- `ndk-interpreter` = `.ndk` code ko actually process aur run karne wala project

## Language Flow

NDK code ka processing flow generally ye hota hai:

`example.ndk` -> `lexer` -> `parser` -> `AST` -> `interpreter`

1. `lexer` source code ko tokens mein todta hai.
2. `parser` grammar aur syntax rules check karta hai.
3. `AST` statements ko structured representation mein convert karta hai.
4. `interpreter` us structure ko execute karke output deta hai.

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

## Packaging

Extension package banane ke liye `vsce package` use hota hai. Isse `.vsix` file generate hoti hai, jise VS Code mein install kiya ja sakta hai.
