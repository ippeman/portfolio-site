from django.urls import path
from . import views

urlpatterns = [
	path('', views.Index.as_view()),
	path('index.html', views.Index.as_view()),
]