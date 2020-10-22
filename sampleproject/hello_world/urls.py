from django.urls import path, re_path
from hello_world import views

urlpatterns = [
    re_path(r'^hello', views.hello_world, name='hello_world'),
]
