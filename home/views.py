from django.shortcuts import render
from .models import Todo
# from django.http import HttpResponse

def home(request):
    allTodo=Todo.objects.all()
    return render(request, 'home.html',{'todos':allTodo})
def say_hello(request):

    return render(request, 'Hello.html', {'name': 'amin'})
