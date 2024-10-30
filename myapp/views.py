import requests
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Task, TaskState
from .serializers import TaskSerializer


def fetch_data(request):
    url = 'http://192.168.182.211:8080/api/projects'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
    else:
        data = None

    context = {
        'data': data
    }
    return render(request, "C:\\Users\\Arseniy\\PycharmProjects\\demoTrello\\myapp\\templates\\project.html", context)


def project_task_states(request, project_id):
    url = 'http://192.168.182.211:8080/api/projects'
    response = requests.get(url)
    project_name = list(filter(lambda x: int(x["id"]) == int(project_id), response.json()))[0]["name"]
    task_states_response = requests.get(f'http://192.168.182.211:8080/api/projects/{project_id}/task-states')
    task_states_data = task_states_response.json()

    return render(request,
                  "C:\\Users\\Arseniy\\PycharmProjects\\demoTrello\\myapp\\templates\\task_state.html",
                  {
                      'project_name': project_name,
                      'task_states': task_states_data
                  })


class TaskStateTasksCreateView(generics.CreateAPIView):
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task_state_id = self.kwargs.get('task_state_id')
        task_state = TaskState.objects.get(id=task_state_id)
        serializer.save(task_state=task_state)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
