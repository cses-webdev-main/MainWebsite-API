import json

# import requests


def lambda_handler(event, context):
    """
    Parameters
    ----------
    event: dict, required (Input)
    context: object, required (Runtime attributes)

    Returns
    ------
    dict
    """

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
