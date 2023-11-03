from antlr4 import *
import unittest
from ConditionLexer import ConditionLexer
from ConditionParser import ConditionParser
from ConditionVisitor import ConditionVisitor
from icecream import ic


class EvalVisitor(ConditionVisitor):
    def __init__(self) -> None:
        super().__init__()

    def visitRoot(self, ctx: ConditionParser.RootContext):
        results = []
        for r in ctx.getChildren():
            if isinstance(r, TerminalNode):
                continue
            result = self.visit(r)
            if result is not None:
                results.extend(result)
        return results

    def visitCondition(self, ctx: ConditionParser.ConditionContext):
        first_expr = self.visit(ctx.expr())
        if first_expr == 1:
            return self.visit(ctx.action(0))
        elif ctx.getChildCount() > 3 and ctx.getChild(3).getText() == 'otherwise':
            return self.visit(ctx.action(1))

    def visitPrint(self, ctx: ConditionParser.PrintContext):
        results = []
        for r in ctx.getChildren():
            if isinstance(r, TerminalNode):
                continue
            result = self.visit(r)
            results.append(result)
        return results
    
    def visitNext(self, ctx:ConditionParser.NextContext):
        results = []
        for r in ctx.getChildren():
            if isinstance(r, TerminalNode):
                continue
            result = self.visit(r) + 1
            results.append(result)
        return results

    def visitValue(self, ctx: ConditionParser.ValueContext):
        return int(ctx.NUM().getText())

    def visitLt(self, ctx: ConditionParser.LtContext):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return 1 if left < right else 0

    def visitGt(self, ctx: ConditionParser.GtContext):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return 1 if left > right else 0


    def visitSum(self, ctx:ConditionParser.SumContext):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return left + right


    def visitNeq(self, ctx:ConditionParser.NeqContext):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return 1 if left != right else 0


    def visitEq(self, ctx:ConditionParser.EqContext):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return 1 if left == right else 0


class TestEvalVisitor(unittest.TestCase):
    def run_one(self, input_data: str, expected: int):
        input_stream = InputStream(input_data)

        lexer = ConditionLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = ConditionParser(token_stream)
        tree = parser.root()

        visitor = EvalVisitor()
        value = visitor.visit(tree)
        self.assertEqual(value, expected)

    def test_write_value(self):
        self.run_one("write 5", [5])
        self.run_one("write 99999 write 1", [99999, 1])
    
    def test_next_value(self):
        self.run_one("next 5", [6])
        self.run_one("next 99999 next 1", [100000, 2])

    def test_greater_than(self):
        self.run_one("write 5 > 6", [0])
        self.run_one("write 7 > 5", [1])

    def test_less_than(self):
        self.run_one("write 5 < 6", [1])
        self.run_one("write 7 < 6", [0])

    def test_sum_than(self):
        self.run_one("write 5 + 6", [11])
        self.run_one("write 7 + 3", [10])

    def test_neq_than(self):
        self.run_one("write 5 != 6", [1])
        self.run_one("write 7 != 7", [0])

    def test_eq_than(self):
        self.run_one("write 5 == 5", [1])
        self.run_one("write 7 == 6", [0])

    def test_condition(self):
        self.run_one("iff 7 > 2 write 3", [3])
        self.run_one("iff 7 < 2 write 3 otherwise next 4", [5])
        self.run_one("iff 7 != 2 write 3 otherwise next 4", [3])
        self.run_one("iff 7 == 2 write 3 otherwise next 4", [5])
        self.run_one("iff 7 > 2 write 3 > 4 otherwise next 4", [0])
        self.run_one("iff 7 > 2 write 3 < 4 otherwise next 4", [1])
        self.run_one("iff 3 > 6 write 8 otherwise next 9 + 5", [15])
        self.run_one("iff 3 == 3 write 10 + 10 otherwise write 1", [20])



if __name__ == "__main__":
    unittest.main()
