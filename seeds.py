import json
from models import Author, Quote
from dateutil.parser import parse
from connect import connection


def clear_all():
    try:
        Quote.objects().delete()
    except Exception as e:
        print(e)

    try:
        Author.objects().delete()
    except Exception as e:
        print(e)


def read_jsons_from_file(file) -> list:
    with open(file, "r", encoding="utf-8") as f:
        jsons_from_file = json.load(
            f,
        )

    return jsons_from_file


def create_authors_to_db():
    file = "authors.json"
    author_jsons = read_jsons_from_file(file)

    # fullname = StringField()
    # born_date = DateTimeField()
    # born_location = StringField()
    # description = StringField()
    authors = []

    for author_json in author_jsons:
        author = Author(
            fullname=author_json["fullname"],
            born_date=parse(author_json["born_date"]).date(),
            born_location=author_json["born_location"],
            description=author_json["description"],
        )
        author.save()
        # print(author)

        authors.append(author)

    return authors


def create_quotes_to_db():  # arg: authors: list[Author]
    file = "quotes.json"
    quote_jsons = read_jsons_from_file(file)

    # tags = ListField()
    # author = ReferenceField(Authors)
    # quote = StringField()

    quotes = []

    for quote_json in quote_jsons:
        this_author = None
        # authors = Author.objects()
        # print(type(authors))
        for author in Author.objects():
            if author.fullname == quote_json["author"]:
                this_author = author

        quote = Quote(
            tags=quote_json["tags"], author=this_author, quote=quote_json["quote"]
        )
        quote.save()

        quotes.append(quote)

    return quotes


def upload(objects: list):
    for object in objects:
        object.save()


def download_and_print(cls):
    print("\n   ", cls, "\n")
    objects = cls.objects()
    for object in objects:
        print(object.to_mongo().to_dict())
        print(type(object))
        for key, value in object._fields.items():
            print(key, type(value))

    return objects


if __name__ == "__main__":
    # drop_all()
    clear_all()
    # authors = create_authors_to_db()
    # quotes = create_quotes_to_db(authors)
    # tags = create_tags_to_db(quotes)
    create_authors_to_db()
    create_quotes_to_db()

    # upload(authors)
    # upload(quotes)
    # upload(tags)
    # upload(tags)
    download_and_print(Author)
    download_and_print(Quote)
