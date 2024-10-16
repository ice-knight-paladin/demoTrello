from django.urls import path
from .views import fetch_data
from .views import project_task_states

urlpatterns = [
    path("project/", fetch_data, name='fetch_data'),
    path('projects/<str:project_id>/task-states/', project_task_states, name='task_states'),
]
