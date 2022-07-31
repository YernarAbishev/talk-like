from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserRegistrationForm, AddPostForm, ProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Post, Profile

def home(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('logIn')
    else:
        form = UserRegistrationForm()

    return render(request, "home.html", {
        'form': form
    })

def logIn(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("explore")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "login.html", {
        "form": form
    })

def logoutUser(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("logIn")

def explore(request):
    posts = Post.objects.all().order_by('-postDate')
    return render(request, "pages/explore.html", {
        'posts': posts
    })

def postDetails(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "pages/post-details.html", {
        'post': post
    })

def addPost(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.userPost = request.user

            form.save()
            return redirect('explore')
    else:
        form = AddPostForm()
    return render(request, "pages/add-post.html", {
        'form': form
    })

def deletePost(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user == post.userPost:
        if request.method == 'POST':
            Post.objects.filter(pk=pk).delete()
            return redirect('explore')

    return render(request, "pages/delete-post.html", {
        'post': post
    })

def postEdit(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'pages/edit-post.html', {
        'post': post
    })

def postUpdate(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.content = request.POST.get('content')
        post.save()

    return redirect('postDetails', pk=post.pk)

def userProfile(request):
    profile = ProfileForm(instance=request.user)
    return render(request, "pages/profile.html", {
        'profile': profile
    })