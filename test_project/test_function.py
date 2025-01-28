import json

def lambda_handler(event, context):
    # TODO Implement Logic
    variable = "this is a test 5. there shouldnt not be _dev attached to the file"
    return {{
        
        'statusCode': 200,
        'body': json.dumps('Create new lambda function')
    }}
