grammar pseudocode;

IF: 'if';
WHILE: 'while';
FOR: 'for';
ELSE: 'else';
ASSIGN: ':=';
IS: 'is';
RETURN: 'return';
SKIP_TOKEN: 'skip';
NOT: 'not';
FUNCTION: 'function';
C_BRACKET_OPEN: '{';
C_BRACKET_CLOSE: '}';
R_BRACKET_OPEN: '(';
R_BRACKET_CLOSE: ')';
S_BRACKET_OPEN: '[';
S_BRACKET_CLOSE: ']';
MATH_SYM: '+' | '-' | '*' | '/' | '%' | '^';
COMMA: ',';
WHITESPACE: [ \t\r\n] -> skip;
ID: ([a-zA-Z]) ([a-zA-Z0-9] | '_')*;
NUMBER: ('-')?[0-9]+;
SEMICOLON: ';';
STRING: '"'[a-zA-Z0-9 \t\r\n]+'"';
COMPARE_SYM: '=' | '>=' | '<=' | '<' | '>' | '!=';
DIVISIBLE: 'divisible';
FROM: 'from';
TO: 'to';
BOOL: 'true' | 'false';
BY: 'by';
AND: 'and';
OR: 'or';

program: statement* EOF;

increment: ID ASSIGN (ID|NUMBER) MATH_SYM (ID|NUMBER) SEMICOLON;

array: S_BRACKET_OPEN (type(COMMA type)*)? S_BRACKET_CLOSE;

type: (ID|STRING|NUMBER|BOOL);

declaration: ID (S_BRACKET_OPEN NUMBER S_BRACKET_CLOSE)? ASSIGN type SEMICOLON;

if_statement:IF R_BRACKET_OPEN expr R_BRACKET_CLOSE C_BRACKET_OPEN (statement)* C_BRACKET_CLOSE;

for_statement: FOR R_BRACKET_OPEN ID ASSIGN NUMBER NUMBER R_BRACKET_CLOSE C_BRACKET_OPEN (statement)* C_BRACKET_CLOSE (ELSE C_BRACKET_OPEN (statement)+ C_BRACKET_CLOSE)?;

while_statement: WHILE R_BRACKET_OPEN expr R_BRACKET_CLOSE C_BRACKET_OPEN (statement)* C_BRACKET_CLOSE;

statement: (function|increment|for_statement|while_statement|declaration|function_def);

expr:NOT? (type|divisibility) (AND|OR|MATH_SYM|COMPARE_SYM)(type|expr|divisibility);

divisibility: (ID|NUMBER) IS DIVISIBLE BY NUMBER;

return_statement: RETURN type SEMICOLON;

function_def: FUNCTION ID R_BRACKET_OPEN ((ID)(COMMA ID)*)? R_BRACKET_CLOSE C_BRACKET_OPEN (statement)* (return_statement)? C_BRACKET_CLOSE;

function: ID R_BRACKET_OPEN ((ID|NUMBER)(COMMA (ID|NUMBER))*) R_BRACKET_CLOSE ;

array_elem: ID S_BRACKET_OPEN type S_BRACKET_CLOSE;




