from django import http
from django.shortcuts import render

class Post:
  def __init__(self, name, goal, sketch, current_state, published):
    self.name = name
    self.goal = goal
    self.sketch = sketch
    self.current_state = current_state
    self.published = published


posts = [
  Post('Bold and Brash', 'to provide a vivid look into my life', 'https://preview.redd.it/ph1xtyeangy11.jpg?width=640&crop=smart&auto=webp&s=36bed1561760cb8a86b025c8ce49a4591b77f51d', 'https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/high-res-bold-and-brash-repaint-high-res-bold-and-brash-repaint.jpg', 'yes'),

  Post('Gears of War sunset', 'to give a look into my xbox 360 breh', '', 'https://render.fineartamerica.com/images/images-profile-flow/400/images/artworkimages/mediumlarge/1/bridge-to-eternity-michael-lang.jpg', 'yes'),

  Post('commision1', 'she wanted a drawing so i drew her a drawing', 'https://i.ibb.co/28SM6z9/2-v-Q3-PGo-A.jpg', '', 'no')

]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def community_index(request):
  return render(request, 'posts/index.html', {'posts': posts})