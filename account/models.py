from django.db import models
from django.contrib.auth.models import User

# Model for user profiles
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name='User Object')
    bio = models.TextField(null=True, blank=True)
    profile_img = models.ImageField(default='user.png', upload_to='profile_images', blank=True, null=True, verbose_name='Profile Image')
    location = models.CharField(max_length=100, null=True, blank=True)
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    gender = models.CharField(max_length=10, null=True, blank=True, choices=GENDER)
    
    def __str__(self):
        return self.user.username

    @property    
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'