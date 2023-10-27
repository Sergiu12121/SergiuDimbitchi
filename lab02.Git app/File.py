import os
from datetime import datetime


class File:
    def __init__(self, path):
        self.path = path

    def basic_info(self):
        print(f"File Name: {os.path.basename(self.path)}")
        print(f"Updated: {datetime.fromtimestamp(os.path.getctime(self.path))}")
        print(f"Created: {datetime.fromtimestamp(os.path.getmtime(self.path))}")

    def detailed_info(self):
        pass
