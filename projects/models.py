from django.db import models

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=100, null=True)
  description = models.TextField(null=True)
  technology = models.CharField(max_length=20, null=True)
  image = models.FilePathField(path="static/media", null=True)

  objects = models.Manager()

  def __str__(self):
    return self.title
