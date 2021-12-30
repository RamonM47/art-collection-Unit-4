from django import http
from django.shortcuts import render
from django.http import HttpResponse

class Post:
  def __init__(self, name, goal, sketch, current_state):
    self.name = name
    self.goal = goal
    self.sketch = sketch
    self.current_state = current_state

posts = [
  Post('Bold and Brash', 'to provide a vivid look into my life', 'https://preview.redd.it/ph1xtyeangy11.jpg?width=640&crop=smart&auto=webp&s=36bed1561760cb8a86b025c8ce49a4591b77f51d', 'https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/high-res-bold-and-brash-repaint-high-res-bold-and-brash-repaint.jpg')
]

# Create your views here.
def home(request):
  return HttpResponse('<a href="/about">About</a>')

def about(request):
  return render(request, 'about.html')

def community_index(request):
  return render(request, 'community/index.html', {'posts': posts})