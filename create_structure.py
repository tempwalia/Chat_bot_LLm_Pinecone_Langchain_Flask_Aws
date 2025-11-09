import os

# Create directories
directories = ['src', 'analysis']
for directory in directories:
    os.makedirs(directory, exist_ok=True)
    print(f"Created directory: {directory}")

# Create files
files = [
    'src/__init__.py',
    'src/helper.py',
    'src/prompt.py',
    '.env',
    'setup.py',
    'README.md',
    'app.py',
    'analysis/trials.ipynb',
    'requirements.txt'
]

for file in files:
    # Create parent directory if it doesn't exist
    os.makedirs(os.path.dirname(file), exist_ok=True) if os.path.dirname(file) else None
    # Create the file
    with open(file, 'a'):
        pass
    print(f"Created file: {file}")

print("\n Directory and files are successfully created")