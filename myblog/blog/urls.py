from django.urls import path
from .views import *



urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('index/', index, name='index'),
    path('index/<int:pk>/', PostDetail.as_view()),
    path('review/<int:pk>/', AddComments.as_view(), name='add_comments'),
    path('create/', create, name='create'),
    path('login/',LoginPage.as_view(), name='login'),
    path('register/',Register, name='register'),
    path('/', MyLogout.as_view(), name='logout'),
    path('delete/<str:pk>/',DelComment,name='delete'),
]
