import { registerCompletion } from './completion.js';
import * as vscode from "vscode";

export function activate(context: vscode.ExtensionContext) {
    registerCompletion(context);
}