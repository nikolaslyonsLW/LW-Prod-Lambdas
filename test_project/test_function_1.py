import json

def lambda_handler(event, context):
    # TODO Implement Logic
    variable = "lets see if this gets added "
    return {{
        
        'statusCode': 200,
        'body': json.dumps('Create new lambda function')
    }}
