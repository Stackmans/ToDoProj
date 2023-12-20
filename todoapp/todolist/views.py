from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import ToDo


def index(request):
    todos = ToDo.objects.all()
    return render(request, 'todoapp/index.html', {'todolist': todos, 'title': 'Головна сторінка'})


@require_http_methods(['POST'])
def add(request):
    title = request.POST.get('title', '').strip()  # Використовуйте get() та strip() для очищення введення від пробілів
    if title:  # Перевірте, чи назва не є порожньою після очищення
        existing_todo = ToDo.objects.filter(title=title).first()
        if existing_todo is None:
            todo = ToDo(title=title)
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
