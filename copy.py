from Mongo.src.models import Quotes, Authors

quotes = Quotes.objects()
authors = Authors.objects


def main():
    while True:
        list_: list = []
        query: str = input('Command(either: tag, tags, name, or exit): value>>>')

        query_field = query.strip().split(':')

        if query_field[0] == "name":
            result: list = []
            for author in authors:
                if query_field[1].strip() in author.fullname:
                    result.append(author.fullname)

            for res in result:
                print(res)
                if query_field[1].strip() in res:
                    for quote in quotes:
                        list_.append(quote.quote)
                        print(f'Tag "{query_field[1].strip()}": \n {list_}')

        if query_field[0] == "tag":
            for quote in quotes:
                if query_field[1].strip() in quote.tags:
                    list_.append(quote.quote)
                    print(f'Tag "{query_field[1].strip()}": \n {list_}')

        if query_field[0] == "tags":
            for quote in quotes:
                for tag in query_field[1].strip().split(','):
                    if tag in quote.tags:
                        list_.append(quote.quote)
                        print(f'Tags "{query_field[1].strip()}": \n {list_}')
                        # break

        elif query_field[0] == "exit":
            print('Good bye')
            break


if __name__ == "__main__":
    main()