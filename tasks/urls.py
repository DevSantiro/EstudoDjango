from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.helloWorld),
    path('listtask', views.tasksList, name='task-list'),
    path('task/<int:id>', views.taskView, name='task-view'),
    path('edit/<int:id>', views.editTask, name="edit-task"),
    path('delete/<int:id>', views.deleteTask, name="delete-task"),
    path('newtask/', views.newTask, name='new-task'),
    path('yourname/<str:name>', views.yourName,name='your-name'),
    path('',views.tasksIndex, name='task-index'),
    path('teste/', views.teste,name='pagina-teste'),
    path('novaSequencia/', views.upload_seq, name='inserir-sequencia'),
    path('listSequencia/', views.seq_list, name='lista-sequencia'),
    path('testeCMD/', views.testeCMD, name='teste-cmd'),
    path('proteina/<int:id>', views.infoProteina, name='lista-proteina'),
    path('geraModelo/<int:id>', views.getModelo, name='getModelo')
]
