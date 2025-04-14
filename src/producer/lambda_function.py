import json
import boto3
import os

URL_QUEUE = os.environ.get("URL_QUEUE")
#QUEUE_NAME = os.environ.get("QUEUE_NAME")

def lambda_handler(event, context):
    client_sqs = boto3.client('sqs')
    #queue = client_sqs.get_queue_url(QueueName=QUEUE_NAME)
    entries = []
    for num in range(10):
        entry ={
            "Id": str(num),
            "MessageBody": "message %s" % str(num)
        }
        entries.append(entry)
    msg = client_sqs.send_message_batch(QueueUrl=URL_QUEUE, Entries=entries)
    return {
        "statusCode":"200",
        "headers":{
            "Content-Type":"application/json"
        },
        "body": json.dumps({
            "msg": msg,
            "status": "enviadas"
        })
    }