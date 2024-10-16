import requests
from django.shortcuts import render


def fetch_data(request):
    url = 'http://localhost:8080/api/projects'
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
    # TODO project_name
    project_name = request.GET.get('project_id')
    project_name = "Project1"
    print(project_id)
    # TODO http://localhost:8080/api/projects/{project_id}/task-states
    task_states_response = requests.get(f'http://localhost:8080/api/projects/102/task-states')
    task_states_data = task_states_response.json()
    print(task_states_data)

    return render(request,
                  "C:\\Users\\Arseniy\\PycharmProjects\\demoTrello\\myapp\\templates\\task_state.html",
                  {
                      'project_name': project_name,
                      'task_states': task_states_data
                  })
