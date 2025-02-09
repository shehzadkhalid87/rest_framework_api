from rest_framework import viewsets
from .models import Todo
from .serializations import Todoseralizer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = Todoseralizer
