
from lambda_parser import Lambda_Parser
from grammar import Function, Application


if __name__ == "__main__":
    print("Welcome to Lamda Hat. <:)")
    parser = Lambda_Parser()

    #application = Application("($x.x)y")
    #print(application.evaluate())

    # func = Function("$x.x")
    # print(func.evaluate())

    #print(func.evaluate("y"))
    while True:
        print("Enter a lambda expression to be evaluated. Valid lambda syntax: ($x.x)")
        s = input(">>")
        try :
            parsed_input = parser.parse_input(s)

        except Exception as error:
            print(f"\n!!!!\nError: {str(error)}\n!!!!\n")
            continue
