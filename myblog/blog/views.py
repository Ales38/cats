from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.template.context_processors import request


from django.views.generic.base import View
from .forms import CommentsForm, PostForm, BlogForm
from .models import Post, Comments
from django.views.generic import DetailView, CreateView


class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog.html', {'post_list': posts})


class PostDetail(View):
    def get(self, request, pk):
        comments = Comments.objects.all()
        post = Post.objects.get(id=pk)
        return render(request, 'blog/blog_detail.html', {'post': post, 'comments': comments})


class AddComments(View):
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            # form.instance.name = request.user
            form.post_id = pk
            form.save()
            return redirect(f'/{pk}')


def create(request):  # добавление поста
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            'Фоpма введена не верно'
    form = PostForm
    data = {'form': form, 'error': error}
    return render(request, 'blog/create.html', data)


def Register(request):  # регистрация
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

        username = form.cleaned_data.get('username')
        my_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=my_password)
        login(request, user)
        return redirect('/')

    else:
        form = UserCreationForm()
        return render(request, 'blog/register.html', {'form': form})


class LoginPage(LoginView):  # страница авторизации
    template_name = 'blog/login.html'
    redirect_authenticated_user = 0


class MyLogout(LogoutView):
    next_page = '/'


def DelComment(request, pk):
    comment = Comments.objects.get(id=pk)
    pk = comment.post.pk
    if request.method == "POST":
        comment.delete()
        return redirect(f'/{pk}')
    context = {'comment': comment, 'pk': pk}
    return render(request, 'blog/del.html', context)


def index(request):
    task = Post.objects.all()
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'task': task, 'form': form}
    return render(request,'blog/index.html',context)



