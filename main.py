def add_context(user_input):
    return user_input


def prompt(query):
    return query


def repl():
    while True:
        user_input = input("> ")
        if user_input == "q":
            break
        query = add_context(user_input)
        prompt(query)


def main():
    repl()


if __name__ == "__main__":
    main()
