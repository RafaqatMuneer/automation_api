from flask import Blueprint,request
from utils.response import success_response,error_response
from utils.file_handler import validate_file,get_file_extension, save_file

uploads_bp = Blueprint('uploads',__name__)

@uploads_bp.route('/file', methods = ['POST'])
def upload_file():
    """Accept a file upload, validate it, save it and return metadata"""
    # Step 1: Validate
    is_valid, error_message, file = validate_file(request)

    if not is_valid:
        return error_response(
            message=error_message,
            status_code=400
        )
    # Step 2: save file
    saved_name, saved_path = save_file(file)

    #Step 3: Build metadata for response
    file_content = file.read()
    metadata = {
        "filename" : saved_name,
        "size_bytes" : len(file_content),
        'extension' : get_file_extension(saved_name),
        "saved_path" : saved_path
    }

    return success_response(
        data = metadata,
        message= "File uploaded successfuly",
        status_code = 201
    )
