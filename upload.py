import json
import boto3

stream_name = 'amazon-books'
kinesis_client = boto3.client('kinesis')

title_to_check= "  Python for Data Science For Dummies "

def process_records(records):

  total_books = 0
  total_price = 0.0

  for record in records['Records']:
    
    record_data = json.loads(record['Data'].decode('utf-8'))

    if record_data.get('Title') == title_to_check:
      print(f"Found book: {title_to_check}")
      print(record_data)

    total_books += 1        
    total_price += record_data.get('Price', 0.0)

  average_price = total_price / total_books if total_books > 0 else 0.0

  print(f"Total books: {total_books}")
  print(f"Average price: ${average_price:.2f}")
  

try:
  shard_iterator = kinesis_client.get_shard_iterator(
    StreamName=stream_name,
    ShardId='shardId-000000000000',  
    ShardIteratorType='TRIM_HORIZON')['ShardIterator']
except kinesis_client.exceptions.KinesisException as err:
  print("Error getting shard iterator:", err)
  
records = kinesis_client.get_records(ShardIterator=shard_iterator, Limit=100)

while 'NextShardIterator' in records:

  if 'Records' in records and records['Records']:
    process_records(records)

  shard_iterator = records['NextShardIterator']

  try:
    records = kinesis_client.get_records(
      ShardIterator=shard_iterator, Limit=100)
  except kinesis_client.exceptions.KinesisException as err:  
    print("Error getting records:", err)
    
if 'Records' in records and records['Records']:      
  process_records(records)
  
kinesis_client.close(shard_iterator)
