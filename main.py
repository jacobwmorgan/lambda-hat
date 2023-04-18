
from lambda_parser import Lambda_Parser
from grammar import Function, Application
import lambda_helper as helper


if __name__ == "__main__":
    print("Welcome to Lamda Hat. <:)")
    parser = Lambda_Parser()

    #application = Application("($x.x)y")
    #print(application.evaluate())

    # func = Function("$x.x")
    # print(func.evaluate())
    #print(helper.mutate_string("(($x.x)($x.x))"))

    #while True:
    # print(helper.beta_reduction("($x.x)") == "($x.x)")
    # print(helper.beta_reduction("(($x.x)y)") == "(($x.x)y)")
    # print(helper.beta_reduction("(($x.x)($x.x))") == "(($x.x)($x.x))")
    # print(helper.beta_reduction("($x y.x y)") == "($x.($y.(x y)))")

    #print(helper.mutate_string(input(">>")))
    #print(func.evaluate("y"))
    #print(helper.get_grammar_type("(($x.x)y)").evaluate())
    #print(helper.is_name("x"))
    #parser.parse_input("(($x.x)y)")
    print(helper.is_name("x y"))
    while True:
        print("Enter a lambda expression to be evaluated. Valid lambda syntax: ($x.x)")
        s = input(">>")
        parsed_input = parser.parse_input(s)
        # try :

        # except Exception as error:
        #     print(f"\n!!!!\nError: {str(error)}\n!!!!\n")
        #     continue
