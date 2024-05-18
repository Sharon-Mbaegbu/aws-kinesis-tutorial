import json
import boto3
import time

# Specify your Kinesis stream name
stream_name = 'amazon-books'

# Create a Kinesis client
kinesis_client = boto3.client('kinesis')

# Read the JSON file
with open('amazon_books200.json', 'r') as file:
    data = json.load(file)

# Measure the start time
start_time = time.time()

# Put each record into the Kinesis stream
for record in data:
    # Convert the record to JSON string
    record_data = json.dumps(record)

    # Use the "Title" field as the partition key
    partition_key = record.get('Title', 'default_partition_key')

    # Put record into the Kinesis stream
    response = kinesis_client.put_record(
        StreamName=stream_name,
        Data=record_data,
        PartitionKey=partition_key
    )

    # Print the response (optional)
    print(response)

# Measure the end time
end_time = time.time()

# Calculate the total time taken
total_time = end_time - start_time
print(f"Total time taken: {total_time} seconds")

