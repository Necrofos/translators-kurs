parser grammar SimplePythonParser;

options {
    tokenVocab=SimplePythonLexer;
}

program
    : declaration* EOF
    ;

declaration
    : structDefinition
    | functionDefinition
    | statement
    ;

statement
    : variableDeclaration SEMICOLON
    | assignment SEMICOLON
    | printfStatement SEMICOLON
    | returnStatement SEMICOLON
    | expressionStatement SEMICOLON
    | ifStatement
    | whileStatement
    | block
    ;

variableDeclaration
    : typeSpecifier NAME (ASSIGN expression)?
    ;

assignment
    : assignmentTarget ASSIGN expression
    ;

printfStatement
    : PRINTF OPEN_PAREN argumentList? CLOSE_PAREN
    ;

returnStatement
    : RETURN expression?
    ;

expressionStatement
    : expression
    ;

ifStatement
    : IF OPEN_PAREN expression CLOSE_PAREN block (ELSE block)?
    ;

whileStatement
    : WHILE OPEN_PAREN expression CLOSE_PAREN block
    ;

functionDefinition
    : functionReturnType NAME OPEN_PAREN parameterList? CLOSE_PAREN block
    ;

functionReturnType
    : typeSpecifier
    | VOID
    ;

typeSpecifier
    : INT
    | BOOL
    | CHAR_PTR
    | STRUCT NAME
    ;

structDefinition
    : STRUCT NAME OPEN_BRACE structFieldDeclaration* CLOSE_BRACE SEMICOLON
    ;

structFieldDeclaration
    : typeSpecifier NAME SEMICOLON
    ;

parameterList
    : parameter (COMMA parameter)*
    ;

parameter
    : typeSpecifier NAME
    ;

argumentList
    : expression (COMMA expression)*
    ;

block
    : OPEN_BRACE statement* CLOSE_BRACE
    ;

expression
    : orExpression
    ;

orExpression
    : andExpression (OR andExpression)*
    ;

andExpression
    : notExpression (AND notExpression)*
    ;

notExpression
    : NOT notExpression
    | comparison
    ;

comparison
    : additiveExpression ((EQ | NE | LT | GT | LE | GE) additiveExpression)*
    ;

additiveExpression
    : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*
    ;

multiplicativeExpression
    : unaryExpression ((STAR | SLASH | PERCENT) unaryExpression)*
    ;

unaryExpression
    : MINUS unaryExpression
    | primary
    ;

primary
    : literal
    | functionCall
    | fieldAccess
    | NAME
    | OPEN_PAREN expression CLOSE_PAREN
    ;

functionCall
    : NAME OPEN_PAREN argumentList? CLOSE_PAREN
    ;

fieldAccess
    : NAME (DOT NAME)+
    ;

assignmentTarget
    : NAME (DOT NAME)*
    ;

literal
    : NUMBER
    | STRING
    | TRUE
    | FALSE
    ;
