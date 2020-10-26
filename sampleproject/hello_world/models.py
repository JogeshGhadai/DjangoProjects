from django.db import models
from django.db.models.signals import post_save, pre_save


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


def after_save_signal_receiver(sender, instance, **kwargs):
    # import pdb;pdb.set_trace()
    print("#### After Save Receiver Ran ####")


def before_save_receiver(sender, instance, **kwargs):
    print("#### Before Save Receiver Ran ####")


pre_save.connect(before_save_receiver, sender=Names)
post_save.connect(after_save_signal_receiver, sender=Names)
