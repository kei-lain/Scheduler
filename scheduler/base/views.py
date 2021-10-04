from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.urls import  reverse_lazy
from .models import Task 

# Create your views here.


class tasklist(LoginRequiredMixin,ListView):
	model = Task
	context_object_name = 'tasks'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tasks'] = context['tasks'].filter(user=self.request.user)
		context['count'] = context['tasks'].filter(complete=False)
		return(context)

	def randomTasks(request):
		random_object = model.objects.order_by('?').first()
		random_list = model.objects.order_by('?')
		return(random_list)
	# template_name = '/templates/base/task_list.html'
	
	

class taskDetail(LoginRequiredMixin,DetailView):
	model = Task
	context_object_name = 'task'
	template_name= 'base/task_detail.html'


class taskCreate(CreateView):
	model = Task
	fields = '__all__' #takes asll fields from model as default
	success_url = reverse_lazy('tasks') #when creating an item send them back to tasks
	def form_invalid(self,form):
		form.instance.user = self.request.user
		return super(taskCreate, self).form_valid()

class taskUpdate(UpdateView):
	model = Task
	fields = '__all__' 
	success_url = reverse_lazy('tasks')

class taskDelete(DeleteView):
	model = Task
	context_object_name ='task'
	success_url = reverse_lazy('tasks')


