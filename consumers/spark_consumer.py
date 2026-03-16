from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, FloatType
import yaml

# Load Snowflake config
with open('config/snowflake_config.yaml') as f:
    sf_config = yaml.safe_load(f)

# Spark session
spark = SparkSession.builder \
    .appName("CryptoStreamConsumer") \
    .getOrCreate()

# Kafka stream
kafka_df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "crypto_data") \
    .option("startingOffsets", "latest") \
    .load()

# Define schema
schema = StructType([
    StructField("bitcoin", StructType([StructField("usd", FloatType())])),
    StructField("ethereum", StructType([StructField("usd", FloatType())]))
])

# Parse JSON
json_df = kafka_df.selectExpr("CAST(value AS STRING) as json") \
    .select(from_json(col("json"), schema).alias("data"))

# Extract BTC and ETH prices
price_df = json_df.select(
    col("data.bitcoin.usd").alias("btc_usd"),
    col("data.ethereum.usd").alias("eth_usd")
)

# Write to Snowflake
price_df.writeStream \
    .format("snowflake") \
    .option("sfURL", sf_config['account']) \
    .option("sfDatabase", sf_config['database']) \
    .option("sfSchema", sf_config['schema']) \
    .option("sfWarehouse", sf_config['warehouse']) \
    .option("dbtable", sf_config['table']) \
    .option("user", sf_config['user']) \
    .option("password", sf_config['password']) \
    .option("checkpointLocation", "/tmp/checkpoint") \
    .start() \
    .awaitTermination()