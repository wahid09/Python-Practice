import json
import time
from uuid import uuid4
from confluent_kafka import Producer
from datetime import datetime

# Configuration
conf = {
    'bootstrap.servers': 'localhost:9092',  # Change for cloud setups
    'client.id': 'ecommerce-producer'
}

producer = Producer(conf)


def delivery_callback(err, msg):
    """Callback for delivery reports."""
    if err is not None:
        print(f"Delivery failed for message: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")


def produce_order():
    order = {
        "order_id": str(uuid4()),
        "user_id": f"user_{int(time.time()) % 1000}",
        "items": [
            {"product": "Laptop", "quantity": 1, "price": 999.99},
            {"product": "Mouse", "quantity": 2, "price": 29.99}
        ],
        "total_amount": 1059.97,
        "timestamp": datetime.utcnow().isoformat(),
        "status": "pending"
    }

    # Produce message (key for partitioning, value as JSON bytes)
    producer.produce(
        topic='orders',
        key=order["user_id"].encode('utf-8'),  # Optional: for ordering per user
        value=json.dumps(order).encode('utf-8'),
        callback=delivery_callback
    )

    # Poll to trigger delivery callbacks
    producer.poll(0)


if __name__ == "__main__":
    print("Starting Order Producer... Press Ctrl+C to stop.")
    try:
        for i in range(20):  # Produce 20 sample orders
            produce_order()
            time.sleep(1)  # Simulate real-time orders
    except KeyboardInterrupt:
        pass
    finally:
        producer.flush()  # Ensure all messages are sent
        print("Producer shut down.")