from database import DBConnection

db = DBConnection()


def add_context(user_input):
    # add user
    return user_input


def prompt(query):
    return query


def store(query, response):
    pass


def main():
    while True:
        user_input = input("> ")
        if user_input == "q":
            break

        query = add_context(user_input)
        response = prompt(query)
        print(response)
        store(query, response)


if __name__ == "__main__":
    main()
