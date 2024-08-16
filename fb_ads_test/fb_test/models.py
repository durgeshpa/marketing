from django.db import models

# Create your models here.
class TokenModel(models.Model):
    token = models.CharField(max_length=500,blank=True,null=True,)
    request = models.JSONField()