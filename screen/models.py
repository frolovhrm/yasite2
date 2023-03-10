from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=50, null=False, unique=True, )
    email = models.EmailField(null=False, )
    phone = models.CharField(max_length=12)


class Cars(models.Model):
    id = models.ForeignKey(User, on_delete=models.PROTECT, primary_key=True, unique=True)
    name = models.CharField(max_length=20)


class Screen(models.Model):
    id = models.ForeignKey(Cars, on_delete=models.PROTECT, primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    usable = models.BooleanField()
    readed = models.BooleanField()
    errors_log = models.CharField(max_length=30)
    strline = models.CharField(max_length=1000)
