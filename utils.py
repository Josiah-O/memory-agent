import json

def mock_api_call(query):
    # This is a mock function to simulate an API call
    # Replace this with actual API call in the future
    result = {
        "product_name": "Dell XPS 13",
        "price": "$950",
        "RAM": "16GB",
        "Rating": "4.5 stars"
    }
    return json.dumps(result)  # Convert to JSON string
