from django.urls import path, re_path
from hello_world import views
from hello_world.views import StaticView


urlpatterns = [
    re_path(r'^hello/([a-zA-z]+)/', views.hello_world, name='hello_world'),
    path('test_redirect1/', views.test_redirect1, name="test_redirect1"),
    path('test_redirect2/', views.test_redirect2, name="test_redirect2"),
    re_path(r'^sample_static/$', StaticView.as_view()),
]
