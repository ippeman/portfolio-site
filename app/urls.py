from django.urls import path
from app.views import todoapp, todo_post, todo_remove

urlpatterns = [
	path('todo/', todoapp),
	path("todo_post/", todo_post),
	path("todo_remove/<int:task_id>", todo_remove),
	]