import boto3
import json
from datetime import datetime

def convertListToString(list):
    count = 1
    string = ""
    for item in list:
        string = string + str(count) + ":" + item + " "
        count = count + 1
    return string


def lambda_handler(event, context):

    client = boto3.resource('dynamodb', region_name='us-west-1').Table('order')
    try:
        dborder = client.get_item(Key={'order_id': event['order_id']}).get('Item').get('order')
        selection = dborder["selection"]
        size = dborder["size"]
        input = int(event["input"])
        response = {}
        if(selection == "none"):
            menuID = client.get_item(Key={'order_id': event['order_id']}).get('Item').get('pizzaid')
            menu = boto3.resource('dynamodb', region_name='us-west-1').Table('Menu')
            selectionname = menu.get_item(Key={'pizzaid': menuID}).get('Item').get('selection')
            sizename = menu.get_item(Key={'pizzaid': menuID}).get('Item').get('size')
            order = {}
            order["selection"] = selectionname[input-1]
            order["size"] = "none"
            order["costs"] = "none"
            order["order_time"] = "none"
            response['Message'] =  "Which size do you want? %s" % convertListToString(sizename)

        elif(size=="none"):
            print "here"
            
            menuID = client.get_item(Key={'order_id': event['order_id']}).get('Item').get('pizzaid')
            menu = boto3.resource('dynamodb', region_name='us-west-1').Table('Menu')
            sizename = menu.get_item(Key={'pizzaid': menuID}).get('Item').get('size')
            price = menu.get_item(Key={'pizzaid': menuID}).get('Item').get('price')
            

            order = {}
            order["selection"] = selection
            order["size"] = sizename[input-1]
            order["costs"] = price[input-1]
            order["order_time"] = str(datetime.now())
            response['Message'] = "Your order costs $%s. We will email you when the order is ready. Thank you!" % order["costs"]


        else:
            return "order already complete and is in progress"

        client.update_item(
            Key={'order_id': event['order_id']},
            UpdateExpression="SET #order = :a",
            ExpressionAttributeNames={'#order': 'order'},
            ExpressionAttributeValues={':a': order})

        return response
    except Exception, e:
        return 400, e
