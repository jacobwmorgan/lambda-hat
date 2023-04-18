#pylint: disable = consider-using-enumerate, invalid-name, missing-class-docstring, missing-function-docstring
import grammar as g

def get_grammar_type(s):
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
    no_paren= remove_outer_parentheses(s)
    if not is_function(no_paren) and not is_application(no_paren) and not is_name(no_paren):
        return False

    return True

def is_function(s):
    # <function> = ($<name>.<expression>)
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
    # can't be an application without at least a $ and a . so therefore anything less than 2 isn't an application.
    if len(s) <= 2 or '$' not in s or '.' not in s:
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
    # gödel moment :)

def get_parentheses_indexes(s):
    for i in range(len(s)):
        if s[i] == ")":
            for j in range(i, -1, -1):
                if s[j] == "(":
                    return (j, i)

def get_parentheses_at_index(s, index_skip):
    end_paren_index = -1
    # average unity developer
    for i in range(len(s)):
        if s[i] == ")":
            end_paren_index += 1
            if end_paren_index == index_skip:
                for j in range(i, -1, -1):
                    if s[j] == "(":
                        return (j, i)
    return (0, len(s))

def remove_outer_parentheses(s):
    if s[0] == '(' and s[len(s)-1] == ')':
        return s[1: len(s)-1]
    return s

def is_name(s):
    no_spaces = s.replace(" ", "")
    return no_spaces.isalpha()


def beta_reduction(s):
    expressions = get_expressions_from_string(s)
    new_expressions = []
    # Lambda functions with multiple names are perfectly valid! However,
    # in their regular input form we cannot evaluate them, so we need to 
    # calculate if there is multiple names in a given lambda function,
    # and if there is, split it up into a lambda evaluatable format.
    for exp in expressions:
        if "$" in exp:
            # This is a lambda function, evaluate if we need to change it
            names = exp[exp.index("$") + 1: exp.index(".")].split(" ")
            returns = exp[exp.index(".")+1 : len(exp)]
            new_string = "("
            # We only want to actually change it if there's more than one name in this function
            if len(names) > 1:
                for name in names:
                    new_string += f"${name}.("
                new_string += f"{returns}"
                new_string += ")" * (len(names) + 1)
                new_expressions.append(new_string)
            else:
                # It's a function, it needs to be encased in parentheses
                new_expressions.append("(" + exp + ")")
        else:
            # This expression was just a name, no need to encase
            new_expressions.append(exp)

    # Construct our new string!
    s = ""
    for new_exp in new_expressions:
        s += new_exp
    
    # If we end on a name or have multiple expressions,
    # encase the whole return string in parentheses
    if s[len(s) -1].isalpha() or len(expressions) > 1:
        s = "(" + s + ")"

    return s

def get_expressions_from_string(s):
    expressions = []
    min_index = 0
    for i in range(s.count('(')):
        (start_index, end_index) = get_parentheses_at_index(s, i)
        if start_index < min_index:
            start_index = min_index
        expression = s[start_index+1:end_index]
        expressions.append(expression)
        min_index = end_index
    return expressions