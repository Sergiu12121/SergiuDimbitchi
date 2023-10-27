import re

from File import File


class ProgramFile(File):
    def detailed_info(self):
        with open(self.path, "r") as f:
            content = f.read()
            class_count = len(re.findall(r"\bclass\b", content))
            method_count = len(re.findall(r"\bdef\b", content))
            print(f"Line Count: {len(content.splitlines())}")
            print(f"Class Count: {class_count}")
            print(f"Method Count: {method_count}")
