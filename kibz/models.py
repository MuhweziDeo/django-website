from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError('user requires an email')
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,name,password):
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save() 
        return user   

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=254,unique=True)
    name=models.TextField(max_length=30)
    is_staff=models.BooleanField(default=False)
    REQUIRED_FIELDS=['name']
    USERNAME_FIELD='email'
    objects=UserManager()

    def __str__(self):
        return self.email

class Post(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    created_on=models.DateField(auto_now=True)
    post_image_1=models.ImageField(upload_to='post_images')
    post_image_2=models.ImageField(upload_to='post_images')
    post_image_3=models.ImageField(upload_to='post_images')
    post_image_4=models.ImageField(upload_to='post_images')
    post_image_5=models.ImageField(upload_to='post_images')
    post_image_6=models.ImageField(upload_to='post_images')

    def __str__(self):
        return self.title
class TeamProfile(models.Model):
    name=models.CharField(max_length=100)
    position=models.CharField(max_length=200)
    description=models.TextField(max_length=500)
    profile=models.ImageField(upload_to='profile_images')
    facebook=models.URLField(blank=True)
    twitter=models.URLField(blank=True)
    instagram=models.URLField(blank=True)
    linkedin=models.URLField(blank=True)
    created_on=models.DateField(auto_now=True)    

    def __str__(self):
        return self.name

class Artist(models.Model):
    name=models.CharField(max_length=200)
    profile_photo=models.ImageField(upload_to='artist_profile',blank='True',default=None)
    position=models.CharField(max_length=100,default='artist')
    bio=models.TextField(max_length=500)
    genre=models.CharField(max_length=100)
    facebook=models.URLField(blank=True)
    twitter=models.URLField(blank=True)
    instagram=models.URLField(blank=True)
    linkedin=models.URLField(blank=True)
    youtube=models.URLField(blank=True)
    music_link=models.URLField(blank=True)
    created_on=models.DateField(auto_now=True)
    image_1=models.ImageField(upload_to='artist_images',default='me.jpg',blank=True, null=True)
    image_2=models.ImageField(upload_to='artist_images',default='me.jpg',blank=True, null=True)
    image_3=models.ImageField(upload_to='artist_images',default='me.jpg',blank=True, null=True)
    image_4=models.ImageField(upload_to='artist_images',default='me.jpg',blank=True, null=True)
    image_5=models.ImageField(upload_to='artist_images',default='me.jpg',blank=True, null=True)
 

    def __str__(self):
    	return self.name



class Client(models.Model):
	name=models.CharField(max_length=100)
	logo=models.ImageField(upload_to="client_logo")
	client_website=models.URLField(blank=True)

	def __str__(self):
		return self.name

class CompanyGallery(models.Model):
    title=models.CharField(max_length=100)
    image_1=models.ImageField(upload_to='post_images')
    image_2=models.ImageField(upload_to='post_images')
    image_3=models.ImageField(upload_to='post_images')
    image_4=models.ImageField(upload_to='post_images')
    image_5=models.ImageField(upload_to='post_images')
    image_6=models.ImageField(upload_to='post_images')

    def __str__(self):
        return self.title

class Video(models.Model):
    title=models.CharField(max_length=100)
    video_1=models.URLField(max_length=500)
    video_2=models.URLField(max_length=500)
    video_3=models.URLField(max_length=500)

    def __str__(self):
        return self.title