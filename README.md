# CS 5115 – PA7: SomeWMULife Lexical Analyzer & Parser

This project implements:

1. A **lexical analyzer** (lexer) for the `SomeWMULife` language using **PLY (Python Lex-Yacc)**.
2. A **parser** that builds an **Abstract Syntax Tree (AST)** and prints a **level-order traversal** of the tree, with nodes in each level separated by `#` and a blank line between levels. :contentReference[oaicite:0]{index=0}  

The language specification is based on the official **SomeWMULife language description** (a small Pascal-like language with `INTEGER` and `FLOAT`, arrays, `IF/THEN/ELSE`, `WHILE`, `READ`, `WRITE`, etc.). :contentReference[oaicite:1]{index=1}  

Assignment: **Programming Assignment 7 – Lexical Analysis & Parsing, CS 5115 Fall 2025**. :contentReference[oaicite:2]{index=2}  

---

## 1. Project Structure

Suggested folder layout:

```text
.
├── lexer.py          # PLY-based lexical analyzer for SomeWMULife
├── parser.py         # PLY-based parser + AST construction
├── ast_utils.py      # (optional) shared Node & traversal helpers
├── test_lexer.py     # script to run lexer on an input file
├── test_parser.py    # script to run parser and print AST levels
├── test.wmu          # sample SomeWMULife program for testing
└── README.md




Typescript:
Hi, I’m going to walk through my solution for CS 5115 Programming Assignment 7, which is the lexical analyzer and parser for the SomeWMULife language.

The goal of this assignment is to implement a lexer and parser for a small Pascal-like language called SomeWMULife, using PLY in Python. The language supports two basic data types, INTEGER and FLOAT, one-dimensional arrays, control flow like IF–THEN–ELSE and WHILE–DO, as well as READ and WRITE statements, and comments enclosed in curly braces.

Project structure:
In my project directory, I have:

lexer.py – the lexical analyzer implemented with PLY’s lex module.

parser.py – the parser and AST construction using PLY’s yacc module.

ast_utils.py – a helper file with the Node class and a level-order traversal function for printing the AST.

test_lexer.py – a small driver script to run the lexer on a source file and print tokens.

test_parser.py – a driver script to parse a source file and print the AST in the required format.

And one or more .wmu files, such as test.wmu, which contain sample SomeWMULife programs.

How to run the lexer:
First, after installing PLY with pip install ply, we can run the lexical analyzer using:

python test_lexer.py

The test_lexer.py script opens test.wmu, sends the source code to the lexer, and then repeatedly calls lexer.token() until there are no more tokens. Each token is printed in the form (TYPE, value).

In the output, we can see:

Keywords like PROGRAM, VAR, BEGIN, END, IF, WHILE, and WRITE recognized as reserved words.

Identifiers that start with a letter and may contain letters and digits.

Integer and floating-point constants.

Arithmetic operators such as +, -, *, and /.

Relational and logical operators such as =, <, >, <=, >=, <>, AND, OR, and NOT.

Separators including parentheses, brackets, commas, semicolons, colons, and dots.

Comments inside { ... } are recognized but ignored, so they do not appear as tokens in the output.

This confirms that the lexical analyzer correctly implements the token categories specified in the assignment and the SomeWMULife language spec.

How to run the parser and AST:
Next, the parser in parser.py uses the same tokens to recognize the grammar of SomeWMULife and build an Abstract Syntax Tree. The rules correspond to the official BNF for PROGRAM, declarations, compound statements, assignments, IF statements, WHILE loops, and expressions.

To run the parser, I use:

python test_parser.py

This script again reads test.wmu, calls parser.parse, and receives the root of the AST. I then call a helper function that performs a level-order traversal of the tree. Each level is printed on its own line, with nodes separated by the # symbol, and a blank line between levels. This matches the required output format for the assignment.

At the top level, we see a PROGRAM node with children for the program identifier, the declarations, and the main BEGIN–END compound statement. Below that, we see nodes for individual declarations, assignments, READ and WRITE statements, and expression subtrees. By examining a few test inputs, we can verify that the structure of the AST matches the intended grammar of the SomeWMULife language.

Testing and validation:
I tested my implementation with several .wmu files that include simple arithmetic, nested IF statements, WHILE loops, and array declarations. For each test program, I first ran the lexer to confirm that every token is recognized correctly, and then ran the parser to make sure no syntax errors occur and that the resulting AST prints in the correct level-order format.

Overall, this project demonstrates a complete pipeline from source code to token stream to parse tree for the SomeWMULife language, following the specifications of PA7 and using PLY for both lexical analysis and parsing.

That concludes my demo. Thank you.