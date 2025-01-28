import json

def lambda_handler(event, context):
    # TODO Implement Logic
    variable = "this is for sarah"
    VARIABLE = 'HELLO'
    return {{
        'statusCode': 200,
        'body': json.dumps('Create new lambda function')
    }}
