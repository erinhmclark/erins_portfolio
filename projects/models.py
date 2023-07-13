from django.db import models
from PIL import Image


class Project(models.Model):
    title = models.CharField(max_length=200)
    external_link = models.URLField(max_length=200)
    summary = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(default='default.jpeg', upload_to='project_images')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
