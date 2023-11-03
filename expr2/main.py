import operator
from antlr4 import *
import unittest
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
from icecream import ic

ops = {'+' : operator.add, '-': operator.sub, '*' : operator.mul, '/' : operator.truediv, '^': operator.pow}



class EvalVisitor(ExprVisitor):

    def __init__(self) -> None:
        super().__init__()
        self.vars = {}

    def visitRoot(self, ctx:ExprParser.RootContext):
        l = list(ctx.getChildren())
        results = []
        for r in l:
            if isinstance(r, TerminalNode):
                continue
            result = self.visit(r)
            results.append(result)
        return results


    def visitAction(self, ctx:ExprParser.ActionContext):
        l = list(ctx.getChildren())
        
        if len(l) == 2:
            if l[0].getText() == 'write':
                var_name = l[1].getText()
                if var_name in self.vars:
                    return self.vars[var_name]
                return None
            else:
                raise ValueError('write not found')

        if len(l) == 3 and l[1].getText() == ':=':
            var_name = l[0].getText()
            var_value = self.visit(l[2])
            self.vars[var_name] = var_value
            return None
        else:
            raise ValueError('assigment not found')


    def visitExpr(self, ctx:ExprParser.ExprContext):
        l = list(ctx.getChildren())
        
        if len(l) == 1:
            return int(l[0].getText())
        
        expr_operator = ops[l[1].getText()]
        return expr_operator(self.visit(l[0]), self.visit(l[2]))

            
class TestEvalVisitor(unittest.TestCase):

    def run_one(self, input_data: str, expected: int):
        input_stream = InputStream(input_data)

        lexer = ExprLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = ExprParser(token_stream)
        tree = parser.root()

        visitor = EvalVisitor()
        value = visitor.visit(tree)
        self.assertEqual(value, expected)

    def test_sum(self):
        self.run_one('x := 1 + 1 write x', [None, 2])
        self.run_one('write x', [None])
        self.run_one('x := 1 + 1 write x write x', [None, 2, 2])
        self.run_one('billabong := 1 ^ 2 + 1 / 1 * 1 - 1 write billabong', [None, 1])
        self.run_one('billabong := 1 + 1 - 1 * 1 / 1 write billabong', [None, 1])
       
if __name__ == '__main__':
    unittest.main()