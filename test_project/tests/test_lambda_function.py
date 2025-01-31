import json
import pytest
from test_project_dev.test_function import lambda_handler

# Mock AWS Lambda event and context
@pytest.fixture
def mock_event():
    return {
        "key1": "value1",
        "key2": "value2"
    }

@pytest.fixture
def mock_context():
    class Context:
        def __init__(self):
            self.function_name = "test_lambda"
            self.memory_limit_in_mb = 128
            self.invoked_function_arn = "arn:aws:lambda:us-east-1:123456789012:function:test_lambda"
    return Context()

# Test the Lambda function
def test_lambda_handler(mock_event, mock_context):
    response = lambda_handler(mock_event, mock_context)
    
    assert response["statusCode"] == 200
    assert json.loads(response["body"]) == "Create new lambda function"