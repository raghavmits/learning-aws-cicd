def handler(event, context):
    response_body = {
        "message": "Na kisi ka thikana!",
        "version": "1.0.0"

    }
    return {"statusCode": 200, "body": response_body }

