from django.db import models

class UploadedImage(models.Model):
    original = models.ImageField(upload_to='uploads/')
    processed = models.ImageField(upload_to='processed/', null=True, blank=True)
