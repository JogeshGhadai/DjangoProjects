from django.shortcuts import render

def hello_world(request, name):
    # import pdb;pdb.set_trace()
    print("Hello "+name)
    return render(request, 'hello_world.html', {"name":name, "chk":name[0].lower(), "itr":[1,2,3,4,5]})
