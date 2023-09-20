from django.db import models

class user(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=20)
    password = models.CharField(max_length=16)
    def __str__(self) -> str:
        return self.name