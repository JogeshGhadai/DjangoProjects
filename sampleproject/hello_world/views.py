from hello_world.models import Names, Profile
from hello_world.forms import LoginForm, ProfileForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.signals import request_started, request_finished
from django.dispatch import receiver


def hello_world(request, name):
    # import pdb;pdb.set_trace()
    print("Hello "+name)
    all_names = Names.objects.all()
    all_name_list = [x.name for x in all_names]
    chk_name = name.lower() in all_name_list
    flag = 'old'
    if not chk_name:
        flag = 'new'
        all_name_list.append(name)
        name_obj = Names(name=name.lower())
        name_obj.save()
    context_dict = {
            "name": name,
            "chk": flag,
            "itr": list(enumerate([x.title() for x in all_name_list], start=1)),
        }
    return render(request, 'hello_world.html', context_dict)


@receiver(request_finished)
def do_at_request_finish(sender, **kwargs):
    # import pdb;pdb.set_trace()
    print("#### Request Finished ####")


@receiver(request_started)
def do_at_request_start(sender, **kwargs):
    print("#### Request Started ####")


def test_redirect1(request):
    return redirect("https://docs.djangoproject.com/en/3.1/")


def test_redirect2(request):
    return redirect("http://127.0.0.1:8000/hello_world/hello/Jogesh/")


def login_form_test(request):
    username = "not logged in"
    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
    else:
        MyLoginForm = LoginForm()
    return render(request, 'login.html', {"username" : username})


def SaveProfile(request):
   saved = False
   if request.method == "POST":
      MyProfileForm = ProfileForm(request.POST, request.FILES)
      if MyProfileForm.is_valid():
         profile = Profile()
         profile.name = MyProfileForm.cleaned_data["name"]
         profile.picture = MyProfileForm.cleaned_data["picture"]
         profile.save()
         saved = True
   else:
      MyProfileForm = Profileform()
		
   return render(request, 'saved.html', locals())


class StaticView(TemplateView):
   template_name = "static_file.html"



