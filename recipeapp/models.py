from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    recipe_id = models.IntegerField(default=0)
class Ranking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ranking = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    recipe_id = models.IntegerField(default=0)
    
