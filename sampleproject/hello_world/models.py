from django.db import models

# Create your models here.
class Names(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        db_table = "names"


class Profile(models.Model):

   name = models.CharField(max_length = 50)
   picture = models.ImageField(upload_to = '~/Desktop/Uploaded')

   class Meta:
      db_table = "profile"
