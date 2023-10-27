import threading
from Folder import Folder


class Main:
    def __init__(self, folder_path):
        self.monitor = Folder(folder_path)

    def display_help(self):
        print("Available commands:")
        print("  commit - Update the snapshot time.")
        print("  info <filename> - Display information about a specific file.")
        print("  status - Show the status of files since the last snapshot.")
        print("  exit - Exit the program.")

    def start(self):
        self.monitor.commit()
        detection_thread = threading.Thread(target=self.monitor.detect_changes)
        detection_thread.daemon = True
        detection_thread.start()

        self.display_help()
        while True:
            command = input("Enter command: ").split()
            if not command:
                continue
            if command[0] == "commit":
                self.monitor.commit()
                print("Snapshot time updated")
            elif command[0] == "info":
                if len(command) < 2:
                    print("Please provide a filename for the info command.")
                    self.monitor.list_files()
                else:
                    self.monitor.info(command[1])
            elif command[0] == "status":
                self.monitor.status()
            elif command[0] == "exit":
                break
            else:
                print("Wrong command!")
                self.display_help()


def main():
    sergiu_folder = Main("/Users/sergiu_sd/Desktop/test_folder")
    sergiu_folder.start()


if __name__ == "__main__":
    main()
