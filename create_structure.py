from pathlib import Path

# Root project folder
project_name = "day02_file_upload/"

# Files to create
files = [
    "app.py",
    "config.py",
    "requirements.txt",
    "utils/__init__.py",
    "utils/response.py",
    "utils/file_handler.py",
    "routes/__init__.py",
    "routes/products.py",
    "routes/health.py",
    "routes/uploads.py",
    "uploads/.gitkeep"
]

# Create project structure
for file in files:
    file_path = Path(project_name) / file

    # Create parent directories if they don't exist
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Create empty file
    file_path.touch(exist_ok=True)

print(f"Project structure '{project_name}' created successfully!")