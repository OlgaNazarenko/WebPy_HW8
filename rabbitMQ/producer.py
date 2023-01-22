import sys

from mongoengine import connect
import pika
import faker

from models import Contacts

connect(host="mongodb+srv://goitlearn:Seoul@cluster0.aksl02l.mongodb.net/?retryWrites=true&w=majority")

fake = faker.Faker()


def create_data():
    for _ in range(8):
        data = Contacts(
            fullname=fake.name(),
            email=fake.email(),
        )
        data.save()


def main():

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672))
    channel = connection.channel()

    channel.exchange_declare(exchange='email', exchange_type='direct')

    channel.queue_declare(queue='email-out', durable=True)
    channel.queue_bind(exchange='email', queue='email-out')

    contacts = Contacts.objects().limit(8)

    for contact in contacts:
        message = ' '.join(sys.argv[1:]) or "info: Best luck in the Year of The Rabbit!"

        channel.basic_publish(exchange = '',
                              routing_key = 'email-out',
                              body = f'{contact.id}'.encode()
                              )
        contact.update(status=True)
        print(f" [x] Sent email to ObjectID:{contact.id} : {message}")

    connection.close()


if __name__ == '__main__':
    create_data()
    main()
