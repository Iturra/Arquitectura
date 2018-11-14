from django.shortcuts import render

def index(request):
  return render(request,'blog/index.html',{})

def registrou(request):
  return render(request,'blog/registrou.html',{})

