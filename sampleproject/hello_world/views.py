from django.shortcuts import render

def hello_world(request):
    # import pdb;pdb.set_trace()
    return render(request, 'hello_world.html', {})
