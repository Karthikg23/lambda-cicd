import json

def lambda_handler(event, context):
    """
    A simple AWS Lambda function that returns a success message.
    """
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from AWS Lambda deployed via CodePipeline!"
        })
    }
    return response
