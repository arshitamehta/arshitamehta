from django.db import models

# Create your models here.

class Art(models.Model):
    name = models.CharField(max_length=100)
    art = models.ImageField(upload_to="img/%y")
    def __str__(self):
        return self.name
    
