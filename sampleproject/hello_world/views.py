from hello_world.models import Names
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


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


def test_redirect1(request):
    return redirect("https://docs.djangoproject.com/en/3.1/")


def test_redirect2(request):
    return redirect("http://127.0.0.1:8000/hello_world/hello/Jogesh/")


class StaticView(TemplateView):
   template_name = "static_file.html"
