from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=122)
    email = models.EmailField()
    password = models.CharField(max_length=32)

    data_display = ("username", "email", "password",)
 

    def __str__(self):
        return self.username