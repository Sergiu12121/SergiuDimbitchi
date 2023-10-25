import os
import time


class File:
    def __init__(self, path):
        self.path = path
        self.filename = os.path.basename(path)
        self.extension = os.path.splitext(self.filename)[1]
        self.created_time = os.path.getctime(path)
        self.last_modified_time = os.path.getmtime(path)

    def has_changed(self, snapshot_time):
        return self.last_modified_time > snapshot_time


class FolderMonitor:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.snapshot_time = time.time()
        self.files = self.load_files()

    def load_files(self):
        files = {}
        for filename in os.listdir(self.folder_path):
            path = os.path.join(self.folder_path, filename)
            if os.path.isfile(path):
                files[filename] = File(path)
        return files

    def commit(self):
        self.snapshot_time = time.time()

    def status(self):
        for filename, file in self.files.items():
            status = "Changed" if file.has_changed(self.snapshot_time) else "No Change"
            print(f"{filename} - {status}")


if __name__ == "__main__":
    folder_path = "/Users/sergiu_sd/Desktop/test_folder"
    monitor = FolderMonitor(folder_path)
    print(monitor.snapshot_time)

    while True:
        command = input("> ")
        if command == "help":
            print("'commit' - Update the snapshot time")
            print("'status' - Display the change status of each file.")
            print("'exit' - Exit")
        elif command == "commit":
            monitor.commit()
            print("Snapshot updated.")
        elif command == "status":
            monitor.status()
        elif command == "exit":
            break
        else:
            print("Unknown command! Type 'help' for all the commands.")
