from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class contact(models.Model):
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.phone_number


class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    todo_name=models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.todo_name +" created_by " +self.user.username