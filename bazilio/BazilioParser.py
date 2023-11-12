# Generated from /workspaces/antlr-programming-masterclass-with-python/bazilio/Bazilio.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,193,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,5,2,52,8,2,10,2,12,
        2,55,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,66,8,3,1,4,1,4,
        1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,8,5,8,82,8,8,10,8,
        12,8,85,9,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,97,8,9,1,
        10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,5,11,107,8,11,10,11,12,11,
        110,9,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,
        1,13,1,14,1,14,1,14,1,15,5,15,128,8,15,10,15,12,15,131,9,15,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,145,
        8,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,5,16,180,8,16,10,16,12,16,
        183,9,16,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,0,1,32,19,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,0,205,0,41,
        1,0,0,0,2,44,1,0,0,0,4,53,1,0,0,0,6,65,1,0,0,0,8,67,1,0,0,0,10,71,
        1,0,0,0,12,74,1,0,0,0,14,77,1,0,0,0,16,83,1,0,0,0,18,86,1,0,0,0,
        20,98,1,0,0,0,22,104,1,0,0,0,24,113,1,0,0,0,26,117,1,0,0,0,28,123,
        1,0,0,0,30,129,1,0,0,0,32,144,1,0,0,0,34,184,1,0,0,0,36,187,1,0,
        0,0,38,40,3,2,1,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,
        1,0,0,0,42,1,1,0,0,0,43,41,1,0,0,0,44,45,5,27,0,0,45,46,3,16,8,0,
        46,47,5,29,0,0,47,48,3,4,2,0,48,49,5,30,0,0,49,3,1,0,0,0,50,52,3,
        6,3,0,51,50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,
        5,1,0,0,0,55,53,1,0,0,0,56,66,3,8,4,0,57,66,3,10,5,0,58,66,3,12,
        6,0,59,66,3,14,7,0,60,66,3,28,14,0,61,66,3,18,9,0,62,66,3,20,10,
        0,63,66,3,24,12,0,64,66,3,26,13,0,65,56,1,0,0,0,65,57,1,0,0,0,65,
        58,1,0,0,0,65,59,1,0,0,0,65,60,1,0,0,0,65,61,1,0,0,0,65,62,1,0,0,
        0,65,63,1,0,0,0,65,64,1,0,0,0,66,7,1,0,0,0,67,68,5,26,0,0,68,69,
        5,1,0,0,69,70,3,32,16,0,70,9,1,0,0,0,71,72,5,2,0,0,72,73,5,26,0,
        0,73,11,1,0,0,0,74,75,5,3,0,0,75,76,5,26,0,0,76,13,1,0,0,0,77,78,
        5,4,0,0,78,79,3,32,16,0,79,15,1,0,0,0,80,82,5,26,0,0,81,80,1,0,0,
        0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,17,1,0,0,0,85,83,
        1,0,0,0,86,87,5,5,0,0,87,88,3,32,16,0,88,89,5,29,0,0,89,90,3,4,2,
        0,90,96,5,30,0,0,91,92,5,6,0,0,92,93,5,29,0,0,93,94,3,4,2,0,94,95,
        5,30,0,0,95,97,1,0,0,0,96,91,1,0,0,0,96,97,1,0,0,0,97,19,1,0,0,0,
        98,99,5,7,0,0,99,100,3,32,16,0,100,101,5,29,0,0,101,102,3,4,2,0,
        102,103,5,30,0,0,103,21,1,0,0,0,104,108,5,8,0,0,105,107,3,32,16,
        0,106,105,1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,
        0,109,111,1,0,0,0,110,108,1,0,0,0,111,112,5,9,0,0,112,23,1,0,0,0,
        113,114,5,26,0,0,114,115,5,10,0,0,115,116,3,32,16,0,116,25,1,0,0,
        0,117,118,5,11,0,0,118,119,5,26,0,0,119,120,5,31,0,0,120,121,3,32,
        16,0,121,122,5,32,0,0,122,27,1,0,0,0,123,124,5,27,0,0,124,125,3,
        30,15,0,125,29,1,0,0,0,126,128,3,32,16,0,127,126,1,0,0,0,128,131,
        1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,31,1,0,0,0,131,129,1,
        0,0,0,132,133,6,16,-1,0,133,134,5,33,0,0,134,135,3,32,16,0,135,136,
        5,34,0,0,136,145,1,0,0,0,137,145,5,26,0,0,138,145,5,25,0,0,139,145,
        5,28,0,0,140,145,3,22,11,0,141,145,3,34,17,0,142,145,3,36,18,0,143,
        145,5,24,0,0,144,132,1,0,0,0,144,137,1,0,0,0,144,138,1,0,0,0,144,
        139,1,0,0,0,144,140,1,0,0,0,144,141,1,0,0,0,144,142,1,0,0,0,144,
        143,1,0,0,0,145,181,1,0,0,0,146,147,10,18,0,0,147,148,5,15,0,0,148,
        180,3,32,16,19,149,150,10,17,0,0,150,151,5,16,0,0,151,180,3,32,16,
        18,152,153,10,16,0,0,153,154,5,17,0,0,154,180,3,32,16,17,155,156,
        10,15,0,0,156,157,5,13,0,0,157,180,3,32,16,16,158,159,10,14,0,0,
        159,160,5,14,0,0,160,180,3,32,16,15,161,162,10,13,0,0,162,163,5,
        18,0,0,163,180,3,32,16,14,164,165,10,12,0,0,165,166,5,19,0,0,166,
        180,3,32,16,13,167,168,10,11,0,0,168,169,5,20,0,0,169,180,3,32,16,
        12,170,171,10,10,0,0,171,172,5,21,0,0,172,180,3,32,16,11,173,174,
        10,9,0,0,174,175,5,22,0,0,175,180,3,32,16,10,176,177,10,8,0,0,177,
        178,5,23,0,0,178,180,3,32,16,9,179,146,1,0,0,0,179,149,1,0,0,0,179,
        152,1,0,0,0,179,155,1,0,0,0,179,158,1,0,0,0,179,161,1,0,0,0,179,
        164,1,0,0,0,179,167,1,0,0,0,179,170,1,0,0,0,179,173,1,0,0,0,179,
        176,1,0,0,0,180,183,1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,
        33,1,0,0,0,183,181,1,0,0,0,184,185,5,12,0,0,185,186,5,26,0,0,186,
        35,1,0,0,0,187,188,5,26,0,0,188,189,5,31,0,0,189,190,3,32,16,0,190,
        191,5,32,0,0,191,37,1,0,0,0,10,41,53,65,83,96,108,129,144,179,181
    ]

class BazilioParser ( Parser ):

    grammarFileName = "Bazilio.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<-'", "'<?>'", "'<w>'", "'(:)'", "'if'", 
                     "'else'", "'while'", "'{'", "'}'", "'<<'", "'8<'", 
                     "'#'", "'+'", "'-'", "'*'", "'/'", "'%'", "'<'", "'<='", 
                     "'>'", "'>='", "'='", "'/='", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'|:'", "':|'", 
                     "'['", "']'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ADD", "SUB", "MUL", "DIV", "MOD", "LT", 
                      "LTE", "GT", "GTE", "EQ", "NEQ", "NOTE", "NUM", "VAR", 
                      "PROCEDURE_NAME", "STRING", "LEFT_BAR", "RIGHT_BAR", 
                      "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_PAREN", "RIGHT_PAREN", 
                      "WS", "COMMENT" ]

    RULE_root = 0
    RULE_procedure = 1
    RULE_instructions = 2
    RULE_instruction = 3
    RULE_assignment = 4
    RULE_input_ = 5
    RULE_output_ = 6
    RULE_reproduction = 7
    RULE_parameters = 8
    RULE_condition = 9
    RULE_while_ = 10
    RULE_list_expression = 11
    RULE_list_add = 12
    RULE_list_cut = 13
    RULE_procedure_call = 14
    RULE_procedure_call_parameters = 15
    RULE_expression = 16
    RULE_list_size = 17
    RULE_list_query = 18

    ruleNames =  [ "root", "procedure", "instructions", "instruction", "assignment", 
                   "input_", "output_", "reproduction", "parameters", "condition", 
                   "while_", "list_expression", "list_add", "list_cut", 
                   "procedure_call", "procedure_call_parameters", "expression", 
                   "list_size", "list_query" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    ADD=13
    SUB=14
    MUL=15
    DIV=16
    MOD=17
    LT=18
    LTE=19
    GT=20
    GTE=21
    EQ=22
    NEQ=23
    NOTE=24
    NUM=25
    VAR=26
    PROCEDURE_NAME=27
    STRING=28
    LEFT_BAR=29
    RIGHT_BAR=30
    LEFT_BRACKET=31
    RIGHT_BRACKET=32
    LEFT_PAREN=33
    RIGHT_PAREN=34
    WS=35
    COMMENT=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def procedure(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ProcedureContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ProcedureContext,i)


        def getRuleIndex(self):
            return BazilioParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = BazilioParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 38
                self.procedure()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROCEDURE_NAME(self):
            return self.getToken(BazilioParser.PROCEDURE_NAME, 0)

        def parameters(self):
            return self.getTypedRuleContext(BazilioParser.ParametersContext,0)


        def LEFT_BAR(self):
            return self.getToken(BazilioParser.LEFT_BAR, 0)

        def instructions(self):
            return self.getTypedRuleContext(BazilioParser.InstructionsContext,0)


        def RIGHT_BAR(self):
            return self.getToken(BazilioParser.RIGHT_BAR, 0)

        def getRuleIndex(self):
            return BazilioParser.RULE_procedure

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedure" ):
                return visitor.visitProcedure(self)
            else:
                return visitor.visitChildren(self)




    def procedure(self):

        localctx = BazilioParser.ProcedureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_procedure)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(BazilioParser.PROCEDURE_NAME)
            self.state = 45
            self.parameters()
            self.state = 46
            self.match(BazilioParser.LEFT_BAR)
            self.state = 47
            self.instructions()
            self.state = 48
            self.match(BazilioParser.RIGHT_BAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.InstructionContext)
            else:
                return self.getTypedRuleContext(BazilioParser.InstructionContext,i)


        def getRuleIndex(self):
            return BazilioParser.RULE_instructions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstructions" ):
                return visitor.visitInstructions(self)
            else:
                return visitor.visitChildren(self)




    def instructions(self):

        localctx = BazilioParser.InstructionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instructions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 201328828) != 0):
                self.state = 50
                self.instruction()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(BazilioParser.AssignmentContext,0)


        def input_(self):
            return self.getTypedRuleContext(BazilioParser.Input_Context,0)


        def output_(self):
            return self.getTypedRuleContext(BazilioParser.Output_Context,0)


        def reproduction(self):
            return self.getTypedRuleContext(BazilioParser.ReproductionContext,0)


        def procedure_call(self):
            return self.getTypedRuleContext(BazilioParser.Procedure_callContext,0)


        def condition(self):
            return self.getTypedRuleContext(BazilioParser.ConditionContext,0)


        def while_(self):
            return self.getTypedRuleContext(BazilioParser.While_Context,0)


        def list_add(self):
            return self.getTypedRuleContext(BazilioParser.List_addContext,0)


        def list_cut(self):
            return self.getTypedRuleContext(BazilioParser.List_cutContext,0)


        def getRuleIndex(self):
            return BazilioParser.RULE_instruction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = BazilioParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instruction)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.input_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.output_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.reproduction()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 60
                self.procedure_call()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 61
                self.condition()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 62
                self.while_()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 63
                self.list_add()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 64
                self.list_cut()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BazilioParser.VAR, 0)

        def expression(self):
            return self.getTypedRuleContext(BazilioParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BazilioParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = BazilioParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(BazilioParser.VAR)
            self.state = 68
            self.match(BazilioParser.T__0)
            self.state = 69
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Input_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BazilioParser.VAR, 0)

        def getRuleIndex(self):
            return BazilioParser.RULE_input_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput_" ):
                return visitor.visitInput_(self)
            else:
                return visitor.visitChildren(self)




    def input_(self):

        localctx = BazilioParser.Input_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_input_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(BazilioParser.T__1)
            self.state = 72
            self.match(BazilioParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Output_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BazilioParser.VAR, 0)

        def getRuleIndex(self):
            return BazilioParser.RULE_output_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutput_" ):
                return visitor.visitOutput_(self)
            else:
                return visitor.visitChildren(self)




    def output_(self):

        localctx = BazilioParser.Output_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_output_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(BazilioParser.T__2)
            self.state = 75
            self.match(BazilioParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReproductionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BazilioParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BazilioParser.RULE_reproduction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReproduction" ):
                return visitor.visitReproduction(self)
            else:
                return visitor.visitChildren(self)




    def reproduction(self):

        localctx = BazilioParser.ReproductionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_reproduction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(BazilioParser.T__3)
            self.state = 78
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(BazilioParser.VAR)
            else:
                return self.getToken(BazilioParser.VAR, i)

        def getRuleIndex(self):
            return BazilioParser.RULE_parameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = BazilioParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 80
                self.match(BazilioParser.VAR)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BazilioParser.ExpressionContext,0)


        def LEFT_BAR(self, i:int=None):
            if i is None:
                return self.getTokens(BazilioParser.LEFT_BAR)
            else:
                return self.getToken(BazilioParser.LEFT_BAR, i)

        def instructions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.InstructionsContext)
            else:
                return self.getTypedRuleContext(BazilioParser.InstructionsContext,i)


        def RIGHT_BAR(self, i:int=None):
            if i is None:
                return self.getTokens(BazilioParser.RIGHT_BAR)
            else:
                return self.getToken(BazilioParser.RIGHT_BAR, i)

        def getRuleIndex(self):
            return BazilioParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = BazilioParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(BazilioParser.T__4)
            self.state = 87
            self.expression(0)
            self.state = 88
            self.match(BazilioParser.LEFT_BAR)
            self.state = 89
            self.instructions()
            self.state = 90
            self.match(BazilioParser.RIGHT_BAR)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 91
                self.match(BazilioParser.T__5)
                self.state = 92
                self.match(BazilioParser.LEFT_BAR)
                self.state = 93
                self.instructions()
                self.state = 94
                self.match(BazilioParser.RIGHT_BAR)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BazilioParser.ExpressionContext,0)


        def LEFT_BAR(self):
            return self.getToken(BazilioParser.LEFT_BAR, 0)

        def instructions(self):
            return self.getTypedRuleContext(BazilioParser.InstructionsContext,0)


        def RIGHT_BAR(self):
            return self.getToken(BazilioParser.RIGHT_BAR, 0)

        def getRuleIndex(self):
            return BazilioParser.RULE_while_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_" ):
                return visitor.visitWhile_(self)
            else:
                return visitor.visitChildren(self)




    def while_(self):

        localctx = BazilioParser.While_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_while_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(BazilioParser.T__6)
            self.state = 99
            self.expression(0)
            self.state = 100
            self.match(BazilioParser.LEFT_BAR)
            self.state = 101
            self.instructions()
            self.state = 102
            self.match(BazilioParser.RIGHT_BAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExpressionContext,i)


        def getRuleIndex(self):
            return BazilioParser.RULE_list_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = BazilioParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_list_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(BazilioParser.T__7)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8975814912) != 0):
                self.state = 105
                self.expression(0)
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 111
            self.match(BazilioParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_addContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BazilioParser.VAR, 0)

        def expression(self):
            return self.getTypedRuleContext(BazilioParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BazilioParser.RULE_list_add

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_add" ):
                return visitor.visitList_add(self)
            else:
                return visitor.visitChildren(self)




    def list_add(self):

        localctx = BazilioParser.List_addContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_list_add)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(BazilioParser.VAR)
            self.state = 114
            self.match(BazilioParser.T__9)
            self.state = 115
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_cutContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BazilioParser.VAR, 0)

        def LEFT_BRACKET(self):
            return self.getToken(BazilioParser.LEFT_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(BazilioParser.ExpressionContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(BazilioParser.RIGHT_BRACKET, 0)

        def getRuleIndex(self):
            return BazilioParser.RULE_list_cut

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_cut" ):
                return visitor.visitList_cut(self)
            else:
                return visitor.visitChildren(self)




    def list_cut(self):

        localctx = BazilioParser.List_cutContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_list_cut)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(BazilioParser.T__10)
            self.state = 118
            self.match(BazilioParser.VAR)
            self.state = 119
            self.match(BazilioParser.LEFT_BRACKET)
            self.state = 120
            self.expression(0)
            self.state = 121
            self.match(BazilioParser.RIGHT_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Procedure_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROCEDURE_NAME(self):
            return self.getToken(BazilioParser.PROCEDURE_NAME, 0)

        def procedure_call_parameters(self):
            return self.getTypedRuleContext(BazilioParser.Procedure_call_parametersContext,0)


        def getRuleIndex(self):
            return BazilioParser.RULE_procedure_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedure_call" ):
                return visitor.visitProcedure_call(self)
            else:
                return visitor.visitChildren(self)




    def procedure_call(self):

        localctx = BazilioParser.Procedure_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_procedure_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(BazilioParser.PROCEDURE_NAME)
            self.state = 124
            self.procedure_call_parameters()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Procedure_call_parametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExpressionContext,i)


        def getRuleIndex(self):
            return BazilioParser.RULE_procedure_call_parameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedure_call_parameters" ):
                return visitor.visitProcedure_call_parameters(self)
            else:
                return visitor.visitChildren(self)




    def procedure_call_parameters(self):

        localctx = BazilioParser.Procedure_call_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_procedure_call_parameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 126
                    self.expression(0) 
                self.state = 131
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BazilioParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExpressionContext,i)

        def ADD(self):
            return self.getToken(BazilioParser.ADD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class SubContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExpressionContext,i)

        def SUB(self):
            return self.getToken(BazilioParser.SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)


    class ParentesesContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEFT_PAREN(self):
            return self.getToken(BazilioParser.LEFT_PAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(BazilioParser.ExpressionContext,0)

        def RIGHT_PAREN(self):
            return self.getToken(BazilioParser.RIGHT_PAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenteses" ):
                return visitor.visitParenteses(self)
            else:
                return visitor.visitChildren(self)


    class ModContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExpressionContext,i)

        def MOD(self):
            return self.getToken(BazilioParser.MOD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMod" ):
                return visitor.visitMod(self)
            else:
                return visitor.visitChildren(self)


    class MulContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExpressionContext,i)

        def MUL(self):
            return self.getToken(BazilioParser.MUL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul" ):
                return visitor.visitMul(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(BazilioParser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class LtContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExpressionContext,i)

        def LT(self):
            return self.getToken(BazilioParser.LT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLt" ):
                return visitor.visitLt(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(BazilioParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class EqContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExpressionContext,i)

        def EQ(self):
            return self.getToken(BazilioParser.EQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEq" ):
                return visitor.visitEq(self)
            else:
                return visitor.visitChildren(self)


    class GtContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExpressionContext,i)

        def GT(self):
            return self.getToken(BazilioParser.GT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGt" ):
                return visitor.visitGt(self)
            else:
                return visitor.visitChildren(self)


    class DivContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExpressionContext,i)

        def DIV(self):
            return self.getToken(BazilioParser.DIV, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiv" ):
                return visitor.visitDiv(self)
            else:
                return visitor.visitChildren(self)


    class ListSizeContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def list_size(self):
            return self.getTypedRuleContext(BazilioParser.List_sizeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListSize" ):
                return visitor.visitListSize(self)
            else:
                return visitor.visitChildren(self)


    class NoteContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOTE(self):
            return self.getToken(BazilioParser.NOTE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNote" ):
                return visitor.visitNote(self)
            else:
                return visitor.visitChildren(self)


    class ValueContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(BazilioParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)


    class GteContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExpressionContext,i)

        def GTE(self):
            return self.getToken(BazilioParser.GTE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGte" ):
                return visitor.visitGte(self)
            else:
                return visitor.visitChildren(self)


    class ListExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def list_expression(self):
            return self.getTypedRuleContext(BazilioParser.List_expressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListExpr" ):
                return visitor.visitListExpr(self)
            else:
                return visitor.visitChildren(self)


    class NeqContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExpressionContext,i)

        def NEQ(self):
            return self.getToken(BazilioParser.NEQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeq" ):
                return visitor.visitNeq(self)
            else:
                return visitor.visitChildren(self)


    class LteContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ExpressionContext,i)

        def LTE(self):
            return self.getToken(BazilioParser.LTE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLte" ):
                return visitor.visitLte(self)
            else:
                return visitor.visitChildren(self)


    class ListQueryContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BazilioParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def list_query(self):
            return self.getTypedRuleContext(BazilioParser.List_queryContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListQuery" ):
                return visitor.visitListQuery(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BazilioParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = BazilioParser.ParentesesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 133
                self.match(BazilioParser.LEFT_PAREN)
                self.state = 134
                self.expression(0)
                self.state = 135
                self.match(BazilioParser.RIGHT_PAREN)
                pass

            elif la_ == 2:
                localctx = BazilioParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 137
                self.match(BazilioParser.VAR)
                pass

            elif la_ == 3:
                localctx = BazilioParser.ValueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 138
                self.match(BazilioParser.NUM)
                pass

            elif la_ == 4:
                localctx = BazilioParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 139
                self.match(BazilioParser.STRING)
                pass

            elif la_ == 5:
                localctx = BazilioParser.ListExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 140
                self.list_expression()
                pass

            elif la_ == 6:
                localctx = BazilioParser.ListSizeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 141
                self.list_size()
                pass

            elif la_ == 7:
                localctx = BazilioParser.ListQueryContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 142
                self.list_query()
                pass

            elif la_ == 8:
                localctx = BazilioParser.NoteContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 143
                self.match(BazilioParser.NOTE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 181
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 179
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = BazilioParser.MulContext(self, BazilioParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 146
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 147
                        self.match(BazilioParser.MUL)
                        self.state = 148
                        self.expression(19)
                        pass

                    elif la_ == 2:
                        localctx = BazilioParser.DivContext(self, BazilioParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 149
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 150
                        self.match(BazilioParser.DIV)
                        self.state = 151
                        self.expression(18)
                        pass

                    elif la_ == 3:
                        localctx = BazilioParser.ModContext(self, BazilioParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 152
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 153
                        self.match(BazilioParser.MOD)
                        self.state = 154
                        self.expression(17)
                        pass

                    elif la_ == 4:
                        localctx = BazilioParser.AddContext(self, BazilioParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 155
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 156
                        self.match(BazilioParser.ADD)
                        self.state = 157
                        self.expression(16)
                        pass

                    elif la_ == 5:
                        localctx = BazilioParser.SubContext(self, BazilioParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 158
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 159
                        self.match(BazilioParser.SUB)
                        self.state = 160
                        self.expression(15)
                        pass

                    elif la_ == 6:
                        localctx = BazilioParser.LtContext(self, BazilioParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 161
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 162
                        self.match(BazilioParser.LT)
                        self.state = 163
                        self.expression(14)
                        pass

                    elif la_ == 7:
                        localctx = BazilioParser.LteContext(self, BazilioParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 164
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 165
                        self.match(BazilioParser.LTE)
                        self.state = 166
                        self.expression(13)
                        pass

                    elif la_ == 8:
                        localctx = BazilioParser.GtContext(self, BazilioParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 167
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 168
                        self.match(BazilioParser.GT)
                        self.state = 169
                        self.expression(12)
                        pass

                    elif la_ == 9:
                        localctx = BazilioParser.GteContext(self, BazilioParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 170
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 171
                        self.match(BazilioParser.GTE)
                        self.state = 172
                        self.expression(11)
                        pass

                    elif la_ == 10:
                        localctx = BazilioParser.EqContext(self, BazilioParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 173
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 174
                        self.match(BazilioParser.EQ)
                        self.state = 175
                        self.expression(10)
                        pass

                    elif la_ == 11:
                        localctx = BazilioParser.NeqContext(self, BazilioParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 176
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 177
                        self.match(BazilioParser.NEQ)
                        self.state = 178
                        self.expression(9)
                        pass

             
                self.state = 183
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class List_sizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BazilioParser.VAR, 0)

        def getRuleIndex(self):
            return BazilioParser.RULE_list_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_size" ):
                return visitor.visitList_size(self)
            else:
                return visitor.visitChildren(self)




    def list_size(self):

        localctx = BazilioParser.List_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_list_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(BazilioParser.T__11)
            self.state = 185
            self.match(BazilioParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_queryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BazilioParser.VAR, 0)

        def LEFT_BRACKET(self):
            return self.getToken(BazilioParser.LEFT_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(BazilioParser.ExpressionContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(BazilioParser.RIGHT_BRACKET, 0)

        def getRuleIndex(self):
            return BazilioParser.RULE_list_query

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_query" ):
                return visitor.visitList_query(self)
            else:
                return visitor.visitChildren(self)




    def list_query(self):

        localctx = BazilioParser.List_queryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_list_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(BazilioParser.VAR)
            self.state = 188
            self.match(BazilioParser.LEFT_BRACKET)
            self.state = 189
            self.expression(0)
            self.state = 190
            self.match(BazilioParser.RIGHT_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[16] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 8)
         




