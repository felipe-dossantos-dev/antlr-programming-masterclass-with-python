import unittest
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

    def test_visitAssignment(self):
        # arrange
        parser = self.get_parser("MyVar <- 42")
        ctx = parser.assignment()
        self.eval_visitor.stack.append({})

        # act
        self.eval_visitor.visitAssignment(ctx)

        # assert
        self.assertEqual(self.eval_visitor.stack[0]["MyVar"], 42)


if __name__ == "__main__":
    unittest.main()
