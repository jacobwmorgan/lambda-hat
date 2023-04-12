class Expression:
    """ <expression> = <name> | <function> | <application>"""
    def __init__(self):
        pass

    def evaluate(self):
        """Apply the lambda expression to the argument"""
        return 0
    
    def return_type(self):
        """Returns the type of the expression."""
        if type(self) == Application:
            return "<application>"
        elif type(self) == Function:
            return "<function>"
        elif type(self) == Name:
            return "<name>"
        else:   
            return "<expression>"

class Application(Expression):
    """ <application> = (<function><expression>)"""
    def __init__(self,app):
        self.application = app 

class Function(Expression) :
    """ <function> = ($<name>.<expression>)"""
    def __init__(self,s):
        self.function = s
        self.name = self.splice_function()[0]
        self.expression = self.splice_function()[1]


    def splice_function(self):
        """Splices the function into a list of [name, expression]"""
        full_stop_index = self.function.index(".")
        name = self.function[1:full_stop_index]
        expression = self.function[full_stop_index+1: len(self.function)]

        return [name,expression]

class Name(Expression) :
    """ <name> = [a-z] +"""
    def __init__(self,s):
        self.name = s
