from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
    else:
        city = ''
    return render(request, 'index.html', {'city': city})
