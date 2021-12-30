from django.db import models

# Create your models here.
class Post(models.Model):
  name = models.CharField(max_length=50)
  goal = models.CharField(max_length=200)
  sketch = models.CharField(max_length=100)
  current_state = models.CharField(max_length=100)
  current_state = models.CharField(max_length=3)