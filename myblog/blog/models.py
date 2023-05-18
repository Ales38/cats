from django.db import models
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

class Comments(models.Model):#коментарии
   post=models.ForeignKey(Post, on_delete=models.CASCADE)
   email = models.EmailField()
   name = models.CharField('Имя',max_length=50)
   text_comments = models.TextField('Текст комментария',max_length=500)
   post = models.ForeignKey(Post, verbose_name='Статья',on_delete=models.CASCADE)
   def __str__(self):
      return f'{self.name},{self.post}'
   class Meta:
      verbose_name = 'комментарий'
      verbose_name_plural = 'комментарии'



#class Blog(models.Model):
 #  title = models.CharField('Заголовок',max_length=50)
  # text = models.TextField('Описание', blank=True)
#
   #def __str__(self):
    #  return f'{self.title}',f'{self.text}'
   #class Meta:
      #verbose_name = 'Пост '
      #verbose_name_plural= 'Посты'









