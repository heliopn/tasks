from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from tasks.serializer import TaskSerializer
from tasks.models import Task
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")


@api_view(["GET"])
def getTasks(request):
    data = TaskSerializer(Task.objects.all(), many=True)
    return JsonResponse(data.data, safe=False)


@api_view(["POST"])
def createTasks(request):
    data = JSONParser().parse(request)
    task_ser = TaskSerializer(data=data)
    if task_ser.is_valid():
        task_ser.save()
        return JsonResponse(task_ser.data, status=200)
    return JsonResponse(task_ser.errors, status=400)


@api_view(["DELETE"])
def deleteTasks(request):
    Task.objects.all().delete()
    return HttpResponse("TASKS DELETED")
