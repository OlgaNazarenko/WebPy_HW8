import json
import datetime

from models import Authors, Quotes


def open_authors_file():
    Authors.drop_collection()

    with open('files/authors.json', 'r') as file:
        authors = json.load(file)

        # authors = Authors.objects()

        for a in authors:
            author = Authors(
                fullname = a['fullname'],
                born_date = datetime.strptime(a['born_date'], "B% %d %Y"),
                born_location= a['born_location'],
                description = a['description']
            )
            author.save()


def open_quotes_file():
    Quotes.drop_collection()

    with open('files/quotes.json', 'r') as file:
        quotes = json.load(file)

        # quotes = Quotes.objects()
        for q in quotes:
            quote = Quotes(
                tags = q['tags'],
                author = q['author'],
                quote = q['quote']
            )
            quote.save()
