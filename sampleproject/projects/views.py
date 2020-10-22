from django.shortcuts import render
from projects.models import Project


# Create your views here.
def project_index(request):
    # import pdb; pdb.set_trace()
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    # import pdb;pdb.set_trace()
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
