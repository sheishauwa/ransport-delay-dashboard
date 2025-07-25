import json
import boto3
import datetime

s3 = boto3.client('s3')
bucket = "my-transport-delay-lambda-bucket"  # ✅ Use your actual bucket name

def lambda_handler(event, context):
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")
    filename = f"processed/delay-{now}.json"

    delay_event = {
        "route_id": "M12",
        "location": "Broadway & 42nd",
        "delay_minutes": 12,
        "timestamp": now
    }

    s3.put_object(
        Bucket=bucket,
        Key=filename,
        Body=json.dumps(delay_event)
    )

    return {
        'statusCode': 200,
        'body': f'Data saved to {filename}'
    }
