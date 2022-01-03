import re
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Photo
from .forms import WorkForm
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

def community_index(request):
  posts = Post.objects.all()
  return render(request, 'posts/index.html', {'posts': posts})

def posts_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  work_form = WorkForm()
  return render(request, 'posts/detail.html', { 'post': post, 'work_form': work_form })

def add_worked_on(request, post_id):
  form = WorkForm(request.POST)
  if form.is_valid():
    new_work = form.save(commit=False)
    new_work.post_id = post_id
    new_work.save()
  return redirect('posts_detail', post_id=post_id)

class PostCreate(CreateView):
  model = Post
  fields = '__all__'
  success_url = '/posts/'

class PostUpdate(UpdateView):
  model = Post
  fields = ['name', 'current_state', 'published']

class PostDelete(DeleteView):
  model = Post
  success_url = '/posts/'

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