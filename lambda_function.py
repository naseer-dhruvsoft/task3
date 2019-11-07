import json
import object_count as oc
import boto3
from smart_open import open

def lambda_handler(event, context):
    # TODO implement
    a = oc.count_of_objects()
    print(a)
    # with open("s3://task3bucket/google_logo.json", 'w') as f:
    with open("s3://task3bucket/solar_system.json", 'w') as f:
        data = json.dump(a, f)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }