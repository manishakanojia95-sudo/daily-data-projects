import os
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
folder = f"project-{today}"

os.makedirs(folder, exist_ok=True)

with open(f"{folder}/README.md", "w") as f:
    f.write(f"# Project {today}\n\nAuto-generated project 🚀")

print("Project created successfully")
