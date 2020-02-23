from django.db import models

# Create your models here.
class ImgModel(models.Model):
    img = models.ImageField(upload_to='Myapp')
    msg = models.CharField(max_length=100)