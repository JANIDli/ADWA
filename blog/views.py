from django.shortcuts import render, redirect
from .models import BlogPost
from .form import BlogForm
# Create your views here.
from django.contrib.auth.decorators import login_required

def home(req):
    post = BlogPost.objects.all()
    context = {'post':post}
    return render(req, 'blog/home.html', context)

@login_required(login_url='login')
def single_post(req, pk):
    post = BlogPost.objects.get(id = pk)
    context = {'post':post}
    return render(req, 'blog/single.html', context)

@login_required(login_url='login')
def add_post(req):
    if req.user.is_superuser:
        form = BlogForm()
        if req.method == "POST":
            form = BlogForm(req.POST, req.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        return redirect('home')
    context = {'form':form}
    return render(req, 'blog/form.html', context)


@login_required(login_url='login')
def update_post(req, pk):
    if req.user.is_superuser:
        post = BlogPost.objects.get(id =pk)
        form = BlogForm(instance=post)
        if req.method == "POST":
            form = BlogForm(req.POST, req.FILES, instance=post)

            if form.is_valid():
                form.save()
                return redirect('home')
    else:
        return redirect('home')
    context = {'form':form}
    return render(req, 'blog/form.html', context)

@login_required(login_url='login')
def delete_post(req, pk):
    if req.user.is_authenticated:
        post = BlogPost.objects.get(id = pk)
        post.delete()
        return redirect('home')
    else:
        return redirect('home')

@login_required(login_url='login')
def adminpage(req):
    if req.user.is_superuser:
        post = BlogPost.objects.all()
    else:
        return redirect('home')
    context = {'post':post}
    return render(req, 'blog/edit-post.html', context)


