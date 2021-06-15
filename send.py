#!/usr/bin/env python
import pika
credentials = pika.PlainCredentials('basic', 'basic')
connection = pika.BlockingConnection(pika.ConnectionParameters('test.web.bluehairfreak.com', 5672, "/", credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()

