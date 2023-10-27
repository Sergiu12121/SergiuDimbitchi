import os
from datetime import datetime

from File import File
from TextFile import TextFile
from ImageFile import ImageFile
from ProgramFile import ProgramFile


class Folder:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.snapshot_time = None
        self.file_snapshots = {}

    def get_file_instance(self, file_path):
        extension = os.path.splitext(file_path)[1].lower()
        if extension in [".txt"]:
            return TextFile(file_path)
        elif extension in [".png", ".jpg"]:
            return ImageFile(file_path)
        elif extension in [".py", ".java"]:
            return ProgramFile(file_path)
        else:
            return File(file_path)

    def display_help(self):
        print("Available commands:")
        print("  commit - Update the snapshot time.")
        print("  file - List all available files in the folder.")
        print("  info <filename> - Display information about a specific file.")
        print("  status - Show the status of files since the last snapshot.")
        print("  exit - Exit the program.")

    def commit(self):
        self.snapshot_time = datetime.now()
        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)
            self.file_snapshots[filename] = os.path.getmtime(file_path)

    def list_files(self):
        print("Available files:")
        for filename in os.listdir(self.folder_path):
            print(filename)

    def info(self, filename):
        file_path = os.path.join(self.folder_path, filename)
        if not os.path.exists(file_path):
            print("File not found!")
            return

        file_instance = self.get_file_instance(file_path)
        file_instance.basic_info()
        file_instance.detailed_info()

    def status(self):
        if self.snapshot_time is None:
            print("No snapshot taken yet!")
            return

        print(f"Created Snapshot at: {self.snapshot_time.strftime('%H:%M , %d.%m.%Y')}")
        for filename, last_modified in self.file_snapshots.items():
            file_path = os.path.join(self.folder_path, filename)
            current_modified = os.path.getmtime(file_path)
            if current_modified > last_modified:
                print(f"{filename} : Changed")
            else:
                print(f"{filename} : No Change")
