from collections import defaultdict, deque
from typing import Any
from antlr4 import *
from models import *
from BazilioParser import BazilioParser
from BazilioVisitor import BazilioVisitor
from icecream import ic


class EvalVisitor(BazilioVisitor):
    def __init__(
        self,
        entry_procedure="Main",
        entry_parameters=[],
    ) -> None:
        super().__init__()
        self.stack = deque()
        self.results = []
        self.score = []
        self.procedures_definition = {}
        self.entry_procedure = entry_procedure
        self.entry_parameters = entry_parameters

    def procedure_invocation(self, name, values):
        if name not in self.procedures_definition:
            raise BazilioException(f"procedure {name} not defined")

        procedure_def_model: ProcedureDefinition = self.procedures_definition[name]

        if len(values) != len(procedure_def_model.args):
            raise BazilioException(
                f"args length not match, {name} was expecting {procedure_def_model.args} but was given {values}"
            )

        new_vars = defaultdict(lambda: 0)
        for param, value in zip(procedure_def_model.args, values):
            new_vars[param] = value

        self.stack.append(new_vars)
        self.visit(procedure_def_model.instructions)
        self.stack.pop()

    @property
    def actual_stack(self):
        return self.stack[0]

    def visitRoot(self, ctx: BazilioParser.RootContext):
        return self.visitChildren(ctx)

    def visitProcedure(self, ctx: BazilioParser.ProcedureContext):
        return self.visitChildren(ctx)

    def visitInstructions(self, ctx: BazilioParser.InstructionsContext):
        return self.visitChildren(ctx)

    def visitInstruction(self, ctx: BazilioParser.InstructionContext):
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx: BazilioParser.AssignmentContext):
        var_name = ctx.VAR().getText()
        expr = self.visit(ctx.expression())
        self.actual_stack[var_name] = expr
        return self.visitChildren(ctx)

    def visitInput_(self, ctx: BazilioParser.Input_Context):
        return self.visitChildren(ctx)

    def visitOutput_(self, ctx: BazilioParser.Output_Context):
        return self.visitChildren(ctx)

    def visitReproduction(self, ctx: BazilioParser.ReproductionContext):
        return self.visitChildren(ctx)

    def visitParameters(self, ctx: BazilioParser.ParametersContext):
        return self.visitChildren(ctx)

    def visitCondition(self, ctx: BazilioParser.ConditionContext):
        return self.visitChildren(ctx)

    def visitWhile_(self, ctx: BazilioParser.While_Context):
        return self.visitChildren(ctx)

    def visitList_add(self, ctx: BazilioParser.List_addContext):
        return self.visitChildren(ctx)

    def visitList_cut(self, ctx: BazilioParser.List_cutContext):
        return self.visitChildren(ctx)

    def visitProcedure_call(self, ctx: BazilioParser.Procedure_callContext):
        return self.visitChildren(ctx)

    def visitProcedure_call_parameters(
        self, ctx: BazilioParser.Procedure_call_parametersContext
    ):
        return self.visitChildren(ctx)

    def visitAdd(self, ctx: BazilioParser.AddContext):  #
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return left + right

    def visitSub(self, ctx: BazilioParser.SubContext):  #
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return left - right

    def visitParenteses(self, ctx: BazilioParser.ParentesesContext):  #
        return self.visit(ctx.expression())

    def visitMod(self, ctx: BazilioParser.ModContext):  #
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return left % right

    def visitMul(self, ctx: BazilioParser.MulContext):  #
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return left * right

    def visitVar(self, ctx: BazilioParser.VarContext):  #
        var_name = ctx.VAR().getText()
        if var_name not in self.actual_stack:
            return 0
        return self.actual_stack[var_name]

    def visitLt(self, ctx: BazilioParser.LtContext):  #
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return 1 if left < right else 0

    def visitString(self, ctx: BazilioParser.StringContext):  #
        return ctx.STRING().getText()

    def visitEq(self, ctx: BazilioParser.EqContext):  #
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return 1 if left == right else 0

    def visitGt(self, ctx: BazilioParser.GtContext):  #
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return 1 if left > right else 0

    def visitDiv(self, ctx: BazilioParser.DivContext):  #
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        if right == 0:
            raise BazilioException("cannot divide by zero")
        return int(left / right)

    def visitNote(self, ctx: BazilioParser.NoteContext): # 
        note_str = ctx.NOTE().getText()
        if len(note_str) == 1:
            note_str += "4"
        return NOTES[note_str]

    def visitValue(self, ctx: BazilioParser.ValueContext):  #
        return int(ctx.NUM().getText())

    def visitGte(self, ctx: BazilioParser.GteContext):  #
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return 1 if left >= right else 0

    def visitNeq(self, ctx: BazilioParser.NeqContext):  #
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return 1 if left != right else 0

    def visitLte(self, ctx: BazilioParser.LteContext):  #
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return 1 if left <= right else 0
    
    def visitList_expression(self, ctx:BazilioParser.List_expressionContext): # 
        return [self.visit(c) for c in ctx.expression()]

    def visitList_size(self, ctx: BazilioParser.List_sizeContext):
        var_name = ctx.VAR().getText()
        return len(self.actual_stack[var_name])

    def visitList_query(self, ctx: BazilioParser.List_queryContext):
        var_name = ctx.VAR().getText()
        return self.visitChildren(ctx)
