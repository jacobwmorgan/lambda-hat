from lambda_parser import Lambda_Parser
from grammar import Function, Application
import lambda_helper as helper


if __name__ == "__main__":
    print("Welcome to Lambda Hat. <:)")
    parser = Lambda_Parser()

    while True:
        try:
            print("Enter a lambda expression to be evaluated. Valid lambda syntax: ($x.x)")
            s = input(">>")
            parsed_input = parser.parse_input(s)
        except Exception as e:
            print("Invalid lambda expression.")
