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
        if (isinstance(first_expr, int) and first_expr == 1) or first_expr:
            return self.visit(ctx.action(0))
        elif ctx.getChildCount() > 3 and ctx.getChild(3).getText() == 'else':
            return self.visit(ctx.action(1))

    def visitPrint(self, ctx: ConditionParser.PrintContext):
        results = []
        for r in ctx.getChildren():
            if isinstance(r, TerminalNode):
                continue
            result = self.visit(r)
            results.append(result)
        return results

    def visitValue(self, ctx: ConditionParser.ValueContext):
        return int(ctx.NUM().getText())

    def visitLt(self, ctx: ConditionParser.LtContext):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return left < right

    def visitGt(self, ctx: ConditionParser.GtContext):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return left > right


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

    def test_print_value(self):
        self.run_one("print 5", [5])
        self.run_one("print 99999 print 1", [99999, 1])

    def test_greater_than(self):
        self.run_one("print 5 > 6", [False])
        self.run_one("print 7 > 5", [True])

    def test_less_than(self):
        self.run_one("print 5 < 6", [True])
        self.run_one("print 7 < 6", [False])

    def test_condition(self):
        self.run_one("if 7 > 2 print 3", [3])
        self.run_one("if 7 < 2 print 3", [])
        self.run_one("if 7 < 2 print 3 else print 4", [4])
        self.run_one("if 7 > 2 print 3 > 4 else print 4", [False])
        self.run_one("if 7 > 2 print 3 < 4 else print 4", [True])



if __name__ == "__main__":
    unittest.main()
