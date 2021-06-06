from django.db import models
class Connector(models.Model):
    naam=models.CharField(max_length=200)
    last=models.CharField(max_length=200)
    gmail=models.EmailField()
    comment=models.TextField()

    def __str__(self):
        return f"{self.naam},{self.last}"
