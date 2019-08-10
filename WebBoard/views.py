from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from . models import Post, Topic, ReplyPost, Profile
from . forms import AskQuestionForm, ReplyPostForm, ProfileEditForm, \
                    SignUpForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# for signup (urlname:signup)
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()      # cleaned_data is generated only after the form wills save.
            username = form.cleaned_data.get("username")
            password1 = form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=password1)
            profile = Profile.objects.create(user=user)
            profile.save()
            login(request, user)
            return redirect("allposts")
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form':form})

# for homepage (urlname:home)
def home(request):
    return render(request, 'home/home.html')

def auth_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('allposts')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


# to display all post (urlname:allposts)
def all_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    topics = Topic.objects.all()

    paginator = Paginator(posts, 6) # Show 25 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    args = {
        'posts': posts,
        'topics':topics,
        'contacts': contacts
    }

    return render(request, "home/all_posts.html", args)

# to ask any question (urlname:askquestion)
@login_required(login_url='/accounts/login/')
def ask_question(request):
    if request.method == "POST":
        form = AskQuestionForm(request.POST)
        user = request.user

        if form.is_valid():
            post = form.save(commit=False)
            post.message = form.cleaned_data.get("message")
            post.topic = form.cleaned_data.get("tag")
            post.created_by = user
            post.save()

        return redirect("allposts")

    else:
        posts = Post.objects.all().order_by('-created_at')
        form = AskQuestionForm()
        args = {
            'posts': posts,
            'form': form
        }
        return render(request, "home/ask_question.html", args)

# to reply a post (urlname:replypost)
@login_required(login_url='/accounts/login/')
def reply_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = ReplyPostForm(request.POST)

        if form.is_valid():
            replypost = form.save(commit=False)
            replypost.reply = form.cleaned_data.get('reply')
            replypost.post = post
            replypost.created_by = request.user
            replypost.save()
            return redirect("post", post.id)

    else:
        form = ReplyPostForm()

    return render(request, 'home/replypost.html', {'form':form ,'post':post})


# for a particular post (urlname:post)
@login_required(login_url='/accounts/login/')
def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    replypost = ReplyPost.objects.filter(post=post)

    args = {
        'post': post,
        'replypost': replypost
    }

    return render(request, 'home/post.html', args)

# return post related to a particular topic (urlname=topicpostview)
def topicpostview(request, pk):
    topic = get_object_or_404(Topic, pk=pk)

    args = {
        'topic': topic
    }

    return render(request, 'home/topicpage.html', args)


@login_required(login_url='/accounts/login/')
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # to prepopulate the form .
    form = AskQuestionForm(request.POST or None, instance=post)
    if request.method == "POST":
        form.save()
        return redirect('post', post.id)

    return render(request, 'home/editpost.html', {'form':form})

def likefunc(request,pk):
    post = Post.objects.get(pk=pk)
    post.like += 1
    post.save()
    return HttpResponse(post.like)

def my_post(request):
    post = Post.objects.filter(created_by=request.user)
    args = {
        'posts':post
    }
    return render(request, 'home/myposts.html', args)

def most_viewed_post(request):
    posts = Post.objects.all().order_by('-views')
    args = {
        'posts':posts
    }
    return render(request, 'home/mostviewedpost.html', args)

# gives profile of a user (urlname:profile)
def profile(request, pk):
    user = User.objects.get(pk=pk)
    profile = Profile.objects.get(user=user)
    args = {
        'current_user': user,
        'profile': profile
    }
    return render(request, 'home/profile.html', args)

def edit_profile(request, pk):
    user = User.objects.get(pk=pk)
    profile = Profile.objects.get(user=user)
    if request.method == "POST":
        form = ProfileEditForm(request.POST ,  request.FILES , instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect("profile", user.id)
    else:
        form = ProfileEditForm(instance=profile)

    return render(request, 'home/editprofile.html', {'form':form, \
                                                         'current_user':user,
                                                         'profile':profile })
