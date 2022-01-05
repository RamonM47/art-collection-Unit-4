from django.db import models
from django.db.models.fields import URLField
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

TOD = (
  ('M', 'Morning'),
  ('A', 'AfterNoon'),
  ('N', 'Night')
)

# Create your models here.
class Post(models.Model):
  name = models.CharField(max_length=50)
  goal = models.TextField(max_length=250)
  sketch = models.URLField(max_length=500)
  current_state = models.URLField(max_length=500)
  published = models.BooleanField()
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

  def worked_on_today(self):
    return self.work_set.filter(date=date.today()).count() >= len(TOD)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('posts_detail', kwargs={'post_id': self.id})
  
class Work(models.Model):
  date = models.DateField()
  tod = models.CharField(
    max_length=1, 
    choices=TOD, 
    default=TOD[0][0]
  )
  progress_pic = URLField(max_length=250, default='https://toppng.com//public/uploads/preview/9d5-badly-drawn-thinking-emoji-11562863577r4jcmmnhf9.png')
  post = models.ForeignKey(Post, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_tod_display()} on {self.date}"

  class Meta:
    ordering = ['date']

class Photo(models.Model):
  url = models.CharField(max_length=250)
  post = models.OneToOneField(Post, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for post_id: {self.post_id} @{self.url}."