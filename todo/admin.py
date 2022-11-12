from django.contrib import admin

from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'monday','tuesday','wednesday','thursday','friday','saturday','sunday')

# Register your models here.

admin.site.register(Todo, TodoAdmin)
