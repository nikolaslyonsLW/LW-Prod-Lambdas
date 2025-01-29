import json

def lambda_handler(event, context):
    # TODO Implement Logic
    variable = "trevor is cool in this new function"
    return {{
        'statusCode': 200,
        'body': json.dumps('Create new lambda function')
    }}
