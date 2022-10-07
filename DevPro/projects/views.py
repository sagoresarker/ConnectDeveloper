from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def project(request, pk):
    context = {'id':pk}
    return render(request, 'projects/single-project.html', context)

def projects(request):
    context = {}
    return render(request, 'projects/projects.html')