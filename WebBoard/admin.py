from django.contrib import admin
from . models import Topic, Post, ReplyPost, Profile


class PostAdmin(admin.ModelAdmin):
    list_display = ('message','created_by', 'created_at', 'like')

class ReplyPostAdmin(admin.ModelAdmin):
    list_display = ('reply', 'created_by', 'created_at')

admin.site.register(Topic)
admin.site.register(Post, PostAdmin)
admin.site.register(ReplyPost, ReplyPostAdmin)
admin.site.register(Profile)
