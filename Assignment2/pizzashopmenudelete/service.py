import boto3
from botocore.exceptions import ClientError

def handler(event, context):
  try:
    table = boto3.resource('dynamodb', region_name='us-west-1').Table('Menu')
    table.delete_item(
      Key={'pizzaid': event['pizzaid']})
    return 200,"OK"
  except Exception as e:
    return e.message
