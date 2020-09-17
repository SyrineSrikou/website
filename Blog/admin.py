from django.contrib import admin

from .models import BlogPost, Comment

class CommentAdmin(admin.ModelAdmin):
    list_display=('id','name','email','message','date','blogpost')

admin.site.register(Comment, CommentAdmin)
admin.site.register(BlogPost)
