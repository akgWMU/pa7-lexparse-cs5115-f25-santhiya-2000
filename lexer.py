import ply.lex as lex

# ------------------ RESERVED KEYWORDS ------------------
reserved = {
    'AND': 'AND',
    'ARRAY': 'ARRAY',
    'BEGIN': 'BEGIN',
    'DO': 'DO',
    'ELSE': 'ELSE',
    'END': 'END',
    'FLOAT': 'FLOAT',
    'IF': 'IF',
    'INTEGER': 'INTEGER',
    'NOT': 'NOT',
    'OR': 'OR',
    'PROGRAM': 'PROGRAM',
    'READ': 'READ',
    'THEN': 'THEN',
    'VAR': 'VAR',
    'WHILE': 'WHILE',
    'WRITE': 'WRITE',
}

# ------------------ TOKEN LIST ------------------
tokens = [
    'ASSIGN',       # :=
    'IDENTIFIER',
    'CONSTANT',     # int or float (simplified)
    'STRING',       # 'abc'
    'ARITH_OP',     # + - * /
    'RELOP',        # < <= > >= = <>

    # Separators
    'LPAREN', 'RPAREN',
    'LBRACK', 'RBRACK',
    'COMMA', 'SEMI', 'COLON', 'DOT',
] + list(reserved.values())

# ------------------ IGNORE WHITESPACE ------------------
t_ignore = ' \t\r'

# ------------------ TOKENS ------------------

# Assignment operator (must be before ':' and '=')
t_ASSIGN   = r':='

# Arithmetic operators
t_ARITH_OP = r'[\+\-\*/]'

# Relational operators
t_RELOP    = r'<=|>=|<>|<|>|='

# Separators
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_LBRACK   = r'\['
t_RBRACK   = r'\]'
t_COMMA    = r','
t_SEMI     = r';'
t_COLON    = r':'
t_DOT      = r'\.'

# String constants: 'abc'
t_STRING   = r'\'[A-Za-z]*\''

# Numbers: integer or float (simplified)
def t_CONSTANT(t):
    r'\d+(\.\d+([eE][+-]?\d+)?)?'
    return t

# Identifiers / keywords
def t_IDENTIFIER(t):
    r'[A-Za-z][A-Za-z0-9]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

# Comments: { ... } (non-nested)
def t_COMMENT(t):
    r'\{[^}]*\}'
    pass  # ignore

# Newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handler
def t_error(t):
    print(f"Lexical Error: Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Build lexer
lexer = lex.lex()
