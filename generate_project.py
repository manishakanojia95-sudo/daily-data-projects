import os
from datetime import datetime

# Get today's date
today = datetime.now().strftime("%Y-%m-%d")

# Create folder
folder = f"project-{today}"
os.makedirs(folder, exist_ok=True)

# Create README file
with open(f"{folder}/README.md", "w") as f:
    f.write(f"# Project {today}\n\nThis is your auto-generated project ✅")

print("Project created successfully")
