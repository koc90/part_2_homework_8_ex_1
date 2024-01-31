from connect import connection
from models import Author, Quote
from seeds import read_jsons_from_file
from random import choices, randint
import logging

logging.basicConfig(level=logging.DEBUG)


def create_tag_name_list():
    jsons = read_jsons_from_file("quotes.json")
    tags_name = []

    for json in jsons:
        tags_name.extend(json["tags"])

    tags_name = set(tags_name)
    tags_name = list(tags_name)

    return tags_name


def list_of_dict_to_list(quotes_list_of_dicts: list[dict]) -> list:
    quotes = []

    for quote_dict in quotes_list_of_dicts:
        for quote in quote_dict.values():
            quotes.append(quote)

    return quotes


def query_name(value: str) -> list:
    logging.debug(f"query_name function called with value: {value}")

    quotes_list_of_dicts = list(
        Quote.objects(author=Author.objects(fullname=value).first())
        .fields(quote=1, id=0)
        .as_pymongo()
    )

    # quotes_list_of_dicts = list(
    #     Quote.objects(author__fullname=value).fields(quote=1, id=0).as_pymongo()
    # )
    # To chyba dziala tylko na EmbeddedDocument

    return quotes_list_of_dicts


def try_query_name():
    authors = ["Albert Einstein", "Steve Martin"]
    for author in authors:
        quotes_list_of_dicts = query_name(author)
        list_of_quotes = list_of_dict_to_list(quotes_list_of_dicts)

        print(list_of_quotes)


def query_tags(value: str):
    logging.debug(f"query_tags function called with value: {value}")

    tags_name = value.split(",")
    print(tags_name)

    quotes_list_of_dicts = list(
        Quote.objects(tags__in=tags_name).fields(quote=1, id=0).as_pymongo()
    )

    return quotes_list_of_dicts


def try_query_tags():
    tags_name = create_tag_name_list()
    tags_list = choices(tags_name, k=randint(1, 5))
    tags_str = ",".join(tags_list)

    print(tags_str)
    quotes_list_of_dicts = query_tags(tags_str)
    list_of_quotes = list_of_dict_to_list(quotes_list_of_dicts)
    print(list_of_quotes)


if __name__ == "__main__":
    try_query_name()
    try_query_tags()
