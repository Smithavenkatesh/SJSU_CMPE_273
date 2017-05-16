import boto3
import json
from datetime import datetime

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def convert12_to_24time(in_time):
    
    in_time = datetime.strptime(in_time, "%I%p")
    out_time = datetime.strftime(in_time, "%H,%M,%S")
    return out_time

def convertListToString(list):
    count = 1
    string = ""
    for item in list:
        string = string + str(count) + ":" + item + " "
        count = count + 1
    return string


def lambda_handler(event, context):
    
        client = boto3.resource('dynamodb', region_name='us-west-1').Table('order')
        myevent = {}
        try:
            myevent["pizzaid"] = event["menu_id"]
            myevent["order_id"] = event["order_id"]
            myevent["customer_name"] = event["customer_name"]
            myevent["customer_email"] = event["customer_email"]
            myevent["order_status"] = "processing"
            order = {}
            order["selection"] = "none"
            order["size"] = "none"
            order["costs"] = "none"
            order["order_time"] = "none"
            myevent["order"] = order
            
            currDay = datetime.now().strftime('%a')
            menuclient = boto3.resource('dynamodb', region_name='us-west-1').Table('Menu')
            storeTime = menuclient.get_item(Key={'pizzaid': event['menu_id']}).get('Item').get('store_hours')
            storeTime = storeTime[currDay]
            starttime=storeTime.split("-")[0]
            endtime=storeTime.split("-")[1]
            start24 = convert12_to_24time(starttime)
            end24 = convert12_to_24time(endtime)
            currtime = datetime.strftime(datetime.now(),"%H,%M,%S")
            
            
            if(time_in_range(start24, end24, currtime)):
            
                print ("in store range")
                client.put_item(Item=myevent)
                menuclient = boto3.resource('dynamodb', region_name='us-west-1').Table('Menu')
                selection = menuclient.get_item(Key={'pizzaid': event['menu_id']}).get('Item').get('selection')
                return "200 OK { Hi %s , please choose one of these selection: %s }" % (myevent["customer_name"], convertListToString(selection))
            
            else:
                return "Store is closed at this time. Sorry we cannot take orders"
        except Exception, e:
            return 400, e
