from django.shortcuts import render
# from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')
def say_hello(request):

    return render(request, 'Hello.html', {'name': 'amin'})
