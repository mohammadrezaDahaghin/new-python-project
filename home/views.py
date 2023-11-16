from django.shortcuts import render,redirect
from .models import Todo
# from django.http import HttpResponse

def home(request):
    allTodo=Todo.objects.all()
    return render(request, 'home.html',{'todos':allTodo})

def detail(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    return render(request,'detail.html',{'todo':todo})


def delete(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('home')
