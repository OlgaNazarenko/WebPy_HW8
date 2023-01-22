import os
import sys
import json

import pika
import time


def main():
    messages_received = 0
    messages_limit = 8

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='email-out', durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        nonlocal messages_received
        if messages_received >= messages_limit:
            ch.stop_consuming()
            return

        message = json.dumps(body.decode())
        print(f" [x] Received email: {message}")
        ch.basic_ack(delivery_tag=method.delivery_tag)

        messages_received += 1

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='email-out', on_message_callback=callback, auto_ack=False)

    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
