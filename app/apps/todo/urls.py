from django.urls import path, include
from . import views


app_name = 'todo'
urlpatterns = [
    path('api/v1/todo/', include(
        ([
            path('', views.TodoListCreateView.as_view(), name='list_todo'),
            path('<int:pk>/', views.TodoDetailView.as_view(), name='detail_todo'),
        ], 'todo_api_v1')
    )),
]
