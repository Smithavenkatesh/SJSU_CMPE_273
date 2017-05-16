import boto3
import json



def lambda_handler(event, context):
    # Your code goes here!
    client = boto3.client("dynamodb")

    try:
       print(event["order_id"])
       table = boto3.resource('dynamodb', region_name='us-west-1').Table('order')
       item = table.get_item(Key={'order_id': event['order_id']}).get('Item')

    except Exception, e:
        return 400, e
    else:
        print(item)
        return item
