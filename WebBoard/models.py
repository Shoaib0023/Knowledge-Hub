from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from markdown import markdown

class Topic(models.Model):
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.subject

class Post(models.Model):
    message = models.CharField(max_length=2000)
    topic = models.ForeignKey(Topic, related_name="posts", null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.message

    def get_message_as_markdown(self):
        return mark_safe(markdown(self.message, safe_mode='escape'))

class ReplyPost(models.Model):
    reply = models.CharField(max_length=2000)
    post = models.ForeignKey(Post, related_name="reply", null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.reply

    def get_reply_as_markdown(self):
        return mark_safe(markdown(self.reply, safe_mode='escape'))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    about = models.CharField(max_length=1000, blank=True, default="")
    hobbies = models.CharField(max_length=1000, blank=True, default="")
    image = models.ImageField(null=True, blank=True, upload_to="images")

    def __str__(self):
        return self.user.username
