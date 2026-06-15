import os
from werkzeug.utils import secure_filename
from config import Config

def get_file_extension(filename):
    """
    Extract extension from file name
    split the name and extension from right side
    'products.csv' -> 'csv'
    'no extension' -> '' 
    """
    return filename.rsplit('.',1)[-1].lower() if '.' in filename else ''

def is_allowed_extension(filename):
    """Check if file extension is in the allowed set."""
    return get_file_extension(filename) in Config.ALLOWED_EXTENSIONS

def validate_file(request):
    """
    validation checks
    1. File key exist in request
    2. Filename is not empty
    3. File extension is allowed
    4. File have some content
    5. File size is within allowed limit
    """
    # 1. File key exist in request
    if 'file' not in request.files:
        return False, "No file found in the request", None
    
    file = request.files['file']
    # 2. Filename is not empty
    if file.filename == '':
        return False, "No file selected", None
    # 3. File extension is allowed
    if not is_allowed_extension(file.filename):
        allowed = ", ".join(Config.ALLOWED_EXTENSIONS)
        return False,f"File type is not allowed. Allowed Types: {allowed}", None
    file_content = file.read()
    print(f"DEBUG: File size is {len(file_content)} bytes") # Check the size here!
    # 4. File have some content
    #need to remove white spaces, newlines, or empty JSON braces
    cleaned_content = file_content.strip()
    if len(cleaned_content) == 0 or cleaned_content == b'{}':
        return False,"File is empty", None
    # 5. File size is within allowed limit
    if len(file_content) > Config.MAX_FILE_SIZE:
        max_mb = Config.MAX_FILE_SIZE / (1024 * 1024)
        return False, f"File too large, Max allowed size is {max_mb : .0f}MB ", None
    # Reset file pointer to the start of file after reading
    file.seek(0)
    return True,None,file
def save_file(file):
    """
    - save validated file to upload folder
    - return saved file name and full path
    """
    # Secure_filname skip dangerous characters (path attack)
    safe_name = secure_filename(file.filename)
    save_path = os.path.join(Config.UPLOAD_FOLDER, safe_name)
    file.save(save_path)
    return safe_name, save_path
    

