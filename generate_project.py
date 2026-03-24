import os
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
folder = f"project-{today}"

os.makedirs(folder, exist_ok=True)

content = f"# Project {today}\n\nThis is your auto-generated project."

with open(f"{folder}/README.md", "w") as f:
    f.write(content)

print("Project created successfully")
