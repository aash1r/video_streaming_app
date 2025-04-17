import boto3, json
from config import Config


config = Config()

sqs_client = boto3.client("sqs",region_name= config.REGION_NAME)
queue_url = config.QUEUE_URL
def poll_sqs():
    
    while True:
        response = sqs_client.receive_message(
            QueueUrl = queue_url,
            MaxNumberOfMessages = 10,
            WaitTimeSeconds = 20,
        )

        for message in response.get("Messages",[]):
            message_body = json.loads(message["Body"])

            if ("Service" in message_body and "Event" in message_body and message_body.get("Event") == "s3:TestEvent"):
                sqs_client.delete_message(QueueUrl = queue_url, ReceiptHandle = message["ReceiptHandle"])
                continue
            
            if "Records" in message_body:
                s3_record = message_body["Records"][0]["s3"]
                bucket_name = s3_record["bucket"]["name"]
                object_key = s3_record["object"]["key"]            

poll_sqs()