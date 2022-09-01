import re
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Core
from .forms import PostForm


def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()
            # Redirect to Home
            return HttpResponseRedirect('/')

        else:
            # No, Show Error
            return HttpResponseRedirect(form.erros.as_json())



    # Get all core, limit = 20
    cores = Core.objects.all().order_by('-created_at')[:20]

    # Show
    return render(request, 'core.html', 
                    {'cores': cores})

def delete(request, core_id):
    # Find post
    core = Core.objects.get(id = core_id)
    core.delete()
    return HttpResponseRedirect('/')


def edit(request, core_id):
    core=Core.objects.get(id=core_id)

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=core)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()
            # Redirect to Home
            return HttpResponseRedirect('/')

        else:
            # No, Show Error
            return HttpResponseRedirect(form.erros.as_json())
    return render (request, 'edit.html', {'core': core})

def LikeView(request, core_id):
    core= Core.objects.get(id=core_id)
    new_value = core.likes + 1
    core.likes = new_value
    core.save()
    return HttpResponseRedirect('/')
