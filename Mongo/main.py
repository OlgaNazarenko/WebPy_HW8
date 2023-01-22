from Mongo.models import Quotes, Authors
import connect

quotes = Quotes.objects()
authors = Authors.objects


def main() :
    while True :
        query = input('Command(either: tag, tags, name, or exit): value>>>')
        command, value = query.strip().split(':')
        value = value.strip()

        if command == "name" :
            result = [author.fullname for author in authors if value in author.fullname]
            for res in result:
                print(res)
                if value in res :
                    quotes_with_name = [quote.quote for quote in quotes if value in quote.fullname]
                    print(f'Quotes with name "{value}": \n {quotes_with_name}')

        elif command == "tag":
            quotes_with_tag = [quote.quote for quote in quotes if value in quote.tags]
            print(f'Quotes with tag "{value}": \n {quotes_with_tag}')

        elif command == "tags":
            tags = value.split(',')
            quotes_with_tags = [quote.quote for quote in quotes if any(tag in quote.tags for tag in tags)]
            print(f'Quotes with tags "{value}": \n {quotes_with_tags}')

        elif command == "exit":
            print('Good bye')
            break


if __name__ == "__main__":
    main()