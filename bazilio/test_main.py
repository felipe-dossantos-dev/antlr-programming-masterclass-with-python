import unittest
from unittest.mock import patch
from antlr4 import *
from BazilioLexer import BazilioLexer
from BazilioParser import BazilioParser
from main import EvalVisitor
from models import *


class TestEvalVisitor(unittest.TestCase):
    def setUp(self):
        self.eval_visitor = EvalVisitor()
        self.eval_visitor.procedures_definition[
            "SampleProcedure"
        ] = ProcedureDefinition(
            name="SampleProcedure",
            args=["arg1", "arg2"],
            instructions=[],
        )

    def get_parser(self, input) -> BazilioParser:
        lexer = BazilioLexer(InputStream(input))
        stream = CommonTokenStream(lexer)
        return BazilioParser(stream)

    def test_procedure_invocation_invalid_name(self):
        # arrange
        name = "InvalidProcedure"
        values = [1, 2]

        # act
        with self.assertRaises(BazilioException) as context:
            self.eval_visitor.procedure_invocation(name, values)

        # assert
        self.assertEqual(str(context.exception), f"procedure {name} not defined")

    def test_procedure_invocation_invalid_argument_length(self):
        # arrange
        name = "SampleProcedure"
        values = [1]

        # act
        with self.assertRaises(BazilioException) as context:
            self.eval_visitor.procedure_invocation(name, values)

        # assert
        self.assertEqual(
            str(context.exception),
            f"args length not match, {name} was expecting ['arg1', 'arg2'] but was given {values}",
        )

    def test_visitAdd(self):
        # arrange
        parser = self.get_parser("1 + 2")
        ctx = parser.expression()

        # act
        result = self.eval_visitor.visitAdd(ctx)

        # assert
        self.assertEqual(result, 3)

    def test_visitSub(self):
        # arrange
        parser = self.get_parser("1 - 2")
        ctx = parser.expression()

        # act
        result = self.eval_visitor.visitSub(ctx)

        # assert
        self.assertEqual(result, -1)

    def test_visitParenteses(self):
        # arrange
        parser = self.get_parser("(1 - 2) * 2")
        ctx = parser.expression()

        # act
        result = self.eval_visitor.visit(ctx)

        # assert
        self.assertEqual(result, -2)

    def test_visitMod(self):
        # arrange
        parser = self.get_parser("2 % 2")
        ctx = parser.expression()

        # act
        result = self.eval_visitor.visitMod(ctx)

        # assert
        self.assertEqual(result, 0)

    def test_visitMul(self):
        # arrange
        parser = self.get_parser("2 * 2")
        ctx = parser.expression()

        # act
        result = self.eval_visitor.visitMul(ctx)

        # assert
        self.assertEqual(result, 4)

    def test_visitVar(self):
        # arrange
        parser = self.get_parser("myVar")
        ctx = parser.expression()
        self.eval_visitor.stack.append({"myVar": 42})

        parser2 = self.get_parser("myVar2")
        ctx2 = parser2.expression()

        # act
        result = self.eval_visitor.visitVar(ctx)
        result2 = self.eval_visitor.visitVar(ctx2)

        # assert
        self.assertEqual(result, 42)
        self.assertEqual(result2, 0)

    def test_visitAssignment(self):
        # arrange
        parser = self.get_parser("myVar <- 42")
        ctx = parser.assignment()
        self.eval_visitor.stack.append({})

        # act
        self.eval_visitor.visitAssignment(ctx)

        # assert
        self.assertEqual(self.eval_visitor.stack[0]["myVar"], 42)

    def test_visitAssignmentList(self):
        # arrange
        parser = self.get_parser("myVar <- { 40 + 2 }")
        ctx = parser.assignment()
        self.eval_visitor.stack.append({})

        # act
        self.eval_visitor.visitAssignment(ctx)

        # assert
        self.assertEqual(self.eval_visitor.stack[0]["myVar"], [42])

    def test_visitLt(self):
        # arrange
        parser = self.get_parser("2 < 2")
        ctx = parser.expression()

        parser2 = self.get_parser("1 < 2")
        ctx2 = parser2.expression()

        # act
        result = self.eval_visitor.visitLt(ctx)
        result2 = self.eval_visitor.visitLt(ctx2)

        # assert
        self.assertEqual(result, 0)
        self.assertEqual(result2, 1)

    def test_visitString(self):
        # arrange
        parser = self.get_parser('"mystring"')
        ctx = parser.expression()

        # act
        result = self.eval_visitor.visitString(ctx)

        # assert
        self.assertEqual(result, "mystring")

    def test_visitDiv(self):
        # arrange
        parser = self.get_parser("2 / 2")
        ctx = parser.expression()

        parser2 = self.get_parser("2 / 0")
        ctx2 = parser2.expression()

        # act
        result = self.eval_visitor.visitDiv(ctx)
        with self.assertRaises(BazilioException) as context:
            self.eval_visitor.visitDiv(ctx2)

        # assert
        self.assertEqual(result, 1)
        self.assertEqual(str(context.exception), f"cannot divide by zero")

    def test_visitNote(self):
        # arrange
        parser = self.get_parser("A0")
        ctx = parser.expression()

        parser2 = self.get_parser("A")
        ctx2 = parser2.expression()

        # act
        result = self.eval_visitor.visitNote(ctx)
        result2 = self.eval_visitor.visitNote(ctx2)

        # assert
        self.assertEqual(result, 0)
        self.assertEqual(result2, 28)

    def test_visitLte(self):
        # arrange
        parser = self.get_parser("3 <= 2")
        ctx = parser.expression()

        parser2 = self.get_parser("2 <= 2")
        ctx2 = parser2.expression()

        # act
        result = self.eval_visitor.visitLte(ctx)
        result2 = self.eval_visitor.visitLte(ctx2)

        # assert
        self.assertEqual(result, 0)
        self.assertEqual(result2, 1)

    def test_visitGte(self):
        # arrange
        parser = self.get_parser("2 >= 3")
        ctx = parser.expression()

        parser2 = self.get_parser("2 >= 2")
        ctx2 = parser2.expression()

        # act
        result = self.eval_visitor.visitGte(ctx)
        result2 = self.eval_visitor.visitGte(ctx2)

        # assert
        self.assertEqual(result, 0)
        self.assertEqual(result2, 1)

    def test_visitNeq(self):
        # arrange
        parser = self.get_parser("3 /= 3")
        ctx = parser.expression()

        parser2 = self.get_parser("2 /= 3")
        ctx2 = parser2.expression()

        # act
        result = self.eval_visitor.visitNeq(ctx)
        result2 = self.eval_visitor.visitNeq(ctx2)

        # assert
        self.assertEqual(result, 0)
        self.assertEqual(result2, 1)

    def test_visitListExpr(self):
        # arrange
        parser = self.get_parser("{ 1 0 }")
        ctx = parser.list_expression()

        # act
        result = self.eval_visitor.visitList_expression(ctx)

        # assert
        self.assertEqual(result, [1, 0])

    def test_visitListSize(self):
        # arrange
        parser = self.get_parser("#myVar")
        ctx = parser.expression()
        self.eval_visitor.stack.append({"myVar": [0, 1]})

        # act
        result = self.eval_visitor.visitListSize(ctx)

        # assert
        self.assertEqual(result, 2)

    def test_visitListQuery(self):
        # arrange
        parser = self.get_parser("myVar[0 + 1]")
        ctx = parser.expression()
        self.eval_visitor.stack.append({"myVar": [0, 1]})

        # act
        result = self.eval_visitor.visitListQuery(ctx)

        # assert
        self.assertEqual(result, 0)

    def test_visitList_add(self):
        # arrange
        parser = self.get_parser("myList << 5")
        ctx = parser.list_add()
        self.eval_visitor.stack.append({"myList": [0, 1]})

        # act
        self.eval_visitor.visitList_add(ctx)

        # assert
        my_list = self.eval_visitor.actual_stack["myList"]
        self.assertEqual(3, len(my_list))
        self.assertEqual(5, my_list[2])

    def test_visitList_cut(self):
        # arrange
        parser = self.get_parser("8< myList[4]")
        ctx = parser.list_cut()

        parser2 = self.get_parser("8< myList[1]")
        ctx2 = parser2.list_cut()

        self.eval_visitor.stack.append({"myList": [0, 1]})

        # act
        with self.assertRaises(BazilioException) as context:
            self.eval_visitor.visitList_cut(ctx)

        self.eval_visitor.visitList_cut(ctx2)

        # assert
        my_list = self.eval_visitor.actual_stack["myList"]
        self.assertEqual(1, len(my_list))
        self.assertEqual(1, my_list[0])

    @patch("builtins.input", return_value="12")
    def test_input_good(self, mock_input):
        # arrange
        parser = self.get_parser("<?> myVar")
        ctx = parser.input_()
        self.eval_visitor.stack.append({})

        # act
        self.eval_visitor.visitInput_(ctx)

        # assert
        myVar = self.eval_visitor.actual_stack["myVar"]
        self.assertEqual(myVar, 12)

    def test_visitOutput_(self):
        # arrange
        parser = self.get_parser('<w> myVar "->" myVar')
        ctx = parser.output_()
        self.eval_visitor.stack.append({"myVar": 1})

        # act
        self.eval_visitor.visitOutput_(ctx)

        # assert
        self.assertEqual(["1 -> 1"], self.eval_visitor.outputs)

    def test_visitReproduction(self):
        # arrange
        parser = self.get_parser("(:) 1 + 2")
        ctx = parser.reproduction()

        # act
        self.eval_visitor.visitReproduction(ctx)

        # assert
        self.assertEqual([3], self.eval_visitor.score)

    def test_visitWhile_(self):
        # arrange
        self.eval_visitor.stack.append({})
        parser = self.get_parser("myVar <- 1")
        ctx = parser.assignment()
        self.eval_visitor.visitAssignment(ctx)

        parser = self.get_parser("while myVar < 3 |: myVar <- myVar + 1 :|")
        ctx = parser.while_()

        # act
        self.eval_visitor.visitWhile_(ctx)

        # assert
        self.assertEqual(3, self.eval_visitor.actual_stack["myVar"])

    def test_visitCondition(self):
        # arrange
        self.eval_visitor.stack.append({})
        parser = self.get_parser("myVar <- 1")
        ctx = parser.assignment()
        self.eval_visitor.visitAssignment(ctx)

        parser = self.get_parser("if myVar = 1 |: result <- 2 :|")
        ctx = parser.condition()

        parser2 = self.get_parser(
            "if myVar /= 1 |: result2 <- 2 :| else |: result2 <- 3 :|"
        )
        ctx2 = parser2.condition()

        parser3 = self.get_parser(
            "if myVar = 1 |: result3 <- 2 :| else |: result3 <- 3 :|"
        )
        ctx3 = parser3.condition()

        # act
        self.eval_visitor.visitCondition(ctx)
        self.eval_visitor.visitCondition(ctx2)
        self.eval_visitor.visitCondition(ctx3)

        # assert
        self.assertEqual(2, self.eval_visitor.actual_stack["result"])
        self.assertEqual(3, self.eval_visitor.actual_stack["result2"])
        self.assertEqual(2, self.eval_visitor.actual_stack["result3"])

    def test_visitProcedure(self):
        # arrange
        self.eval_visitor.stack.append({})
        parser = self.get_parser("""Main |: <w> "Hello Bazilio" :|""")
        ctx = parser.procedure()

        # act
        self.eval_visitor.visitProcedure(ctx)

        # assert
        self.assertEqual(2, len(self.eval_visitor.procedures_definition))
        proc_def = self.eval_visitor.procedures_definition["Main"]
        self.assertEqual("Main", proc_def.name)

    def test_visitProcedure_call(self):
        # arrange
        self.eval_visitor.stack.append({})
        parser = self.get_parser("""Main |: <w> "Hello Bazilio" :|""")
        ctx = parser.procedure()
        self.eval_visitor.visitProcedure(ctx)

        parser = self.get_parser("""Main""")
        ctx = parser.procedure_call()

        # act
        self.eval_visitor.visitProcedure_call(ctx)

        # assert
        self.assertEqual(["Hello Bazilio"], self.eval_visitor.outputs)

    def test_euclides(self):
        # arrange
        parser = self.get_parser(
            """
### program that reads two integers and writes their greatest common divisor ###
Euclides a b |:
    while a /= b |:
        if a > b |:
            a <- a - b
        :| else |:
            b <- b - a
        :|
    :|
    <w> a
:|"""
        )
        ctx = parser.root()
        self.eval_visitor.visitRoot(ctx)

        parser = self.get_parser("""Euclides 6 12""")
        ctx = parser.procedure_call()

        # act
        self.eval_visitor.visitProcedure_call(ctx)

        # assert
        self.assertEqual(["6"], self.eval_visitor.outputs)

    def test_hanoi(self):
        # arrange
        parser = self.get_parser(
            """
### program that reads two integers and writes their greatest common divisor ###
Hanoi n ori dst aux |:
    if n > 0 |:
        Hanoi (n - 1) ori aux dst
        <w> ori "->" dst
        Hanoi (n - 1) aux dst ori
    :|
:|"""
        )
        ctx = parser.root()
        self.eval_visitor.visitRoot(ctx)

        parser = self.get_parser("""Hanoi 3 1 2 3""")
        ctx = parser.procedure_call()

        # act
        self.eval_visitor.visitProcedure_call(ctx)

        # assert
        self.assertEqual(
            [
                "1 -> 2",
                "1 -> 3",
                "2 -> 3",
                "1 -> 2",
                "3 -> 1",
                "3 -> 2",
                "1 -> 2",
            ],
            self.eval_visitor.outputs,
        )

    def test_hanoi_rec(self):
        # arrange
        parser = self.get_parser(
            """
Hanoi |:
    src <- {C D E F G}
    dst <- {}
    aux <- {}
    HanoiRec #src src dst aux
:|

HanoiRec n src dst aux |:
    if n > 0 |:
        HanoiRec (n - 1) src aux dst
        note <- src[#src]
        8< src[#src]
        dst << note
        (:) note
        HanoiRec (n - 1) aux dst src
    :|
:|
"""
        )
        ctx = parser.root()
        self.eval_visitor.visitRoot(ctx)

        parser = self.get_parser("""Hanoi""")
        ctx = parser.procedure_call()

        # act
        self.eval_visitor.visitProcedure_call(ctx)

        # assert
        self.assertEqual(31, len(self.eval_visitor.score))


if __name__ == "__main__":
    unittest.main()
