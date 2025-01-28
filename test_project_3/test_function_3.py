import json

def lambda_handler(event, context):
    # TODO Implement Logic
    variable = "trevor is cool"
    return {{
        'statusCode': 200,
        'body': json.dumps('Create new lambda function')
    }}
