from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('add_todo/', views.add_todo, name='add_todo'),
	path('mark_done/', views.mark_done, name='mark_done'),
	path('del_todo/', views.del_todo, name='del_todo'),
]