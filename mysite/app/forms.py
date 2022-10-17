from curses import meta
from dataclasses import fields
#from pyexpat import model
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


  

class PostForm(forms.ModelForm):    
    class Meta:
        model = Post
        fields = ('feature_image','title', 'text','category','thumb_image','tag')
       

class categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name',)

class tagform(forms.ModelForm):
    class Meta:
        model = Tag 
        fields = ('tag_name',)


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = get_user_model()
        fields = ('username','name', 'email', 'password1', 'password2','city',
        'mobile','profile_image','state','country','gender' )

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Eamil/Username')
    password = forms.CharField(widget=forms.PasswordInput)

class editprofileform(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','name','email','city','mobile','profile_image','state','country',
                'gender']

class postcommentform(forms.ModelForm):
    comment = forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control','placeholder':'text goes here...','rows':'2','cols':'30'}))
    class Meta:
        model = PostComment
        fields = ('name','email','comment')