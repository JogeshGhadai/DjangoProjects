from django.db import models

# Create your models here.
class Names(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        db_table = "names"
