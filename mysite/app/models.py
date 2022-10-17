from email.policy import default
from enum import unique
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# from .manager import UserManager
from django.utils import timezone
from django.conf import settings

# from mysite.app.manager import UserManager


#abstractuser 
class User(AbstractUser):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=14)
    profile_image = models.ImageField(upload_to='profileimg',blank=True)
    state = models.CharField(max_length=100 )
    country = models.CharField(max_length=100)
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=gender_choices)
    
    def __str__(self):
        return self.name

   

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=255,unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=250,allow_unicode=True,unique=True,blank=True,null=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.category_name
    
    # def save(self, *args, **kwargs):
    #     value = self.title
    #     self.slug = slugify(value, allow_unicode=True)
    #     super().save(*args, **kwargs)


class Tag(models.Model):
    tag_name = models.CharField(max_length=255,unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=250,blank=True,null=True,allow_unicode=True,unique=True)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.tag_name
    
    # def save(self, *args, **kwargs):
    #     value = self.title
    #     self.slug = slugify(value, allow_unicode=True)
    #     super().save(*args, **kwargs)
  
    
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=200,allow_unicode=True,unique=True,blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True,related_name='posts')
    feature_image = models.ImageField(upload_to='featureimg/',blank=True,null=True)
    thumb_image = models.ImageField(upload_to='thumbimg/',blank=True,null=True)
    tag = models.ManyToManyField(Tag, related_name='posts',blank=True)


    def get_absolute_url(self):
        return reverse('app:post_detail',args=[self.slug])
        
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#comment    
class PostComment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    reply = models.ForeignKey('PostComment',on_delete=models.CASCADE, null=True,related_name='replies')
    timestamp = models.DateTimeField(auto_now_add=True)
    email= models.EmailField(max_length =100)
    def __str__(self):
        return str(self.comment)

    
    
    


