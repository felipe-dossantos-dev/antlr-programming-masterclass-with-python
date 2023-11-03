from antlr4 import *
import unittest
from LanguageLexer import LanguageLexer
from LanguageParser import LanguageParser
from LanguageVisitor import LanguageVisitor
from icecream import ic


class EvalVisitor(LanguageVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.variables = {}
        self.results = []

    def visitRoot(self, ctx: LanguageParser.RootContext):
        return self.visitChildren(ctx)

    def visitInss(self, ctx: LanguageParser.InssContext):
        return self.visitChildren(ctx)

    def visitIns(self, ctx: LanguageParser.InsContext):
        return self.visitChildren(ctx)

    def visitOutput(self, ctx: LanguageParser.OutputContext):
        for r in ctx.getChildren():
            if isinstance(r, TerminalNode):
                continue
            result = self.visit(r)
            self.results.append(result)

    def visitAssign(self, ctx: LanguageParser.AssignContext):
        var_name = ctx.VAR().getText()
        expr = self.visit(ctx.expr())
        self.variables[var_name] = expr

    def visitWhile_(self, ctx: LanguageParser.While_Context):
        while True:
            expr_value = self.visit(ctx.expr())
            if expr_value != 1:
                break
            self.visit(ctx.inss())

    def visitValue(self, ctx: LanguageParser.ValueContext):
        return int(ctx.NUM().getText())

    def visitLt(self, ctx: LanguageParser.LtContext):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return 1 if left < right else 0

    def visitGt(self, ctx: LanguageParser.GtContext):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return 1 if left > right else 0

    def visitSum(self, ctx: LanguageParser.SumContext):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return left + right

    def visitNeq(self, ctx: LanguageParser.NeqContext):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return 1 if left != right else 0

    def visitEq(self, ctx: LanguageParser.EqContext):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return 1 if left == right else 0

    def visitSub(self, ctx: LanguageParser.SubContext):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return left - right

    def visitVar(self, ctx: LanguageParser.VarContext):
        return self.variables[ctx.VAR().getText()]


class TestEvalVisitor(unittest.TestCase):
    def run_one(self, input_data: str, expected: int):
        input_stream = InputStream(input_data)

        lexer = LanguageLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = LanguageParser(token_stream)
        tree = parser.root()

        visitor = EvalVisitor()
        visitor.visit(tree)
        self.assertEqual(visitor.results, expected)

    def test_(self):
        self.run_one("a <- 3 while a < 5 send a a <- a + 1", [3, 4])


if __name__ == "__main__":
    unittest.main()
