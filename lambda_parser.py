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

        # check if value is actually a string
        if not isinstance(s, str):
            raise TypeError("Input must be a string.")
        # check if amount of opening and closing parentheses match
        opening_parens_count = s.count("(")
        closing_parens_count = s.count(")")
        print(opening_parens_count, closing_parens_count)
        if opening_parens_count != closing_parens_count:
            raise ValueError("Mismatched number of parentheses.")
        # (($x.x) ($x.x))
        # (($x.x)y)

        # (($x.x)y ($x.x)z)

        # (($x.x) ($x.x))
        # (($x.x))
        # ()

        # ((function) (function))

        # (($x.x)y)
        # (y)
        s = helper.mutate_string(s)
        print(s)
        expression_total = closing_parens_count

        # find the first closing parenthesis, then work backwards to find the matching opening
        # parenthesis. Then, check if the first character is a "$". If it is, then we have a lambda function.
        expressions = []

        expression = helper.get_grammar_type(s)

        # lambda x y.x y = lambda x.(lambda y.(x y))



        print (expression.evaluate().replace("$", "λ"))
        # print(helper.get_grammar_type(s).return_type())
        # for i in range(len(s)):
        #     if s[i] == ")":
        #         for j in range(i, -1, -1):
        #             if s[j] == "(":
        #                 # slice string from index j to index i
        #                 body = s[j+1:i]
                  
        #                 self.get_grammar_type(body)
        #                 # if body[0] != "$":
        #                 #     raise ValueError("Invalid lambda function.")
        #                 # print(body)
        #                 # expressions.append(body)
        #                 break
        #     if len(expressions) == expression_total:
        #         break
        # print(expressions)
        return s

    # def get_grammar_type(self, s):
    #     print(f"Called get_grammar_type with string {s}")
    #     no_paren = self.remove_outer_parentheses(s)
    #     grammar_type = None
    #     if self.is_function(no_paren):
    #         grammar_type = Function(no_paren)
    #     elif self.is_application(no_paren):
    #         grammar_type = Application(no_paren)
    #     elif self.is_name(no_paren):
    #         grammar_type = Name(no_paren)
    #     return grammar_type

    # def is_expression(self, s):
    #     print(f"Called is_expression with string {s}")
    #     no_paren = self.remove_outer_parentheses(s)
    #     if not self.is_function(no_paren) and not self.is_application(no_paren) and not self.is_name(no_paren):
    #         return False
        
    #     return True

    # def is_function(self, s):
    #     # <function> = ($<name>.<expression>)
    #     print(f"Called is_function with string {s}")
    #     starts_with_lambda = s[0] == '$'
    #     if not starts_with_lambda:
    #         return False

    #     contains_full_stop = s.count(".") == 0
    #     if contains_full_stop:
    #         return False

    #     full_stop_index = s.index(".")
    #     name = s[1:full_stop_index]
    #     if not self.is_name(name):
    #         return False

    #     expression = s[full_stop_index+1: len(s)]
    #     expression = self.get_grammar_type(expression)
    #     if expression is None:
    #         return False

    #     return True

    # def is_application(self, s):
    #     # <application> = (<function><expression>)
    #     # (($x.x)y)
    #     # (($x.x)($x.x))
    #     print(f"Called is_application with string {s}")
    #     if len(s) <= 2: # can't be an application without at least a $ and a . so therefore anything less than 2 isn't an application.
    #         return False
    #     # split string at first closing parenthesis, remove that set of parenthesis and then get expression on the rest
    #     for i in range(len(s)):
    #         if s[i] == ")":
    #             for j in range(i, -1, -1):
    #                 if s[j] == "(":
    #                     # slice string from index j to index i
    #                     body = s[j+1:i]
    #                     if not self.is_function(body):
    #                         return False
                        
    #                     spliced_string = ""
    #                     for ii in range(len(s)):
    #                         if not (ii > j-1 and ii < i + 1):
    #                             spliced_string += s[ii]
    #                     if not self.is_expression(spliced_string):
    #                         return False
                        
    #                     return True
    #     return False # terry davis told me to put this here
    #     # gödel moment :)
    
    # def remove_outer_parentheses(self, s):
    #     if s[0] == '(' and s[len(s)-1] == ')':
    #         return s[1:len(s)-1]
    #     return s
    
    # def is_name(self, s):
    #     print(f"Called is_name with string {s}")
    #     if s[0] == '(' and s[len(s)-1] == ')':
    #         return s[1:len(s)-1].isalpha()
    #     return s.isalpha()

    def get_parse_input(self):
        return self.lambda_expression
