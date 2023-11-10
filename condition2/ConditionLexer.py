# Generated from /workspaces/antlr-programming-masterclass-with-python/condition2/Condition.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,11,69,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,9,
        4,9,62,8,9,11,9,12,9,63,1,10,1,10,1,10,1,10,0,0,11,1,1,3,2,5,3,7,
        4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,1,0,2,1,0,48,57,3,0,9,10,13,
        13,32,32,69,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,
        1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,
        1,0,0,0,0,21,1,0,0,0,1,23,1,0,0,0,3,27,1,0,0,0,5,37,1,0,0,0,7,43,
        1,0,0,0,9,48,1,0,0,0,11,50,1,0,0,0,13,52,1,0,0,0,15,55,1,0,0,0,17,
        58,1,0,0,0,19,61,1,0,0,0,21,65,1,0,0,0,23,24,5,105,0,0,24,25,5,102,
        0,0,25,26,5,102,0,0,26,2,1,0,0,0,27,28,5,111,0,0,28,29,5,116,0,0,
        29,30,5,104,0,0,30,31,5,101,0,0,31,32,5,114,0,0,32,33,5,119,0,0,
        33,34,5,105,0,0,34,35,5,115,0,0,35,36,5,101,0,0,36,4,1,0,0,0,37,
        38,5,119,0,0,38,39,5,114,0,0,39,40,5,105,0,0,40,41,5,116,0,0,41,
        42,5,101,0,0,42,6,1,0,0,0,43,44,5,110,0,0,44,45,5,101,0,0,45,46,
        5,120,0,0,46,47,5,116,0,0,47,8,1,0,0,0,48,49,5,60,0,0,49,10,1,0,
        0,0,50,51,5,62,0,0,51,12,1,0,0,0,52,53,5,61,0,0,53,54,5,61,0,0,54,
        14,1,0,0,0,55,56,5,33,0,0,56,57,5,61,0,0,57,16,1,0,0,0,58,59,5,43,
        0,0,59,18,1,0,0,0,60,62,7,0,0,0,61,60,1,0,0,0,62,63,1,0,0,0,63,61,
        1,0,0,0,63,64,1,0,0,0,64,20,1,0,0,0,65,66,7,1,0,0,66,67,1,0,0,0,
        67,68,6,10,0,0,68,22,1,0,0,0,2,0,63,1,6,0,0
    ]

class ConditionLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    LT = 5
    GT = 6
    EQ = 7
    NEQ = 8
    ADD = 9
    NUM = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'iff'", "'otherwise'", "'write'", "'next'", "'<'", "'>'", "'=='", 
            "'!='", "'+'" ]

    symbolicNames = [ "<INVALID>",
            "LT", "GT", "EQ", "NEQ", "ADD", "NUM", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "LT", "GT", "EQ", "NEQ", 
                  "ADD", "NUM", "WS" ]

    grammarFileName = "Condition.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


