from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from tasks.serializer import TaskSerializer
from tasks.models import Task
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")


@api_view(["GET"])
def get_all(request):
    data = TaskSerializer(Task.objects.all(), many=True)
    return JsonResponse(data.data, safe=False)


@api_view(["POST"])
def create(request):
    data = JSONParser().parse(request)
    serializer = TaskSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors, status=400)


@api_view(["DELETE"])
def delete_all(request):
    Task.objects.all().delete()
    return HttpResponse("Tasks deletadas")
