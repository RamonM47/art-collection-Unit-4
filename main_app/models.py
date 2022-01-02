from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
  name = models.CharField(max_length=50)
  goal = models.CharField(max_length=200)
  sketch = models.CharField(max_length=500)
  current_state = models.CharField(max_length=500)
  published = models.CharField(max_length=3)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('posts_detail', kwargs={'post_id': self.id})