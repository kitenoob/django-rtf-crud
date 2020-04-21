from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    

class Object(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, related_name="user_objects", on_delete=models.CASCADE)