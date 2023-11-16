from django.shortcuts import render
from .models import Todo
# from django.http import HttpResponse

def home(request):
    allTodo=Todo.objects.all()
    return render(request, 'home.html',{'todos':allTodo})
def say_hello(request):

    return render(request, 'Hello.html', {'name': 'amin'})

def detail(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    return render(request,'detail.html',{'todo':todo})
