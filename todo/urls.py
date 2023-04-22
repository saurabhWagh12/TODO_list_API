
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',apiOverview),
    path('task-list/',taskList,name='TaskList'),
    path('task-details/<int:pk>/',taskDetails,name='TaskDetails'),
    path('task-create/',taskCreation,name="creation"),
    path('task-update/<int:pk>/',taskUpdate,name='Update'),
    path('task-delete/<int:pk>/',deleteTask,name='deletion'),
]
