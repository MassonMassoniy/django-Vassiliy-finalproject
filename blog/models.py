from django.db import models
from django.conf import settings
from django.utils import timezone
from .managers import UserManager
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.utils import timezone
from django.contrib.auth.hashers import make_password

class User(AbstractBaseUser, PermissionsMixin):
    ADMIN, SELLER, COURIER, ASSEMBLER, CUSTOMER=range(1,6)

    ROLE_TYPES=(
        (ADMIN,'Администратор'), #1
        (SELLER,'Продавец'),              #2
        (COURIER,'Курьер'),               #3
        (ASSEMBLER,'Сборщик'),            #4
        (CUSTOMER,'Покупатель')              #5
    )

    objects=UserManager()

    id = models.AutoField(primary_key=True)
    username = models.CharField('Логин', max_length=50, default='', unique=True)
    first_name = models.CharField("ФИО",max_length=100, default='', blank=True,null=True)
    email=models.EmailField("Почта",default="email@mail.com",blank=True,null=True)
    role=models.IntegerField(verbose_name='Роль',default=CUSTOMER,choices=ROLE_TYPES)
    date_joined=models.DateTimeField("Дата присоединения",blank=True,null=True,default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(
        default=True,
        verbose_name='Статус доступа',
    )

    USERNAME_FIELD="username"
    REQUIRED_FIELDS=[]

    def save(self, *args, **kwargs):
        # Если пароль не хэширован, то хэшируем его перед сохранением
        if not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Пользователь создавший пост', null=True,blank=True, related_name='posts')
    title=models.CharField(verbose_name='Заголовок',max_length=255,default='',null=True,blank=True)
    text=models.TextField(verbose_name='Описание')
    date_post=models.DateTimeField(default=timezone.now,verbose_name='Дата создания поста')

    class Meta:
        verbose_name='Пост'
        verbose_name_plural='Посты'

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
