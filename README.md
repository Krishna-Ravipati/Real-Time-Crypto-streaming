# Real-Time Crypto Data Streaming Platform

**Technologies:** Apache Kafka, Apache Spark, Snowflake, Grafana, Python  

## Overview
This project implements a real-time cryptocurrency data streaming pipeline:
- Fetch live crypto data from APIs.
- Stream via Kafka.
- Process with Spark Structured Streaming.
- Store in Snowflake.
- Visualize with Grafana dashboards.

## Features
- High-throughput Kafka producers and consumers.
- Real-time processing of price trends and metrics.
- Historical data storage in Snowflake.
- Interactive Grafana dashboards.

## Setup Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt