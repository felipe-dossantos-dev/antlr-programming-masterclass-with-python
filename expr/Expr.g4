grammar Expr;

root: expr EOF;

// tem prioridade de ordem
expr: expr MUL expr # mul
    | expr DIV expr   # div
    | expr PLUS expr # sum 
    | expr SUB expr # sub 
    | NUM # value;

NUM: [0-9]+;
PLUS: '+';
SUB: '-';
MUL: '*';
DIV: '/';
WS: [ \n] -> skip;