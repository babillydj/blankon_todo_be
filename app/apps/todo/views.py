from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import render


class TodoListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    
class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    

def chat_room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

    
# class AllTodosListView(generics.ListAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
    
# class TodoUpdateView(generics.RetrieveUpdateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#     partial = True
    
    
# class TodoDeleteView(generics.DestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.delete()
#         return Response(print("delete Todo"))

