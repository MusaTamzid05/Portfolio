from django.db import models

# Create your models here.

class Project(models.Model):

    image = models.ImageField(upload_to = "images/" , null = True , blank = True )
    summary = models.CharField(max_length = 200)
    link = models.CharField(max_length = 200)

    def __str__(self):
        return self.summary
