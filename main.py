
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

    while True:
        print(helper.mutate_string(input(">>")))
    #print(func.evaluate("y"))
    # while True:
    #     print("Enter a lambda expression to be evaluated. Valid lambda syntax: ($x.x)")
    #     s = input(">>")
    #     parsed_input = parser.parse_input(s)
        # try :

        # except Exception as error:
        #     print(f"\n!!!!\nError: {str(error)}\n!!!!\n")
        #     continue
