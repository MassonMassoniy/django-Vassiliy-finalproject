from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='Пользователь создавший пост', null=True,blank=True)
    title=models.CharField(verbose_name='Заголовок',max_length=255,default='',null=True,blank=True)
    text=models.TextField(verbose_name='Описание')
    date_post=models.DateTimeField(default=timezone.now,verbose_name='Дата создания поста')

    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'

    def __str__(self) -> str:
        return self.title

class AboutUs(models.Model):
    wat_url = models.URLField(verbose_name=('Whatsapp ссылка'))
    wat_txt = models.TextField(verbose_name=('Имя контакта'))
    tg_url = models.URLField(verbose_name=('Telegram ссылка'))
    tg_txt = models.TextField(verbose_name=('Имя контакта'))
    about_txt = models.TextField(verbose_name=('Информационный текст'))

    class Meta:
        verbose_name='About'
        verbose_name_plural='About'

    def __str__(self):
        return self.about_txt

# Create your models here.
