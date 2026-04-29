# app/consumer.py
import json
import threading
import time
from confluent_kafka import Consumer
from app.config import KAFKA_BOOTSTRAP_SERVERS, TOPIC_ORDERS
from app.models import Order


def process_order(order_data: dict):
    """Process a single order"""
    try:
        order = Order(**order_data)
        tax = order.calculate_tax()

        print(f"✅ PROCESSED Order {order.order_id}")
        print(f"   User: {order.user_id} | Total: ${order.total_amount} | Tax: ${tax}")
        print(f"   Status → 'processed'\n")

        # Future: Save to database, send email, update inventory, etc.
    except Exception as e:
        print(f"❌ Failed to process order: {e}")


def consume_orders():
    """Kafka Consumer running in background thread"""
    consumer = Consumer({
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
        'group.id': 'order-processors-v2',
        'auto.offset.reset': 'earliest',
        'enable.auto.commit': True,
    })

    consumer.subscribe([TOPIC_ORDERS])
    print("🔄 Kafka Consumer Started - Listening for new orders...\n")

    try:
        while True:
            msg = consumer.poll(1.0)  # 1 second timeout

            if msg is None:
                continue
            if msg.error():
                print(f"Consumer Error: {msg.error()}")
                continue

            # Decode and process message
            order_data = json.loads(msg.value().decode('utf-8'))
            process_order(order_data)

    except KeyboardInterrupt:
        print("Consumer stopped by user")
    except Exception as e:
        print(f"Unexpected consumer error: {e}")
    finally:
        consumer.close()
        print("Consumer closed.")


def start_background_consumer():
    """Start consumer in a daemon thread"""
    thread = threading.Thread(target=consume_orders, daemon=True, name="KafkaConsumer")
    thread.start()
    return thread