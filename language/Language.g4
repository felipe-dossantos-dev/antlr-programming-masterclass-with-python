grammar Language;

root: inss EOF;

inss: ins*;

ins: (assign | output | while_);

output: 'send' expr;

assign: VAR ASSIGN expr;

while_: 'while' expr inss;

expr:
	expr ADD expr	# Sum
	| expr SUB expr	# Sub
	| expr LT expr	# Lt
	| expr GT expr	# Gt
	| expr EQ expr	# Eq
	| expr NEQ expr	# Neq
	| VAR			# Var
	| NUM			# Value;

ADD: '+';
SUB: '-';
LT: '<';
GT: '>';
EQ: '==';
NEQ: '!=';

NUM: [0-9]+;
VAR: [a-zA-Z][a-zA-Z0-9]*;
ASSIGN: '<-';

WS: [ \t\r\n]+ -> skip;