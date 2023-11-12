# Generated from /workspaces/antlr-programming-masterclass-with-python/bazilio/Bazilio.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .BazilioParser import BazilioParser
else:
    from BazilioParser import BazilioParser

# This class defines a complete generic visitor for a parse tree produced by BazilioParser.

class BazilioVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BazilioParser#root.
    def visitRoot(self, ctx:BazilioParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#procedure.
    def visitProcedure(self, ctx:BazilioParser.ProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#instructions.
    def visitInstructions(self, ctx:BazilioParser.InstructionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#instruction.
    def visitInstruction(self, ctx:BazilioParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#assignment.
    def visitAssignment(self, ctx:BazilioParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#input_.
    def visitInput_(self, ctx:BazilioParser.Input_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#output_.
    def visitOutput_(self, ctx:BazilioParser.Output_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#reproduction.
    def visitReproduction(self, ctx:BazilioParser.ReproductionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#parameters.
    def visitParameters(self, ctx:BazilioParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#condition.
    def visitCondition(self, ctx:BazilioParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#while_.
    def visitWhile_(self, ctx:BazilioParser.While_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#list_expression.
    def visitList_expression(self, ctx:BazilioParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#list_add.
    def visitList_add(self, ctx:BazilioParser.List_addContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#list_cut.
    def visitList_cut(self, ctx:BazilioParser.List_cutContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#procedure_call.
    def visitProcedure_call(self, ctx:BazilioParser.Procedure_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#procedure_call_parameters.
    def visitProcedure_call_parameters(self, ctx:BazilioParser.Procedure_call_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Add.
    def visitAdd(self, ctx:BazilioParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Sub.
    def visitSub(self, ctx:BazilioParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Parenteses.
    def visitParenteses(self, ctx:BazilioParser.ParentesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Mod.
    def visitMod(self, ctx:BazilioParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Mul.
    def visitMul(self, ctx:BazilioParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Var.
    def visitVar(self, ctx:BazilioParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Lt.
    def visitLt(self, ctx:BazilioParser.LtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#String.
    def visitString(self, ctx:BazilioParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Eq.
    def visitEq(self, ctx:BazilioParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Gt.
    def visitGt(self, ctx:BazilioParser.GtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Div.
    def visitDiv(self, ctx:BazilioParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#ListSize.
    def visitListSize(self, ctx:BazilioParser.ListSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Note.
    def visitNote(self, ctx:BazilioParser.NoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Value.
    def visitValue(self, ctx:BazilioParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Gte.
    def visitGte(self, ctx:BazilioParser.GteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#ListExpr.
    def visitListExpr(self, ctx:BazilioParser.ListExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Neq.
    def visitNeq(self, ctx:BazilioParser.NeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#Lte.
    def visitLte(self, ctx:BazilioParser.LteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#ListQuery.
    def visitListQuery(self, ctx:BazilioParser.ListQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#list_size.
    def visitList_size(self, ctx:BazilioParser.List_sizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#list_query.
    def visitList_query(self, ctx:BazilioParser.List_queryContext):
        return self.visitChildren(ctx)



del BazilioParser