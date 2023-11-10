grammar Bazilio;

root: procedure*;

procedure:
	PROCEDURE_NAME parameters LEFT_BAR instructions RIGHT_BAR;

instructions: instruction*;

instruction:
	assignment
	| input_
	| output_
	| reproduction
	| procedure_call
	| condition
	| while_
	| list_add
	| list_cut;

assignment: VAR '<-' expression;

input_: '<?>' VAR;

output_: '<w>' VAR;

reproduction: '(:)' expression;

parameters: VAR*;

condition:
	'if' expression LEFT_BAR instructions RIGHT_BAR (
		'else' LEFT_BAR instructions RIGHT_BAR
	)?;

while_: 'while' expression LEFT_BAR instructions RIGHT_BAR;

list: '{' expression* '}';

list_add: VAR '<<' expression;

list_cut: '8<' VAR LEFT_BRACKET expression RIGHT_BRACKET;

procedure_call: PROCEDURE_NAME procedure_call_parameters;

procedure_call_parameters: (expression)*;

expression:
	LEFT_PAREN expression RIGHT_PAREN	# Parenteses
	| expression MUL expression			# Mul
	| expression DIV expression			# Div
	| expression MOD expression			# Mod
	| expression ADD expression			# Add
	| expression SUB expression			# Sub
	| expression LT expression			# Lt
	| expression LTE expression			# Lte
	| expression GT expression			# Gt
	| expression GTE expression			# Gte
	| expression EQ expression			# Eq
	| expression NEQ expression			# Neq
	| VAR								# Var
	| NUM								# Value
	| STRING							# String
	| list_size							# ListSize
	| list_query						# ListQuery
	| NOTE								# Note;

list_size: '#' VAR;

list_query: VAR LEFT_BRACKET expression RIGHT_BRACKET;

// Arithmetic operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';

// Relational operators
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
EQ: '=';
NEQ: '/=';

NUM: '-'?[0-9]+;
VAR: [a-zA-Z][a-zA-Z0-9_]*;
PROCEDURE_NAME: [A-Z][a-zA-Z0-9_]*;
STRING: '"' ('\\' . | ~('\\' | '"'))* '"';
NOTE: [A-G][0-9]?;

LEFT_BAR: '|:';
RIGHT_BAR: ':|';
LEFT_BRACKET: '[';
RIGHT_BRACKET: ']';
LEFT_PAREN: '(';
RIGHT_PAREN: ')';

WS: [ \t\r\n]+ -> skip;
COMMENT: '###' ~[\r\n]* -> skip;