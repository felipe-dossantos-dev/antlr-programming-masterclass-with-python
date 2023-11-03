from antlr4 import *
import unittest
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor


class EvalVisitor(ExprVisitor):

    def __init__(self) -> None:
        super().__init__()

    def visitRoot(self, ctx:ExprParser.RootContext):
        r = next(ctx.getChildren())
        return self.visit(r)

    # version without labels
    # def visitExpr(self, ctx:ExprParser.ExprContext):
    #     l = list(ctx.getChildren())
    #     if len(l) == 1:
    #         return int(l[0].getText())
    #     else:
    #         if l[1].getText() == '+':
    #             return self.visit(l[0]) + self.visit(l[2])
    #         else:
    #             return self.visit(l[0]) - self.visit(l[2])

    def visitSub(self, ctx:ExprParser.SubContext):
        l = list(ctx.getChildren())
        return self.visit(l[0]) - self.visit(l[2])


    def visitSum(self, ctx:ExprParser.SumContext):
        l = list(ctx.getChildren())
        return self.visit(l[0]) + self.visit(l[2])
    
    def visitMul(self, ctx:ExprParser.MulContext):
        l = list(ctx.getChildren())
        return self.visit(l[0]) * self.visit(l[2])

    def visitValue(self, ctx:ExprParser.ValueContext):
        v = next(ctx.getChildren())
        return int(v.getText())
    
    def visitDiv(self, ctx:ExprParser.DivContext):
        l = list(ctx.getChildren())
        return self.visit(l[0]) / self.visit(l[2])

            
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
        self.run_one('1+2', 3)
        self.run_one('111+222', 333)
        self.run_one('0+0', 0)
        self.run_one('0', 0)

    def test_subtract(self):
        self.run_one('1-2', -1)
        self.run_one('111-222', -111)
        self.run_one('1-1-1-1-1', -3)
        self.run_one('0-0', 0)
        self.run_one('0', 0)

    def test_mul(self):
        self.run_one('1*2', 2)
        self.run_one('1+2*3', 7)
        self.run_one('1*2*3-1', 5)
        self.run_one('1*1*1*1', 1)
        self.run_one('0*0', 0)

    def test_div(self):
        self.run_one('2/2', 1)
        self.run_one('1+2/2', 2)
        self.run_one('2*2/4', 1)
        self.run_one('1/1/1/1', 1)
        self.run_one('2*2/2*2', 1)

if __name__ == '__main__':
    unittest.main()