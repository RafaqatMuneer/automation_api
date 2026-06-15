import os

class Config:
    APP_NAME = "AutomatePK API"
    VERSION = "1.0.0"
    DEBUG = True

    #File Upload setting
    UPLOAD_FOLDER = "uploads"
    MAX_FILE_SIZE = 2 * 1024 * 1024 # 2MB — math, not magic number
    ALLOWED_EXTENSIONS = {"csv","json"}
