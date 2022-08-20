import os
import json
import datetime
import boto3


def create_url(event, context):
    s3 = boto3.client("s3")
    url = json.loads(event['body'])['url']
    id = os.urandom(10).hex()

    s3.put_object(Bucket='short-url-feed', Key=f'm/{id}', WebsiteRedirectLocation=url)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'id': id
        })
    }
