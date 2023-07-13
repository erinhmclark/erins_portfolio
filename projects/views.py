from django.shortcuts import render


def projects(response):
    return render(response, 'projects/projects.html')


def project(response):
    return render(response, 'projects/project.html')
