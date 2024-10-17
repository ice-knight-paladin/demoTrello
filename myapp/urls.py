from django.urls import path
from .views import fetch_data, TaskStateTasksCreateView
from .views import project_task_states

urlpatterns = [
    path("project/", fetch_data, name='fetch_data'),
    path('projects/<str:project_id>/task-states/', project_task_states, name='task_states'),
    path('api/task-states/<int:task_state_id>/tasks/', TaskStateTasksCreateView.as_view(), name='task-state-tasks'),
]
