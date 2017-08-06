from lexer import Lexer

def main():
    lexer = Lexer("")
    while True:
        user_input = input("> ").lower().strip()
        if user_input != "quit" and user_input != "exit":
            lexer.text = user_input
            print(lexer.lex())
        else:
            break

if __name__ == "__main__":
    main()
