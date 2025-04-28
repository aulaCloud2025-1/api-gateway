import boto3
import logging
import json

dynamodb = boto3.resource('dynamodb')
table= dynamodb.Table('table_contas')

def get_function(user):
    table.

def lambda_handler(event, context):
    response = get_function(event['body']['user'])
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
