from lexer import Lexer
from parser import Parser

def main():
    lexer = Lexer("")
    parser = Parser("")
    while True:
        user_input = input("> ").lower().strip()
        if user_input != "quit" and user_input != "exit":
            lexer.text = user_input
            tokens = lexer.lex()
            print("[LEXER] " + str(tokens))
            parser.tokens = tokens
            print("[PARSER] " + str(parser.step()))
        else:
            break

if __name__ == "__main__":
    main()
