# AWS Kinesis Tutorial Project

## Table of Contents
- [Introduction](#introduction)
- [Objective](#objective)
- [Methodology](#methodology)
- [Results](#results)
- [Conclusion](#conclusion)
- [Files](#files)
- [References](#references)

## Introduction
This project focuses on mastering Amazon Kinesis Data Streams, a core component of AWS designed for real-time data handling. By converting CSV data into JSON and utilizing AWS CLI for stream processing, we explored the practical applications of Amazon Kinesis and evaluated its performance and scalability.

## Objective
The primary goal of this project was to conduct a comprehensive evaluation of Amazon Kinesis Data Streams. This included:
- Setting up AWS CLI for direct interaction with AWS services.
- Preparing and converting datasets into JSON format.
- Streaming data using the `put_record` and `get_record` APIs.
- Processing data in real-time.
- Evaluating the performance of Kinesis under various data loads.

## Methodology
The project was executed through the following steps:
1. **Setup AWS CLI:** Initiated the command line interface for direct interaction with AWS services.
2. **Prepare JSON Datasets:** Converted CSV data into JSON format for compatibility with Kinesis.
3. **Stream Data Using APIs:** Utilized the `put_record` and `get_record` APIs for seamless data streaming.
4. **Process Data:** Engaged in real-time data processing, emphasizing efficiency and speed.
5. **Performance Evaluation:** Tested and documented Kinesis performance across various data loads.

### Scripts
- **make_data.py:** Converts CSV data into JSON format.
- **main.py:** Uploads JSON data to the Kinesis stream.
- **process.py:** Processes and queries data from the Kinesis stream.

## Results
The performance evaluation demonstrated Amazon Kinesis's capability in managing real-time data workflows. Key findings include:
- Kinesis processed 212 records in approximately 10.36 seconds using a single shard.
- With an increased load of 8786 records, the system processed the data in 276.68 seconds using two shards.
- These results indicate Kinesis's scalability and operational efficiency, making it a robust choice for large-scale data streaming.

## Conclusion
The project successfully showcased the strengths of Amazon Kinesis in handling large data volumes and real-time data processing. Kinesis proved to be a scalable, efficient, and cost-effective solution for data streaming within cloud-based infrastructures.

## Files
- **make_data.py:** Script to convert CSV data to JSON.
- **main.py:** Script to upload JSON data to Kinesis.
- **process.py:** Script to process and query data from Kinesis.
- **amazon_books200.json:** JSON dataset used in the project.

## References
- [Amazon Kinesis Documentation](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html)
- Buick, B. (2023). An in-depth look at Amazon Kinesis and a comparison to Apache Kafka.
- Johnson, E. (2019). Increasing real-time stream processing performance with Amazon Kinesis Data Streams.
- Mentzer, A. (2016). Joining and enriching streaming data on Amazon Kinesis.
- Narayanan, R. (2022). Kafka vs. Kinesis: A Deep Dive Comparison.
- Odmark, J. (2023). Unveiling the limitations of Amazon Kinesis: A comprehensive technical analysis.
