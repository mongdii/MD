from django.contrib import admin
from .models import CommentDB


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username',)

admin.site.register(CommentDB, CommentAdmin)

