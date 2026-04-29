import json
from confluent_kafka import Consumer, KafkaError

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'order-processors',  # Consumer group for load balancing
    'auto.offset.reset': 'earliest',  # Start from beginning if no offset
    'enable.auto.commit': True  # Auto-commit offsets (or manual for exactly-once)
}

consumer = Consumer(conf)
consumer.subscribe(['orders'])

print("Starting Order Processor Consumer...")

try:
    while True:
        msg = consumer.poll(1.0)  # Poll every 1 second

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(f"Error: {msg.error()}")
                continue

        # Process the message
        order = json.loads(msg.value().decode('utf-8'))
        print(f"Received order: {order['order_id']} for user {order['user_id']}")

        # Simulate processing (e.g., validate, calculate tax, enrich)
        processed_order = order.copy()
        processed_order['status'] = 'processed'
        processed_order['tax'] = round(order['total_amount'] * 0.1, 2)

        print(
            f"Processed: {processed_order['order_id']} | Total with tax: {processed_order['total_amount'] + processed_order['tax']}")

        # Could produce to another topic here: 'processed-orders'

except KeyboardInterrupt:
    print("Shutting down consumer...")
finally:
    consumer.close()