from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_tasks', views.createTasks, name='create_tasks'),
    path('get_tasks', views.getTasks, name='get_tasks'),
    path('delete_tasks', views.deleteTasks, name='delete_tasks')]
