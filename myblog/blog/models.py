from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete
from django.conf import settings
from django.utils.text import slugify
from django.dispatch import receiver


User =settings.AUTH_USER_MODEL

@receiver(pre_save,sender=User)
def user_pre_save_receiver(sender, instance, *args, **kwargs):#выполнение опред.действий перед сохранением обьекта модели в бд
   print(instance.username, instance.id)
   #instance.save()вызывает сохранение снова и снова и снова
@receiver(post_save,sender=User)
def user_post_save_receiver(sender, instance, created, *args, **kwargs):
   #print(args,kwargs)
   if created:
       print("создан пользователь!", instance.username)
   else:
      print(instance.username,"Был только что сохранен!")

@receiver(post_delete,sender=User)
def user_post_delete(sender,instance,*args,**kwargs):
   print(instance.username,"Пользователь успешно удален!")



class Post(models.Model):
   ''' данные поста'''
   title = models.CharField('Заголовок записи',max_length=50)
   discriptions = models.TextField('Текст записи')
   date = models.DateField(auto_now_add=True)
   author = models.CharField(blank=True,max_length=100)
   image = models.ImageField('Фото',upload_to='images/%Y', blank=True)
   def __str__(self):
      return f'{self.title},{self.author}'
   class Meta:
       verbose_name = 'Запись'
       verbose_name_plural = 'Записи'


def save_post(sender,instance, **kwargs):
   print("Пост добавлен!")

def delete_post(sender,instance,**kwargs):
   print("Пост удален!")

pre_save.connect(save_post,sender=Post)#выполнение опред.действий перед сохранением обьекта модели в бд
post_save.connect(save_post,sender=Post)#после сохранения обьекта модели в бд
post_delete.connect(delete_post,sender=Post)



class Comments(models.Model):#коментарии
   post=models.ForeignKey(Post, on_delete=models.CASCADE)
   email = models.EmailField()
   name = models.CharField('Имя',max_length=50)
   text_comments = models.TextField('Текст комментария',max_length=500)

   def __str__(self):
      return f'{self.name},{self.post}'
   class Meta:
      verbose_name = 'комментарий'
      verbose_name_plural = 'комментарии'



