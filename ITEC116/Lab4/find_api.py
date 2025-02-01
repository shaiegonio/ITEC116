import os

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            with open(os.path.join(root, file), "r", errors="ignore") as f:
                for line in f:
                    if "API_KEY" in line:
                        print(f"Found in {file}: {line.strip()}")
