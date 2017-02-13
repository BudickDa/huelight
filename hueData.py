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
table = dynamodb.Table('airdata')
feedbackTable = dynamodb.Table('feedback')

# setup conversion to epoch
epoch = datetime.utcfromtimestamp(0)

def lambda_handler(event, context):
    
    feedback = feedbackTable.query(KeyConditionExpression=Key('userId').eq('1'))
    offset = 0
    
    for i in feedback['Items']:
        offset += i['feedback']

    response = table.query(
        KeyConditionExpression=Key('event_name').eq('temperature'),
        Limit=1,
        ScanIndexForward=False
    )
    data = response["Items"][0]
    temperature = data["data"] + offset
    
    
    red = -15 + temperature/20*255 % 255
    blue = 270 - temperature/20*255 % 255
    return({
        "temperature": temperature,
        "color": '#%02x%02x%02x' % (red, 0, blue)
    })
