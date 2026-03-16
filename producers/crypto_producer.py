import json
import yaml
from kafka import KafkaProducer
from utils.helpers import fetch_crypto_price, wait

# Load Kafka config
with open('config/kafka_config.yaml') as f:
    config = yaml.safe_load(f)

producer = KafkaProducer(
    bootstrap_servers=config['kafka_broker'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

if __name__ == "__main__":
    print("Starting Kafka producer...")
    while True:
        data = fetch_crypto_price()
        if data:
            producer.send(config['topic'], value=data)
            print(f"Sent: {data}")
        wait(5)