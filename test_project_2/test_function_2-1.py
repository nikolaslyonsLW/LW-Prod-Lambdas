import json

def lambda_handler(event, context):
    # TODO Implement Logic
    varible_2 = "this is another test to make sure its workking we will see"
    return {{
        'statusCode': 200,
        'body': json.dumps('Create new lambda function')
    }}
