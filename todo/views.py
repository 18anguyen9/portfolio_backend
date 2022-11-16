from django.shortcuts import render

from rest_framework import viewsets
from .serializers import TodoSerializer, CreateTask, WeeklySerializer
from rest_framework.views import APIView
from .models import Todo, Weekly
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
import json
# Create your views here.


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    
    queryset = Todo.objects.all()

class WeeklyView(APIView):
    serializer_class = WeeklySerializer
    def get(self,request):
        queryset = Weekly.objects.all()
        serializer  = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            weekly_title = serializer.data['title']
            weekly_complete = serializer.data['completed']
            queryset = Weekly.objects.filter(title = weekly_title)
            if queryset.exists():
                task = queryset[0]
                task.title = weekly_title
                task.completed = weekly_complete
                task.save(update_fields=(['title','completed']))
            else:
                task = Weekly(title=weekly_title,completed=weekly_complete)
                task.save()
            return Response(self.serializer_class(task).data)

class AddTask(APIView):
    serializer_class = TodoSerializer
    create_serializer = CreateTask
    def get(self, request):
        queryset = Todo.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = self.create_serializer(data = request.data)
        if serializer.is_valid():
            #return HttpResponse( json.dumps( serializer.data ) )
            task_title = serializer.data['title']
            task_monday = serializer.data['monday']
            task_tuesday = serializer.data['tuesday']
            task_wednesday = serializer.data['wednesday']
            task_thursday = serializer.data['thursday']
            task_friday = serializer.data['friday']
            task_saturday = serializer.data['saturday']
            task_sunday = serializer.data['sunday']
            
            queryset = Todo.objects.filter(title=task_title)
            if queryset.exists():
                task = queryset[0]
                task.monday=task_monday
                task.tuesday=task_tuesday
                task.wednesday=task_wednesday
                task.thursday=task_thursday
                task.friday=task_friday
                task.saturday=task_saturday
                task.sunday=task_sunday
                task.save(update_fields=(['monday','tuesday','wednesday','thursday','friday','saturday','sunday']))
            else:
                task = Todo(
                    title=task_title,
                    monday=task_monday,
                    tuesday=task_tuesday,
                    wednesday = task_wednesday,
                    thursday=task_thursday,
                    friday=task_friday,
                    saturday=task_saturday,
                    sunday=task_sunday
                    )
                task.save()
            
        return Response(self.serializer_class(task).data)




    

    