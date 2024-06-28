from django.contrib import admin
from .models import File
from .models import Folder

class FileAdmin(admin.ModelAdmin):
    pass

admin.site.register(File, FileAdmin)

class FolderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Folder, FolderAdmin)