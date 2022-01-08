from django.db import models
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
# transactions
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from datetime import timedelta
import datetime


class Applicant(models.Model):
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    other_name = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to='profile_pics',
                              blank=True, null=True)
    thumb_photo = models.ImageField(upload_to='profile_pics_thumbs',
                                    blank=True, null=True)

    def __str__(self):
        return f'Student {self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        old_photo = self.photo.path if self.photo else None
        super().save(*args, **kwargs)
        try:
            if old_photo != self.photo.path:
                with open(self.photo.path, 'rb') as f:
                    self.thumb_photo = SimpleUploadedFile(
                        self.photo.name, f.read())
                super().save()
                img = Image.open(self.thumb_photo.path)
                if img.height > 200 or img.width > 200:
                    output_size = (200, 200)
                    img.thumbnail(output_size)
                    img.save(self.thumb_photo.path)
        except:
            pass


class Tutor(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    about = models.CharField(null=True, blank=True)
    photo = models.ImageField(upload_to='profile_pics',
                              blank=True, null=True)
    thumb_photo = models.ImageField(upload_to='profile_pics_thumbs',
                                    blank=True, null=True)

    def save(self, *args, **kwargs):
        old_photo = self.photo.path if self.photo else None
        super().save(*args, **kwargs)
        try:
            if old_photo != self.photo.path:
                with open(self.photo.path, 'rb') as f:
                    self.thumb_photo = SimpleUploadedFile(
                        self.photo.name, f.read())
                super().save()
                img = Image.open(self.thumb_photo.path)
                if img.height > 200 or img.width > 200:
                    output_size = (200, 200)
                    img.thumbnail(output_size)
                    img.save(self.thumb_photo.path)
        except:
            pass


class Course(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Outline(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
