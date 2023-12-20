from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import ToDo


def index(request):
    todos = ToDo.objects.all()
    return render(request, 'todoapp/index.html', {'todolist': todos, 'title': 'Головна сторінка'})


@require_http_methods(['POST'])
# @csrf_exempt
def add(request):
    title = request.POST['title']
    todo = ToDo(title=title)
    if todo.title == '':
        pass
    else:
        todo.save()
    return redirect('index')


def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')


def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')
