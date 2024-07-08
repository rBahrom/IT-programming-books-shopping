import uuid

class SaveMedia(object):
    def save_image_path(self, filename):
        image_path = filename.split(',')[-1]
        return f"book/{uuid.uuid4()}.{image_path}"
