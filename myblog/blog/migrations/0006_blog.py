# Generated by Django 4.2 on 2023-05-13 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_author_alter_post_date_alter_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('text', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Пост ',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]