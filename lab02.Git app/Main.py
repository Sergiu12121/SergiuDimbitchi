import os
import time
import re
from datetime import datetime
from PIL import Image

FOLDER_PATH = "/Users/sergiu_sd/Desktop/test_folder"

snapshot_time = None
file_snapshots = {}


def display_help():
    print("Available commands:")
    print("  commit - Update the snapshot time.")
    print("  info <filename> - Display information about a specific file.")
    print("  status - Show the status of files since the last snapshot.")
    print("  exit - Exit the program.")
    print("  help - Display this help message.")


def commit():
    global snapshot_time
    snapshot_time = datetime.now()
    for filename in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, filename)
        file_snapshots[filename] = os.path.getmtime(file_path)


def info(filename):
    file_path = os.path.join(FOLDER_PATH, filename)
    if not os.path.exists(file_path):
        print("File not found!")
        return

    print(f"File Name: {filename}")
    extension = filename.split(".")[-1]
    print(f"File Extension: {extension}")
    print(f"Created: {datetime.fromtimestamp(os.path.getctime(file_path))}")
    print(f"Updated: {datetime.fromtimestamp(os.path.getmtime(file_path))}")

    if extension in ["png", "jpg"]:
        with Image.open(file_path) as img:
            width, height = img.size
            print(f"Image Size: {width}x{height}")

    elif extension == "txt":
        with open(file_path, "r") as f:
            content = f.read()
            print(f"Line Count: {len(content.splitlines())}")
            print(f"Word Count: {len(content.split())}")
            print(f"Character Count: {len(content)}")

    elif extension in ["py", "java"]:
        with open(file_path, "r") as f:
            content = f.read()
            class_count = len(re.findall(r"\bclass\b", content))
            method_count = (
                len(re.findall(r"\bdef\b", content))
                if extension == "py"
                else len(re.findall(r"\bvoid\b|\bpublic\b|\bprivate\b", content))
            )
            print(f"Line Count: {len(content.splitlines())}")
            print(f"Class Count: {class_count}")
            print(f"Method Count: {method_count}")


def status():
    if snapshot_time is None:
        print("No snapshot taken yet!")
        return

    print(f"Created Snapshot at: {snapshot_time.strftime('%H:%M , %d.%m.%Y')}")
    for filename, last_modified in file_snapshots.items():
        file_path = os.path.join(FOLDER_PATH, filename)
        current_modified = os.path.getmtime(file_path)
        if current_modified > last_modified:
            print(f"{filename} : Changed")
        else:
            print(f"{filename} : No Change")


def main():
    
    while True:
        command = input("Enter command: ").split()
        if not command:
            continue

        if command[0] == "commit":
            commit()
        elif command[0] == "info":
            if len(command) < 2:
                print("Please provide a filename for the info command.")
            else:
                info(command[1])
        elif command[0] == "status":
            status()
        elif command[0] == "exit":
            break
        elif command[0] == "help":
            display_help()
        else:
            print("Wrong command!")
            display_help()


if __name__ == "__main__":
    main()
