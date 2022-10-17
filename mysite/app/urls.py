from django.urls import path
from .import views

app_name = 'app'

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('category/<slug:slug>/',views.category_detail, name='category_detail'),
    # path('category/<str:slug>/',views.category_detail, name='category_detail'),
    # path('post/<str:slug>/edit/', views.post_edit, name='post_edit'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    # path('post/<str:slug>', views.post_detail, name='post_detail'),
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
    
    path('category/',views.category_list,name='category_list'),
    
    path('signup_view/',views.signup_view,name='signup_view'),
    path('login_view/',views.login_view,name='login_view'),
    path('profile/',views.profile,name='profile'),
    path('profile_update/',views.profile_update,name='profile_update'),
    path('logout_view/',views.logout_view,name='logout_view'),

    path('tag/',views.tag_list, name='tag_list'),
    path('tag_detail/<slug:slug>/',views.tag_detail, name='tag_detail'),
   ]