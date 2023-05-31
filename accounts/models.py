from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self,email,password=None,**extra_fields):

        if not email:
            raise ValueError ('User must have an email')

        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password,**extra_fields):

        user = self.create_user(email,password)
        user.is_staff=True
        user.is_superuser =True
        user.save(using=self._db)
        return user


class CustomUserModel(AbstractBaseUser):

    email   = models.EmailField(max_length=254,unique=True)
    name    = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False)

    objects  = CustomUserManager()
    USERNAME_FIELD  = 'email'


    def __str__(self):
        return self.name

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, perm, obj=None):
        return self.is_staff

    class Meta:
      verbose_name = ("User")
      verbose_name_plural = ("Users")
