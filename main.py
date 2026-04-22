from database import DBConnection


def add_context(user_input):
    return user_input


def prompt(query):
    return query


def main():
    db = DBConnection()

    while True:
        user_input = input("> ")
        if user_input == "q":
            break

        query = add_context(user_input)
        response = prompt(query)
        print(response)


if __name__ == "__main__":
    main()
