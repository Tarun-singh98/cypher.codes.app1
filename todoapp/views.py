from django.shortcuts import render, redirect

from todoapp.models import *
from todoapp.forms import *

# Create your views here.

def index(request):
    todoapp = task.objects.all()
    form = taskform()

    if request.method == 'POST':
        form = taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


    context = {'todoapp':todoapp,'form':form}
    return render(request,'todoapp/index.htm', context)

def updatetask(request, pk):
	Task = task.objects.get(id=pk)

	form = taskform(instance=Task)
    
	if request.method == 'POST':
		form = taskform(request.POST, instance=Task)
		if form.is_valid():
			form.save()
			return redirect('/')


	context = {'form':form}

	return render(request,'todoapp/update_task.htm', context)

def deletetask(request, pk):
	item = task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'todoapp/delete.htm', context)