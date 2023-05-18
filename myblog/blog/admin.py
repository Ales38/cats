from django.contrib import admin
from .forms import PostForm
from .models import Post,Comments
# Register your models here.

admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'post')



