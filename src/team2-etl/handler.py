import boto3
import csv
import sys
sys.path.append("..") # Goes back a level in the directory
from src.app import start_transformation


def handle(event, context):
    # Get key and bucket informaition
    key = event['Records'][0]['s3']['object']['key']
    bucket = event['Records'][0]['s3']['bucket']['name']

    # use boto3 library to get object from S3
    s3 = boto3.client('s3')
    s3_object = s3.get_object(Bucket=bucket, Key=key)
    file_data = s3_object['Body'].read().decode('utf-8')

    # read CSV
    field_names = ['date_time', 'location', 'customer_name', 'products', 'payment_method', 'total', 'card_details']
    csv_data = csv.DictReader(file_data, fieldnames = field_names)
    data = []
    for line in csv_data:
        data.append(dict(line))

    start_transformation(data)
    print("we're in")

    return {"message": "success!!! Check the cloudwatch logs for this lambda in cloudwatch https://eu-west-1.console.aws.amazon.com/cloudwatch/home?region=eu-west-1#logsV2:log-groups"}

