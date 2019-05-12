import pika

#connect/channel
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


print(channel)