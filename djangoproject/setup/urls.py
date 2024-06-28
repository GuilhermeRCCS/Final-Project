from django.contrib import admin
from django.urls import include, path
from files.views import LoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("files/", include("files.urls")),
    path("login", LoginView.as_view(), name='login'),
]
