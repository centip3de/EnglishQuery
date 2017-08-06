import sys
from lexer import Lexer
from parser import Parser

def main():
    lexer = Lexer("")
    parser = Parser("")
    while True:
        try:
            user_input = input("> ").lower().strip()
            if user_input != "quit" and user_input != "exit":
                lexer.text = user_input
                tokens = lexer.lex()
                parser.tokens = tokens
                print(str(parser.step()))
            else:
                break

        except:
            print("An error has occured.", file=sys.stderr)

if __name__ == "__main__":
    main()
