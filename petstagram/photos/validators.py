from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ImageSizeValidator:
    def __init__(self, image_size_mb, message=None):
        self.image_size_mb = image_size_mb
        self.message = message or f"The IMG file must be below {image_size_mb}MB"

    def __call__(self, value):
        if value.size > self.image_size_mb * 1024 * 1024:
            raise ValidationError(self.message)
