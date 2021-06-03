from django.shortcuts import render
from .models import Project
# Create your views here.
def home(request):
    projects = Project.objects.all()
    context = {'project': projects
    }
    return render(request, 'homepage.html', context)

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
  project = Project.objects.get(pk=pk)
  context = {
    'project': project
  }
  return render(request, 'project_detail.html', context)

def services_provided(request):
  return render(request, 'services.html', {})

def about_me(request):
  return render(request, 'about_page.html', {})

def contact(request):
  return render(request, 'contact.html', {})
