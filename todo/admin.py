from django.contrib import admin

from .models import Todo, Weekly

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'monday','tuesday','wednesday','thursday','friday','saturday','sunday')
class WeeklyAdmin(admin.ModelAdmin):
    list_display = ('title','completed')

# Register your models here.

admin.site.register(Todo, TodoAdmin)
admin.site.register(Weekly,WeeklyAdmin)
