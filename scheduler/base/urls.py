from django.urls import path
from .views import taskDetail, tasklist, taskCreate, taskUpdate, taskDelete
from .models import Task

urlpatterns = [
path('',tasklist.as_view(), name='tasks'),
path('task/<int:pk>/', taskDetail.as_view(), name='task'), 
path('create-task/', taskCreate.as_view(), name= 'create-task'),
path('update-task/<int:pk>/==', taskUpdate.as_view(), name= 'update-task'),
path('delete-task/<int:pk>/==', taskDelete.as_view(), name= 'delete-task')
]
