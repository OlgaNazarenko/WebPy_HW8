import sys

from src.models import Authors, Quotes
from src import connect

quotes = Quotes.objects()
authors = Authors.objects


def main():
    while True:
        query = input('Command(either tag, tags, name, or exit): value>>>')

        if query.strip() == "exit":
            print("Goodbye")
            sys.exit()

        command, value = query.strip().split(':')
        value = value.strip()

        if command == "name":
            authors_with_name = [author.fullname for author in authors if value in author.fullname]

            for author in authors_with_name:
                quotes_with_name = Quotes.objects(author__in = authors)
                print(f' quotes with name "{value}": \n {[quote.quote for quote in quotes_with_name]}')

        elif command == "tag":
            quotes_with_tag = [quote.quote for quote in quotes if value in quote.tags]
            print(f'Quotes with tag "{value}": \n {quotes_with_tag}')

        elif command == "tags":
            tags = value.split(',')
            quotes_with_tags = [quote.quote for quote in quotes if any(tag in quote.tags for tag in tags)]
            print(f'Quotes with tags "{value}": \n {quotes_with_tags}')


if __name__ == "__main__":
    main()