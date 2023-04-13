#pylint: disable = consider-using-enumerate, invalid-name, missing-class-docstring, missing-function-docstring
import grammar as g

def get_grammar_type(s):
    print(f"Called get_grammar_type with string {s}")
    no_paren = remove_outer_parentheses(s)
    grammar_type = None
    if is_function(no_paren):
        grammar_type = g.Function(no_paren)
    elif is_application(no_paren):
        grammar_type = g.Application(no_paren)
    elif is_name(no_paren):
        grammar_type = g.Name(no_paren)
    return grammar_type

def is_expression(s):
    print(f"Called is_expression with string {s}")
    no_paren= remove_outer_parentheses(s)
    if not is_function(no_paren) and not is_application(no_paren) and not is_name(no_paren):
        return False

    return True

def is_function(s):
    # <function> = ($<name>.<expression>)
    print(f"Called is_function with string {s}")
    starts_with_lambda= s[0] == '$'
    if not starts_with_lambda:
        return False
    
    contains_full_stop= s.count(".") == 0
    if contains_full_stop:
        return False

    full_stop_index= s.index(".")
    name = s[1: full_stop_index]
    if not is_name(name):
        return False
    
    expression= s[full_stop_index+1: len(s)]
    expression= get_grammar_type(expression)
    if expression is None:
        return False

    return True

def is_application(s):
    # <application> = (<function><expression>)
    # (($x.x)y)
    # (($x.x)($x.x))
    print(f"Called is_application with string {s}")
    # can't be an application without at least a $ and a . so therefore anything less than 2 isn't an application.
    if len(s) <= 2:
        return False
    # split string at first closing parenthesis, remove that set of parenthesis and then get expression on the rest
    (start_index, end_index) = get_parentheses_indexes(s)
    # slice string from index j to index i
    body = s[start_index+1: end_index]
    if not is_function(body):
        return False

    spliced_string= ""
    for i in range(len(s)):
        if not (i > start_index-1 and i < end_index + 1):
            spliced_string += s[i]
    if not is_expression(spliced_string):
        return False

    return True
    return False  # terry davis told me to put this here
    # gödel moment :)

def get_parentheses_indexes(self, s):
    for i in range(len(s)):
        if s[i] == ")":
            for j in range(i, -1, -1):
                if s[j] == "(":
                    return (j, i)

def remove_outer_parentheses(s):
    if s[0] == '(' and s[len(s)-1] == ')':
        return s[1: len(s)-1]
    return s

def is_name(s):
    print(f"Called is_name with string {s}")
    if s[0] == '(' and s[len(s)-1] == ')':
        return s[1: len(s)-1].isalpha()
    return s.isalpha()
 
 def mutate_string(s):
    # lambda x y.x y = lambda x.(lambda y.(x y))
    # ($x y. xy) => ($x.($y.(x y)))
