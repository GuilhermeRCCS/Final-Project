from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.core.exceptions import ValidationError


class File(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=False,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent_folder = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subfolders',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
           unique_together = ('name', 'parent_folder')

    def __str__(self):
                return self.name
    
# I'm using a Django Validation for folder organisation. Prevention of a folder being inside a folder that is inside itself.
    def clean(self):
           if self.parent_folder:
                  parent = self.parent_folder
                  while parent:
                         if parent == self:
                                raise ValidationError("Folder cannot be descendant of itself")
                         parent = parent
           