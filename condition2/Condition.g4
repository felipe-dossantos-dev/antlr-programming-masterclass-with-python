grammar Condition; 

root:  action+ EOF;

action: 'iff' expr action ('otherwise' action)? # Condition
      | 'write' expr                            # Print
      | 'next' expr                             # Next
      ;
      

expr: expr LT expr   # Lt
    | expr GT expr   # Gt
    | expr EQ expr   # Eq
    | expr NEQ expr  # Neq
    | expr ADD expr  # Sum 
    | NUM            # Value
    ;

LT: '<';
GT: '>';
EQ: '==';
NEQ: '!=';
ADD: '+';

NUM: [0-9]+;

WS: [ \t\r\n] -> skip;