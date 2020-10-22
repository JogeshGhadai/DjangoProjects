from django.urls import path, re_path
from hello_world import views

urlpatterns = [
    re_path(r'^hello/([a-zA-z]+)/', views.hello_world, name='hello_world'),
]
