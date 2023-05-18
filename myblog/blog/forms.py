from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Comments, Post
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from django.contrib.auth.forms import UserCreationForm

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name','email','text_comments')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','discriptions')
    

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class BlogForm(forms.ModelForm):
    class Meta:
      model =Post
      fields = ('title','discriptions')

