import json
import boto3
import os


table_name = 'Pinpoint_Campaign'
#region = os.environ['AWS_REGION']
region = 'us-west-2'
dynamodb = boto3.resource('dynamodb')

def put_item(item):
    table = dynamodb.Table(table_name)
    response = table.put_item(
        Item = item
    )

    return response



