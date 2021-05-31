from django.db import models

# Create your models here.
class Operation(models.Model):
    arg1 = models.FloatField(null=False)
    arg2 = models.FloatField(null=False)
    operation_name = models.CharField(max_length=12)
    result = models.FloatField()
    performed = models.DateTimeField(auto_now=True)