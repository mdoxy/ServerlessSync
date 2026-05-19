import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('file-metadata')

def lambda_handler(event, context):

    record = event['Records'][0]

    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']

    file_id = key.split("_")[0]

    table.put_item(
        Item={
            "file_id": file_id,
            "s3_key": key,
            "status": "processed"
        }
    )

    print(f"Stored metadata for {file_id}")

    return {
        'statusCode': 200,
        'body': json.dumps("Success")
    }
