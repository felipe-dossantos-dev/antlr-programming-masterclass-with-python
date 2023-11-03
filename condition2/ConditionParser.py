# Generated from condition2/Condition.g4 by ANTLR 4.13.1
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
        4,1,11,50,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,3,1,19,8,1,1,1,1,1,1,1,1,1,3,1,25,8,1,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,5,2,45,8,2,10,2,12,2,48,9,2,1,2,0,1,4,3,0,2,4,0,0,55,0,7,1,
        0,0,0,2,24,1,0,0,0,4,26,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,9,1,0,
        0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,11,1,0,0,0,11,12,5,0,0,1,12,1,1,
        0,0,0,13,14,5,1,0,0,14,15,3,4,2,0,15,18,3,2,1,0,16,17,5,2,0,0,17,
        19,3,2,1,0,18,16,1,0,0,0,18,19,1,0,0,0,19,25,1,0,0,0,20,21,5,3,0,
        0,21,25,3,4,2,0,22,23,5,4,0,0,23,25,3,4,2,0,24,13,1,0,0,0,24,20,
        1,0,0,0,24,22,1,0,0,0,25,3,1,0,0,0,26,27,6,2,-1,0,27,28,5,10,0,0,
        28,46,1,0,0,0,29,30,10,6,0,0,30,31,5,5,0,0,31,45,3,4,2,7,32,33,10,
        5,0,0,33,34,5,6,0,0,34,45,3,4,2,6,35,36,10,4,0,0,36,37,5,7,0,0,37,
        45,3,4,2,5,38,39,10,3,0,0,39,40,5,8,0,0,40,45,3,4,2,4,41,42,10,2,
        0,0,42,43,5,9,0,0,43,45,3,4,2,3,44,29,1,0,0,0,44,32,1,0,0,0,44,35,
        1,0,0,0,44,38,1,0,0,0,44,41,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,
        46,47,1,0,0,0,47,5,1,0,0,0,48,46,1,0,0,0,5,9,18,24,44,46
    ]

class ConditionParser ( Parser ):

    grammarFileName = "Condition.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'iff'", "'otherwise'", "'write'", "'next'", 
                     "'<'", "'>'", "'=='", "'!='", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "LT", "GT", "EQ", "NEQ", "ADD", "NUM", 
                      "WS" ]

    RULE_root = 0
    RULE_action = 1
    RULE_expr = 2

    ruleNames =  [ "root", "action", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    LT=5
    GT=6
    EQ=7
    NEQ=8
    ADD=9
    NUM=10
    WS=11

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

        def EOF(self):
            return self.getToken(ConditionParser.EOF, 0)

        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConditionParser.ActionContext)
            else:
                return self.getTypedRuleContext(ConditionParser.ActionContext,i)


        def getRuleIndex(self):
            return ConditionParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = ConditionParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.action()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 26) != 0)):
                    break

            self.state = 11
            self.match(ConditionParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ConditionParser.RULE_action

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ConditionContext(ActionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConditionParser.ActionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ConditionParser.ExprContext,0)

        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConditionParser.ActionContext)
            else:
                return self.getTypedRuleContext(ConditionParser.ActionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)


    class PrintContext(ActionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConditionParser.ActionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ConditionParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)


    class NextContext(ActionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConditionParser.ActionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ConditionParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNext" ):
                return visitor.visitNext(self)
            else:
                return visitor.visitChildren(self)



    def action(self):

        localctx = ConditionParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_action)
        try:
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = ConditionParser.ConditionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.match(ConditionParser.T__0)
                self.state = 14
                self.expr(0)
                self.state = 15
                self.action()
                self.state = 18
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 16
                    self.match(ConditionParser.T__1)
                    self.state = 17
                    self.action()


                pass
            elif token in [3]:
                localctx = ConditionParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.match(ConditionParser.T__2)
                self.state = 21
                self.expr(0)
                pass
            elif token in [4]:
                localctx = ConditionParser.NextContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.match(ConditionParser.T__3)
                self.state = 23
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ConditionParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ValueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConditionParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(ConditionParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)


    class LtContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConditionParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConditionParser.ExprContext)
            else:
                return self.getTypedRuleContext(ConditionParser.ExprContext,i)

        def LT(self):
            return self.getToken(ConditionParser.LT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLt" ):
                return visitor.visitLt(self)
            else:
                return visitor.visitChildren(self)


    class SumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConditionParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConditionParser.ExprContext)
            else:
                return self.getTypedRuleContext(ConditionParser.ExprContext,i)

        def ADD(self):
            return self.getToken(ConditionParser.ADD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSum" ):
                return visitor.visitSum(self)
            else:
                return visitor.visitChildren(self)


    class NeqContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConditionParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConditionParser.ExprContext)
            else:
                return self.getTypedRuleContext(ConditionParser.ExprContext,i)

        def NEQ(self):
            return self.getToken(ConditionParser.NEQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeq" ):
                return visitor.visitNeq(self)
            else:
                return visitor.visitChildren(self)


    class EqContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConditionParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConditionParser.ExprContext)
            else:
                return self.getTypedRuleContext(ConditionParser.ExprContext,i)

        def EQ(self):
            return self.getToken(ConditionParser.EQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEq" ):
                return visitor.visitEq(self)
            else:
                return visitor.visitChildren(self)


    class GtContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConditionParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ConditionParser.ExprContext)
            else:
                return self.getTypedRuleContext(ConditionParser.ExprContext,i)

        def GT(self):
            return self.getToken(ConditionParser.GT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGt" ):
                return visitor.visitGt(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ConditionParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ConditionParser.ValueContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 27
            self.match(ConditionParser.NUM)
            self._ctx.stop = self._input.LT(-1)
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 44
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ConditionParser.LtContext(self, ConditionParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 29
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 30
                        self.match(ConditionParser.LT)
                        self.state = 31
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = ConditionParser.GtContext(self, ConditionParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 32
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 33
                        self.match(ConditionParser.GT)
                        self.state = 34
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = ConditionParser.EqContext(self, ConditionParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 36
                        self.match(ConditionParser.EQ)
                        self.state = 37
                        self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = ConditionParser.NeqContext(self, ConditionParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 39
                        self.match(ConditionParser.NEQ)
                        self.state = 40
                        self.expr(4)
                        pass

                    elif la_ == 5:
                        localctx = ConditionParser.SumContext(self, ConditionParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 41
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 42
                        self.match(ConditionParser.ADD)
                        self.state = 43
                        self.expr(3)
                        pass

             
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




