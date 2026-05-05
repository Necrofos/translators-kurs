lexer grammar SimplePythonLexer;

INT: 'int';
BOOL: 'bool';
CHAR_PTR: 'char' [ \t]* '*';
VOID: 'void';
STRUCT: 'struct';
RETURN: 'return';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
PRINTF: 'printf';
TRUE: 'true';
FALSE: 'false';

AND: '&&';
OR: '||';
EQ: '==';
NE: '!=';
LE: '<=';
GE: '>=';
LT: '<';
GT: '>';
ASSIGN: '=';
NOT: '!';
PLUS: '+';
MINUS: '-';
STAR: '*';
SLASH: '/';
PERCENT: '%';
COMMA: ',';
SEMICOLON: ';';
DOT: '.';
OPEN_PAREN: '(';
CLOSE_PAREN: ')';
OPEN_BRACE: '{';
CLOSE_BRACE: '}';

NAME: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
STRING: '"' (~["\\\r\n] | '\\' .)* '"';

LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
WS: [ \t\r\n]+ -> skip;
