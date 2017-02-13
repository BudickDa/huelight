from __future__ import print_function
import logging
import boto3
from datetime import *
from boto3.dynamodb.conditions import Key, Attr

# enable basic logging to CloudWatch Logs
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# setup the DynamoDB table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('feedback')

def lambda_handler(event, context):
    table.put_item(
        Item={
            'userId': '1',
            'feedback': event['feedback']
        }
    )
    return("Success!")
