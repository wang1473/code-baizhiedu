from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class UserInto(AbstractUser):
    phone = models.CharField(max_length=11, unique=True)
    user_head = models.ImageField(upload_to='user', blank=True, null=True, verbose_name='用户头像')

    class Meta:
        db_table = 'bz_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
