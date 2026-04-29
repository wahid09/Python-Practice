# app/producer.py
import json
from datetime import datetime
from uuid import UUID
from confluent_kafka import Producer
from app.config import KAFKA_BOOTSTRAP_SERVERS, TOPIC_ORDERS
from app.models import Order

# Custom JSON encoder to handle UUID and datetime
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        elif isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


producer = Producer({
    'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
    'client.id': 'ecommerce-producer'
})


def produce_order(order: Order):
    def delivery_callback(err, msg):
        if err is not None:
            print(f"❌ Delivery failed for order {order.order_id}: {err}")
        else:
            print(f"✅ Order sent successfully → {order.order_id} | Partition: {msg.partition()}")

    # Convert Pydantic model to dict
    order_dict = order.dict() if hasattr(order, 'dict') else dict(order)

    try:
        # Use custom encoder to handle UUID and datetime
        value_bytes = json.dumps(order_dict, cls=CustomJSONEncoder).encode('utf-8')
    except Exception as e:
        print(f"❌ JSON serialization error: {e}")
        return

    producer.produce(
        topic=TOPIC_ORDERS,
        key=str(order.user_id).encode('utf-8'),
        value=value_bytes,
        callback=delivery_callback
    )
    producer.poll(0)   # Trigger delivery callback