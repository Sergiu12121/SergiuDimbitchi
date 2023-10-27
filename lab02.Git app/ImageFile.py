from PIL import Image

from File import File


class ImageFile(File):
    def detailed_info(self):
        with Image.open(self.path) as img:
            width, height = img.size
            print(f"Image Size: {width}x{height}")
