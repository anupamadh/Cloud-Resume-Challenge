import boto3
import json


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCountTable-new')


def lambda_handler(event, context):
    response = table.get_item(
            Key = {
                'id': '1',
            }
        )
    views = response['Item']['views']
    views = views + 1
    print(views)
    response = table.put_item(Item={
        'id':'1',
        'views':views
    })
    return views