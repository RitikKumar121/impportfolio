from django.db import models
class Connector(models.Model):
    naam=models.CharField(null=True,max_length=200)
    last=models.CharField(null=True,max_length=200)
    gmail=models.EmailField(null=True)
    comment=models.TextField(null=True)

    def __str__(self):
        return f"{self.naam},{self.last}"
