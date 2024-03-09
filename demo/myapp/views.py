from django.shortcuts import render, HttpResponse
from .models import TodoItems

# Create your views here.
def home(request):
    return render(request, 'home.html')

def todo(request):
    items = TodoItems.objects.all()
    return render(request, 'todo.html', {'todo': items})