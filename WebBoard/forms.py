from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Post, Topic, ReplyPost, Profile
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    email = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']


class ProfileForm(ModelForm):
    about = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Profile
        fields = ['about', 'hobbies', 'image']

class AskQuestionForm(ModelForm):
    message = forms.CharField(widget=forms.Textarea)
    tag = forms.ModelChoiceField(queryset=Topic.objects.all())

    class Meta:
        model = Post
        fields = ('message', 'tag')

class ReplyPostForm(ModelForm):
    reply = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ReplyPost
        fields = ['reply']

class ProfileEditForm(ModelForm):
    about = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Profile
        fields = ('about', 'hobbies', 'image')
