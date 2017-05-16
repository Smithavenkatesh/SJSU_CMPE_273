import boto3

def lambda_handler(event, context):
    # Your code goes here!
    try:
        table = boto3.resource("dynamodb").Table("Menu")
        menu_id = {"pizzaid": event["pizzaid"]}
        key = event["update"].keys()[0]
        value = event["update"][key]
        table.update_item(Key=menu_id, UpdateExpression="SET #key = :val",ExpressionAttributeNames={"#key":key}, ExpressionAttributeValues={ ":val" :value})
        return "Item with", menu_id,"updated succesfully"
    except Exception as e:
        return e.message
