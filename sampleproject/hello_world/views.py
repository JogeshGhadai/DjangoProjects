from django.shortcuts import render

def hello_world(request, name):
    # import pdb;pdb.set_trace()
    print("Hello "+name)
    return render(request, 'hello_world.html', {"name":name})
