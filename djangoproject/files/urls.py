from django.urls import path
from files.views import UsersView, FilesView
from .views import LoginView

#Defining which url corresponds with which view

urlpatterns = [
    path('users', UsersView.as_view(), name='users'),
    path("files", FilesView.as_view(), name="files"),
]