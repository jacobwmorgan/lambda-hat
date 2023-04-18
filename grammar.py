#pylint: disable = consider-using-enumerate, invalid-name, missing-class-docstring, missing-function-docstring
import lambda_helper as helper

class Expression:
    """ <expression> = <name> | <function> | <application>"""
    def __init__(self):
        pass
    # def evaluate(self):
    #     """Apply the lambda expression to the argument"""
    #     return 0

    def evaluate(self, s = ""):
        return "balls"

    def return_type(self):
        """Returns the type of the expression."""
        # (($x.x)($x.x))
        if isinstance(self, Application):
            return "<application>"
        elif isinstance(self, Function):
            return "<function>"
        elif isinstance(self, Name):
            return "<name>"
        else: 
            return "<expression>"
        
    def get_function(self, s):
        (start_index, end_index) = helper.get_parentheses_indexes(s)
        function = s[start_index+1:end_index]
        print(function)
        return Function(function)

    def get_expression(self, s):
        if s[0] == '(':
            (start_index, end_index) = helper.get_parentheses_indexes(s)
            expression = ""
            for i in range(len(s)):
                if not (i > start_index-1 and i < end_index + 1):
                    expression += s[i]
        else:
            expression = s
        return helper.get_grammar_type(expression)

class Application(Expression):
    """ <application> = ((<function>)<expression>)"""
    def __init__(self,s):
        self.function = self.get_function(s)
        self.expression = self.get_expression(s)
      
    def evaluate(self, s=""):
        evaluated = self.expression.evaluate()
        #print(self.function.expression.name)
        #print(evaluated)
        return self.function.evaluate(evaluated)
       
class Function(Expression) :
    """ <function> = ($<name>.<expression>)"""
    def __init__(self,s):
        self.function = s
        (name, expression) = self.splice_function()
        self.name = Name(name)
        #print(expression)
        self.expression = self.get_expression(expression)
        #print(self.name)
        #print(self.expression)

    def splice_function(self):
        """Splices the function into a list of [name, expression]"""
        full_stop_index = self.function.index(".")
        name = self.function[1:full_stop_index]
        expression = self.function[full_stop_index+1: len(self.function)]

        return [name,expression]
    
    def evaluate(self, s = ""):
        if s == "":
            return self.function
        
        # print(isinstance(self.expression, Name))
        # print(self.name)
        # print(self.expression.name)
        print(self.name.name)
        if isinstance(self.expression, Name) and self.name.name == self.expression.name:
            return s
        return self.expression.evaluate(s)

class Name(Expression) :
    """ <name> = [a-z] +"""
    def __init__(self,s):
        self.name = s
    
    def evaluate(self, s=""):
        return self.name
