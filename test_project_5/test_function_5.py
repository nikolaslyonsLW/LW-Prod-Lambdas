import json

def lambda_handler(event, context):
    # TODO Implement Logic
    variable = "this is cool"
    variable2 = "kim"
    return {{
        'statusCode': 200,
        'body': json.dumps('Create new lambda function')
    }}
