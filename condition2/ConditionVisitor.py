# Generated from condition2/Condition.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ConditionParser import ConditionParser
else:
    from ConditionParser import ConditionParser

# This class defines a complete generic visitor for a parse tree produced by ConditionParser.

class ConditionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ConditionParser#root.
    def visitRoot(self, ctx:ConditionParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConditionParser#Condition.
    def visitCondition(self, ctx:ConditionParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConditionParser#Print.
    def visitPrint(self, ctx:ConditionParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConditionParser#Next.
    def visitNext(self, ctx:ConditionParser.NextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConditionParser#Value.
    def visitValue(self, ctx:ConditionParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConditionParser#Lt.
    def visitLt(self, ctx:ConditionParser.LtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConditionParser#Sum.
    def visitSum(self, ctx:ConditionParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConditionParser#Neq.
    def visitNeq(self, ctx:ConditionParser.NeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConditionParser#Eq.
    def visitEq(self, ctx:ConditionParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ConditionParser#Gt.
    def visitGt(self, ctx:ConditionParser.GtContext):
        return self.visitChildren(ctx)



del ConditionParser