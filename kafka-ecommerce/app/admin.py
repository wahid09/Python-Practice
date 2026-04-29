# app/admin.py
from confluent_kafka.admin import AdminClient, NewTopic
from app.config import KAFKA_BOOTSTRAP_SERVERS, TOPIC_ORDERS

def create_topic_if_not_exists():
    admin_client = AdminClient({'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS})

    topic = NewTopic(
        topic=TOPIC_ORDERS,
        num_partitions=3,
        replication_factor=1
    )

    fs = admin_client.create_topics([topic])

    for topic, f in fs.items():
        try:
            f.result()        # Wait for operation to finish
            print(f"✅ Topic '{topic}' created successfully")
        except Exception as e:
            if "already exists" in str(e).lower():
                print(f"ℹ️  Topic '{topic}' already exists")
            else:
                print(f"⚠️  Failed to create topic '{topic}': {e}")