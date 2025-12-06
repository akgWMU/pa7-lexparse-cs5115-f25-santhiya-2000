import ply.yacc as yacc
from lexer import tokens

# ------------------ AST NODE ------------------
class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

    def __repr__(self):
        return str(self.value)

# ------------------ GRAMMAR RULES ------------------

# Program -> PROGRAM id ; Decls CompoundStatement [ . ]
def p_program(p):
    '''Program : PROGRAM IDENTIFIER SEMI DeclSection CompoundStmt DotOpt'''
    p[0] = Node("PROGRAM", [Node(p[2]), p[4], p[5]])

# Optional final dot
def p_DotOpt(p):
    '''DotOpt : DOT
              | empty'''
    # ignored

# Decls -> VAR DeclList | empty
def p_DeclSection(p):
    '''DeclSection : VAR DeclList
                   | empty'''
    if len(p) == 3:
        p[0] = Node("DECLS", [p[2]])
    else:
        p[0] = Node("DECLS", [])

# DeclList -> IdentifierList : Type ; DeclList | IdentifierList : Type ;
def p_DeclList(p):
    '''DeclList : IdentifierList COLON Type SEMI DeclList
                | IdentifierList COLON Type SEMI'''
    decl_node = Node("DECL", [p[1], p[3]])  # DECL( IDLIST , TYPE )
    if len(p) == 6:
        p[0] = Node("DECLLIST", [decl_node, p[5]])
    else:
        p[0] = Node("DECLLIST", [decl_node])

# IdentifierList -> id | IdentifierList , id
def p_IdentifierList(p):
    '''IdentifierList : IDENTIFIER
                      | IdentifierList COMMA IDENTIFIER'''
    if len(p) == 2:
        p[0] = Node("IDLIST", [Node(p[1])])
    else:
        p[1].children.append(Node(p[3]))
        p[0] = p[1]

# Type -> INTEGER | FLOAT  (arrays can be added later)
def p_Type(p):
    '''Type : INTEGER
            | FLOAT'''
    p[0] = Node(f"TYPE:{p[1]}")

# CompoundStmt -> BEGIN StmtList END
def p_CompoundStmt(p):
    'CompoundStmt : BEGIN StmtList END'
    p[0] = Node("BEGIN-END", p[2])

# StmtList -> Statement | StmtList ; Statement
def p_StmtList(p):
    '''StmtList : Statement
                | StmtList SEMI Statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

# Statement -> Assignment | If | While | IO | CompoundStmt
def p_Statement(p):
    '''Statement : Assignment
                 | If
                 | While
                 | IO
                 | CompoundStmt'''
    p[0] = p[1]

# Variable -> IDENTIFIER   (no arrays yet)
def p_Variable(p):
    'Variable : IDENTIFIER'
    p[0] = Node(p[1])

# Assignment -> Variable := Expr
def p_Assignment(p):
    'Assignment : Variable ASSIGN Expr'
    p[0] = Node("ASSIGN", [p[1], p[3]])

# If -> IF Expr THEN Statement
#     | IF Expr THEN Statement ELSE Statement
def p_If(p):
    '''If : IF Expr THEN Statement
          | IF Expr THEN Statement ELSE Statement'''
    if len(p) == 5:
        p[0] = Node("IF", [p[2], p[4]])          # IF(cond, then)
    else:
        p[0] = Node("IF", [p[2], p[4], p[6]])    # IF(cond, then, else)

# While -> WHILE Expr DO Statement
def p_While(p):
    'While : WHILE Expr DO Statement'
    p[0] = Node("WHILE", [p[2], p[4]])

# IO -> READ ( Variable ) | WRITE ( Expr ) | WRITE ( STRING )
def p_IO(p):
    '''IO : READ LPAREN Variable RPAREN
          | WRITE LPAREN Expr RPAREN
          | WRITE LPAREN STRING RPAREN'''
    if p[1] == 'READ':
        p[0] = Node("READ", [p[3]])
    else:
        p[0] = Node("WRITE", [Node(p[3])])

# --------- EXPRESSIONS (simple & a bit ambiguous, but fine for PA7) ---------

def p_Expr_binop(p):
    '''Expr : Expr ARITH_OP Expr
            | Expr RELOP Expr'''
    p[0] = Node(p[2], [p[1], p[3]])

def p_Expr_logic(p):
    '''Expr : Expr AND Expr
            | Expr OR Expr'''
    p[0] = Node(p[2], [p[1], p[3]])

def p_Expr_not(p):
    'Expr : NOT Expr'
    p[0] = Node("NOT", [p[2]])

def p_Expr_paren(p):
    'Expr : LPAREN Expr RPAREN'
    p[0] = p[2]

def p_Expr_simple(p):
    '''Expr : CONSTANT
            | IDENTIFIER'''
    p[0] = Node(str(p[1]))

# Empty rule
def p_empty(p):
    'empty :'
    pass

# Error rule
def p_error(p):
    if p:
        print(f"Syntax Error at token {p.type}, value '{p.value}'")
    else:
        print("Syntax Error at EOF")

# Build parser
parser = yacc.yacc()
