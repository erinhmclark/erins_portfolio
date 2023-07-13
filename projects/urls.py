from django.urls import path
from . import views


urlpatterns = [
    path('', views.projects, name='projects-home'),
    # path('<int:id>', views.projects, name='project'),
]

