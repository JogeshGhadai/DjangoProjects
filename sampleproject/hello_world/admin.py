from django.contrib import admin
from hello_world.models import Names


# Register your models here.
class NamesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Names, NamesAdmin)
