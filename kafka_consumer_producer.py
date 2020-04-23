import threading
import logging
import time
import json
from kafka import KafkaConsumer, KafkaProducer

class Producer(threading.Thread):
    daemon = True
    def run(self):
        producer = KafkaProducer(bootstrap_servers='targethost:9092',
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))

        while True:
            producer.send('custommon', {"dataObjectID": "MCulug_test1"})    #These two lines are sending data to topic name "custommon" to target hosts 9092 port
            producer.send('custommon', {"dataObjectID": "MCulug_test12"})
            time.sleep(10)
class Consumer(threading.Thread):
    daemon = True

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers='targethost:9092',        #Here is where we define consumer which listens on 9092 port
                                 auto_offset_reset='earliest',
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')))
        consumer.subscribe(['custommon'])

        for message in consumer:
            print (message)

def main():
    threads = [
        Producer(),                                                           #enable or disable producer and consumer components
        Consumer()
    ]

    for t in threads:
        t.start()
    time.sleep(10)

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:' +                 #We can disable logging for performance purposes
               '%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO                                                    #logging level is currently at info
    )
    main()
