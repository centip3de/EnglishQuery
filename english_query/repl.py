from parser import Parser

def main():
    while True:
        user_input = input("> ")
        if user_input.lower() != "quit" or user_input.lower() != "exit":
            print(Parser(user_input).parse())
        else:
            break

if __name__ == "__main__":
    main()
