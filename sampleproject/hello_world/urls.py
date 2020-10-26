from django.urls import path, re_path
from hello_world import views
from hello_world.views import StaticView
from django.views.generic import TemplateView


urlpatterns = [
    re_path(r'^hello/([a-zA-z]+)/', views.hello_world, name='hello_world'),
    path('test_redirect1/', views.test_redirect1, name="test_redirect1"),
    path('test_redirect2/', views.test_redirect2, name="test_redirect2"),
    re_path(r'^sample_static/$', StaticView.as_view()),
    # path('login_form_test/', views.login_form_test, name="login_form_test"),
    # path('login_form_test/', TemplateView.as_view(template_name = 'login.html')),
    # re_path(r'^profile/',TemplateView.as_view(template_name = 'profile.html')), 
    # re_path(r'^saved/', views.SaveProfile, name = 'saved'),
]
