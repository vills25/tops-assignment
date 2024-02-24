from django.urls import path
from .views import task_create, task_update_delete

urlpatterns = [
    path('', task_create, name='task_create'),
    path('<int:pk>/', task_update_delete, name='task_update_delete'),
]

