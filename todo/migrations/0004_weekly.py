# Generated by Django 4.0.4 on 2022-11-14 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_rename_completed_todo_friday_todo_monday_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weekly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
