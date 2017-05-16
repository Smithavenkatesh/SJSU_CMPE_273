from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError



def handler(event, context):
    # Your code goes here!
    client = boto3.client("dynamodb")
    print("event: ")
    print(event['pizzaid'])

    try:
       table = boto3.resource('dynamodb', region_name='us-west-1').Table('Menu')
       item = table.get_item(Key={'pizzaid': event['pizzaid']}).get('Item')

    except Exception, e:
        return 400, e
    else:
        print(item)
        return item
