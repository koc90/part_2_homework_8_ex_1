from connect import connection
import logging
from queries import query_name, query_tags, list_of_dict_to_list


logging.basicConfig(level=logging.DEBUG)


COMMANDS = {
    "name": query_name,
    "tag": query_tags,
    "tags": query_tags,
}


def parse_phrase(phrase):
    try:
        (commnand, value) = phrase.split(":")
        return (commnand, value)
    except Exception as e:
        logging.error("Wrong form of command")
        return (None, None)


def main():
    print("Hello, I am a quote searcher.")

    while True:
        print(
            "\n\nWrite the command in the following form: \nkeyword:value (eg. name:Steve Martin). There is no space near the ':'.\nYou can also input 'exit' to quit"
        )
        phrase = input()

        if phrase.lower() == "exit":
            break

        (command, value) = parse_phrase(phrase)

        try:
            logging.debug(f"    command = {command}     value = {value}")
            result = COMMANDS[command](value)
        except:
            print("I don't understand what do you want. Try again")
        else:
            list_of_quotes = list_of_dict_to_list(result)
            print("")
            print("Searched quotes:")
            print(list_of_quotes)


if __name__ == "__main__":
    main()
