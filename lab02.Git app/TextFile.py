from File import File


class TextFile(File):
    def detailed_info(self):
        with open(self.path, "r") as f:
            content = f.read()
            print(f"Line Count: {len(content.splitlines())}")
            print(f"Word Count: {len(content.split())}")
            print(f"Character Count: {len(content)}")
