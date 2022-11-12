from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=120)
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)


    def _str_(self):
        return self.title
