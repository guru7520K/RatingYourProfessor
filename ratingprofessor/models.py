

# Create your models here.
# models.py

import uuid
from django.db import models
from django.contrib.auth.models import User

from django.db.models import Avg




class Professor(models.Model):
    name = models.CharField(max_length=255)
    
    
    def get_average_rating(self):
        return Rating.objects.filter(professor=self).aggregate(Avg('rating'))['rating__avg']
    def __str__(self):
        return self.name


class Rating(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    #rater = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user_id', 'professor'),)
        
    def get_average_rating(self):
        return Rating.objects.filter(professor=self).aggregate(Avg('rating'))['rating__avg']

