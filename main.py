from database import DBConnection
from transformer import Transformer
from model import Model
from memory import Memory

db = DBConnection()
t = Transformer()
model = Model()  # TODO: Update later if necessary based on Model implementation

top_k = 5


def add_context(user_input: str) -> str:
    memories = db.retrieve_all_memories()
    t.sort_by_relevance(memories, user_input)
    query: str = user_input

    query += "\n\n---ADDITIONAL CONTEXT FROM PREVIOUS CONVERSATIONS HAS BEEN ADDED BELOW---\n\n"

    for i in range(top_k):
        if i > len(memories) - 1:
            break
        memories[i].importance += 1
        db.update_importance(memories[i])
        query += memories[i].content

    return query


def prompt(query: str) -> str:
    return model.prompt(query)


def store(query: str, response: str) -> None:
    new_memory = Memory(
        content=query + response,
        embedding=t.encode(query + response),
        importance=1,
    )
    db.store_memory(new_memory)


def main():
    while True:
        user_input = input("> ")
        if user_input == "q":
            break

        query = add_context(user_input)
        response = prompt(query)
        print(response)
        store(user_input, response)


if __name__ == "__main__":
    main()
