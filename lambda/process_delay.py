import json
import boto3
import datetime
import random

# Initialize S3 client
s3 = boto3.client('s3')

# Your target S3 bucket name
bucket = "transport-delay-data-bucket"

# Sample data pools
routes = ["M12", "B25", "Q50", "T7"]
locations = ["Broadway & 42nd", "Lexington & 59th", "Harlem 125th", "Wall Street"]

def lambda_handler(event, context):
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")
    filename = f"processed/delay-{now}.json"

    # Simulate 10 delay records
    delay_events = []

    for _ in range(10):
        delay_events.append({
            "route_id": random.choice(routes),
            "location": random.choice(locations),
            "delay_minutes": random.randint(0, 30),
            "timestamp": datetime.datetime.utcnow().isoformat()
        })

    # Convert list of JSON to newline-delimited JSON string
    body = "\n".join([json.dumps(event) for event in delay_events])

    # Upload to S3
    s3.put_object(
        Bucket=bucket,
        Key=filename,
        Body=body
    )

    return {
        'statusCode': 200,
        'body': f'{len(delay_events)} records saved to s3://{bucket}/{filename}'
    }
