from hello_world.models import Names
from django.shortcuts import render


def hello_world(request, name):
    # import pdb;pdb.set_trace()
    print("Hello "+name)
    all_names = Names.objects.all()
    all_name_list = [x.name for x in all_names]
    chk_name = name.lower() in all_name_list
    if not chk_name:
        all_name_list.append(name)
        name_obj = Names(name=name.lower())
        name_obj.save()
    context_dict = {
            "name": name,
            "chk": name[0].lower(),
            "itr": list(enumerate([x.title() for x in all_name_list], start=1)),
        }
    return render(request, 'hello_world.html', context_dict)
