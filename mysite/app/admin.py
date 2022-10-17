
from urllib import response
from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from .models import *
import csv
# from .forms import *

class PostAdmin(admin.ModelAdmin):
    list_dispaly =('author','title','text','category','feature_image','thumb_image')
    search_fields=('title',)
    list_filter = ['title']

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_dispaly =('category_name','slug')
    search_fields=('category_name',)
    list_filter = ['category_name']

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('tag_name',)}
    list_display = ('tag_name',)
    search_fields = ('tag_name',)
    list_filter = ('tag_name',)

class UserAdmin(admin.ModelAdmin):
    list_dispaly =['name','city','email','mobile','profile_image','state','country','gender']
    search_fields=('name',)
    list_filter = ['name']
    actions = ['export_to_csv']

    def export_to_csv(self,request,queryset):
        response = HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename="user.csv"'
        writer = csv.writer(response)
        writer.writerow(['Username','Password','Last Login','Superuser Status','Frist Name','Last Name','Staff Status','Date joined','Name','City','Email','Mobile','Profile Image','State','Country','Gender'])
        obj = queryset.values_list('username','password','last_login','is_superuser','first_name','last_name','is_staff','date_joined','name','city','email','mobile','profile_image','state','country','gender')
        for objs in obj:
            writer.writerow(objs)
        return response
    export_to_csv.short_description = 'Export to CSV'

   

class PostCommentAdmin(admin.ModelAdmin):
    list_display=('name','comment','user','post','reply','timestamp','email')
    search_fields= ('comment',)
    list_filter = ['name']

# Register your models here.
admin.site.register(Post,PostAdmin)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)

admin.site.register(User,UserAdmin)
admin.site.register(PostComment,PostCommentAdmin)



