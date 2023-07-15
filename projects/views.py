from django.shortcuts import render
from .models import Project


def projects(response):
    context = {
        'projects': Project.objects.all()
    }
    return render(response, 'projects/projects.html', context)


def project(response, pk):
    context = {
        'project': Project.objects.get(id=pk)
    }
    return render(response, 'projects/project.html', context)
