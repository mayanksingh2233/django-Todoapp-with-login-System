# Generated by Django 3.2.4 on 2021-07-28 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_name', models.CharField(max_length=100)),
                ('is_complete', models.BooleanField(default=False)),
            ],
        ),
    ]
