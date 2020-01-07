from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField("Заголовок курса", blank=True, max_length=255)
