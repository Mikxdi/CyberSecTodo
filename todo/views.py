from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import connection
from .models import Todo

@login_required
def index(request):
	username = request.user.username
	todos = Todo.objects.all()


	context = {'username': username, 'todos': todos}

	return render(request, 'index.html', context)

@login_required
def add_todo(request):
	if request.method == "GET":
		current = request.user
		name = request.GET['todo_name']
		description = request.GET['todo_description']
		newTodo = Todo(user=current, name=name, description=description)
		newTodo.save()
		return HttpResponseRedirect('/')
	
	return redirect('/')

@login_required
def mark_done(request):
	if request.method == "GET":
		namereq = request.GET.get('todo_name')
		todo = Todo.objects.get(name = namereq)
		todo.done = not todo.done
		todo.save()
		return HttpResponseRedirect('/')

	return redirect('/')

@login_required
def del_todo(request):
	if request.method == "POST":
		deletename = request.POST.get('todo_name')
		todos = Todo.objects.raw("SELECT * FROM todo_todo WHERE name LIKE '%{}%'".format(deletename))

		for todo in todos:
			todo.delete()
		
		return HttpResponseRedirect('/')
			
	return redirect('/')