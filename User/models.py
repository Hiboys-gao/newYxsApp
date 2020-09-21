from django.db import models

# Create your models here.

class Users(models.Model):
    u_name=models.CharField(max_length=32)
    u_password=models.CharField(max_length=128)
    u_mail=models.CharField(max_length=32)
    u_icon=models.ImageField(upload_to='icons')
    u_tokon=models.CharField(max_length=128)
    u_active=models.BooleanField(default=False)

    class meta():
        db_table='users'