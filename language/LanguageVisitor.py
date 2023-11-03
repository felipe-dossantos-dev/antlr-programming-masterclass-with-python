# Generated from language/Language.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LanguageParser import LanguageParser
else:
    from LanguageParser import LanguageParser

# This class defines a complete generic visitor for a parse tree produced by LanguageParser.

class LanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LanguageParser#root.
    def visitRoot(self, ctx:LanguageParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#inss.
    def visitInss(self, ctx:LanguageParser.InssContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#ins.
    def visitIns(self, ctx:LanguageParser.InsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#output.
    def visitOutput(self, ctx:LanguageParser.OutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#assign.
    def visitAssign(self, ctx:LanguageParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#while_.
    def visitWhile_(self, ctx:LanguageParser.While_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#Sub.
    def visitSub(self, ctx:LanguageParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#Var.
    def visitVar(self, ctx:LanguageParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#Value.
    def visitValue(self, ctx:LanguageParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#Lt.
    def visitLt(self, ctx:LanguageParser.LtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#Sum.
    def visitSum(self, ctx:LanguageParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#Neq.
    def visitNeq(self, ctx:LanguageParser.NeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#Eq.
    def visitEq(self, ctx:LanguageParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#Gt.
    def visitGt(self, ctx:LanguageParser.GtContext):
        return self.visitChildren(ctx)



del LanguageParser