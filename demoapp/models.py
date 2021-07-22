from django.db import models

# Create your models here.

class Visit(models.Model):
    name=models.CharField(max_length=100)
    tag=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images/")
    description=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField()


    def __str__(self):
        return self.name

