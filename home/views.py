from django.shortcuts import render,redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm
# from django.http import HttpResponse

def home(request):
    allTodo=Todo.objects.all()
    return render(request, 'home.html',{'todos':allTodo})

def detail(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    return render(request,'detail.html',{'todo':todo})


def delete(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request,'todo deleted successfully','success')
    return redirect('home')


def create(request):
    if request.method =='POST':
        form=TodoCreateForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            Todo.objects.create(title=cd['title'], body=cd['body'],created=cd['created'])
            messages.success(request,'Todo creted Successfully','success')
            return redirect('home')
    else:
        form=TodoCreateForm()
    return render(request,'create.html',{'form': form})
