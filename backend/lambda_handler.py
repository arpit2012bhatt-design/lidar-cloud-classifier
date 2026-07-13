import json
import boto3
from datetime import datetime

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        print(f"[PROCESSOR] File: {key}")
        print(f"[PROCESSOR] Processing...")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Processing successful',
                'file': key
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
