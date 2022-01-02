from django.db import models
from django.urls import reverse

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

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
  
class Work(models.Model):
  date = models.DateField('Last worked on')
  meal = models.CharField(
    max_length=3, 
    choices=MEALS, 
    default=MEALS[0][0]
  )

  post = models.ForeignKey(Post, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"