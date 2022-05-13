from django.urls import path
from app.views import todoapp, todo_post

urlpatterns = [
	path('todo/', todoapp),
	path('todo_post/', todo_post),
	]