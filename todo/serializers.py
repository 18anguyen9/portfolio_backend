from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title', 'monday','tuesday','wednesday','thursday','friday','saturday','sunday')
class CreateTask(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'monday','tuesday','wednesday','thursday','friday','saturday','sunday')