from django.urls import path
from . import views


urlpatterns = [
    path('', views.projects, name='projects-home'),
    path('<int:pk>/', views.project, name='project'),
]

