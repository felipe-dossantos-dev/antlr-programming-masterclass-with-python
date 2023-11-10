# Generated from /workspaces/antlr-programming-masterclass-with-python/expr/Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#root.
    def visitRoot(self, ctx:ExprParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#div.
    def visitDiv(self, ctx:ExprParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#sub.
    def visitSub(self, ctx:ExprParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mul.
    def visitMul(self, ctx:ExprParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#sum.
    def visitSum(self, ctx:ExprParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#value.
    def visitValue(self, ctx:ExprParser.ValueContext):
        return self.visitChildren(ctx)



del ExprParser