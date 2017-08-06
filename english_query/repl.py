from lexer import Lexer

def main():
    lexer = Lexer("")
    while True:
        user_input = input("> ")
        if user_input.lower() != "quit" or user_input.lower() != "exit":
            lexer.text = user_input
            print(lexer.lex())
        else:
            break

if __name__ == "__main__":
    main()
