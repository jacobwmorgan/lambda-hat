#pylint: disable = consider-using-enumerate, invalid-name, missing-class-docstring, missing-function-docstring
from grammar import Application, Expression, Function, Name
import lambda_helper as helper


class Lambda_Parser:
    def __init__(self):
        self.lambda_expression = ""

    def parse_input(self,s):
        # Grammar rules:
        # <expression> = <name> | <function> | <application>
        # <function> = ($<name>.<expression>)
        # <application> = (<function><expression>)
        # <name> = [a-z] +

        # Check if value is actually a string
        if not isinstance(s, str):
            raise TypeError("Input must be a string.")
        # Check if amount of opening and closing parentheses match
        opening_parens_count = s.count("(")
        closing_parens_count = s.count(")")
        if opening_parens_count != closing_parens_count:
            raise ValueError("Mismatched number of parentheses.")
       
        s = helper.beta_reduction(s)
        expression = helper.get_grammar_type(s)
        print (expression.evaluate().replace("$", "λ"))
        return s

    def get_parse_input(self):
        return self.lambda_expression