import * as vscode from "vscode";

const printItem = new vscode.CompletionItem(
    "print",
    vscode.CompletionItemKind.Function
);
printItem.insertText = new vscode.SnippetString(
    'print("$1");'
);

const letItem = new vscode.CompletionItem(
    "let",
    vscode.CompletionItemKind.Keyword
);

export function registerCompletion(context: vscode.ExtensionContext) {
    const provider = vscode.languages.registerCompletionItemProvider(
        "ndk",
        {
            provideCompletionItems() {
                return [
                    printItem,
                    letItem
                ];
            }
        }
    );

    context.subscriptions.push(provider);
}