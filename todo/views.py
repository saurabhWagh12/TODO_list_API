from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializers import TaskSerializer
from .models import *

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    apiUrls = {
        'List':'/task-list/',
        'Details View':'/task-details/<int:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<int:pk>/',
        'Delete':'/task-delete/<int:pk>/'
    }
    return Response(apiUrls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetails(request,pk):
    task = Task.objects.get(pk = pk)
    serializer = TaskSerializer(task,many=False)
    return Response(serializer.data)
    

@api_view(['POST'])
def taskCreation(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(pk = pk)
    serializer = TaskSerializer(instance=task,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTask(request,pk):
    task = Task.objects.get(pk = pk)
    task.delete()
    return Response('Item Successfully Deleted')



