import re
import django
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Photo
from .forms import WorkForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3

#AWS

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'art-collector-ramon'

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required(login_url='/')
def community_index(request):
  posts = Post.objects.all()
  return render(request, 'posts/index.html', {'posts': posts})

@login_required(login_url='/')
def posts_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  work_form = WorkForm()
  return render(request, 'posts/detail.html', { 'post': post, 'work_form': work_form })

@login_required(login_url='/')
def add_worked_on(request, post_id):
  form = WorkForm(request.POST)
  if form.is_valid():
    new_work = form.save(commit=False)
    new_work.post_id = post_id
    new_work.save()
  return redirect('posts_detail', post_id=post_id)

class PostCreate(LoginRequiredMixin, CreateView):
  login_url = '/'
  model = Post
  fields = ['name', 'goal', 'sketch', 'current_state', 'published']
  success_url = '/posts/'

  def form_vaild(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class PostUpdate(LoginRequiredMixin , UpdateView):
  login_url = '/'
  model = Post
  fields = ['name', 'current_state', 'published']

class PostDelete(LoginRequiredMixin, DeleteView):
  login_url = '/'
  model = Post
  success_url = '/posts/'
  
@login_required(login_url='/')
def add_photo(request, post_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, post_id=post_id)
      post_photo = Photo.objects.filter(post_id=post_id)
      if post_photo.first():
        post_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('posts_detail', post_id=post_id)

class Home(LoginView):
  template_name = 'home.html'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('community_index')
    else:
      error_message = 'invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)