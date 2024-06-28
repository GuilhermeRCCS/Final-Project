from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

#Responsible to interact with models and render the template

class UsersView(View):
    def get(self, request):
        users = User.objects.all()

        return render(
            request=request,
            template_name="users.html",
            context={"users": users},
        )

class FilesView(View):
    pass

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    

