from django.urls import path
from app.views import portfolioapp, todo_post, todo_remove

urlpatterns = [
	path('todo/', portfolioapp),
	path("todo_post/", todo_post),
	path("todo_remove/<int:task_id>", todo_remove),
	]