from flask import jsonify
from datetime import datetime, timezone

def success_response(data = None,message = "Success",status_code= 200):
    """
    Standard success response envelope.
    Always returns the same structure on success.
    """
    response = {
        "status" : "success",
        "message" : message,
        "data" : data,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    return jsonify(response), status_code
    # return response, status_code

def error_response(message = "Something went wrong",status_code= 400):
    """
     Standard error response envelope.
    Always returns the same structure on failure
    """
    response = {
        "status" : "error",
        "message" : message,
        "data" : None,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    return jsonify(response), status_code
    # return response, status_code

# if __name__ == "__main__":
#     print(success_response({"name": "Ali"}))
#     print(error_response("Invalid file"))