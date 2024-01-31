from mongoengine import (
    Document,
    StringField,
    DateTimeField,
    ListField,
    ReferenceField,
)


class Author(Document):
    fullname = StringField()
    born_date = DateTimeField()
    born_location = StringField()
    description = StringField()

    # def __str__(self):
    #     obj_2_str = f"""
    #     Author(
    #         fullname = {self.fullname},
    #         born_date = {self.born_date},
    #         born_location = {self.born_location},
    #         description = {self.description},
    #         )
    #     """
    #     return obj_2_str


class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField()

    # def __str__(self):
    #     obj_2_str = f"""
    #     Quotes(
    #         tags = {self.tags},
    #         author = {self.author.fullname},
    #         quote = {self.quote},
    #         )
    #     """
    #     return obj_2_str
