from django.shortcuts import render,redirect, HttpResponseRedirect
from .models import *
from .forms import LoginForm, PostForm, SignUpForm, editprofileform, PostComment, postcommentform
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages 
from django.shortcuts import render
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

#all post home
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'app/post_list.html',{'posts':posts})

#show post in details
def post_detail(request, slug):
    posts = Post.objects.filter(slug=slug).first()
    comments = PostComment.objects.filter(post=posts,reply=None).order_by('-id')
    
    if request.method == 'POST':
        comment_form = postcommentform(request.POST or None)
        if comment_form.is_valid():
            comment = request.POST.get('comment')
            reply_id = request.POST.get('comment_id')
            comment_qs = None 
            if reply_id:
                comment_qs = PostComment.objects.get(id=reply_id)
            content = PostComment.objects.create(post=posts,user= request.user, comment=comment,reply=comment_qs)
            content.save()
            # return HttpResponseRedirect(post.get_absolute_url())
            #return HttpResponseRedirect(reverse('/post_detail/', args=[slug]))
            # return redirect("post",slug=slug)
            return redirect('app:post_detail' ,slug=slug )
    else:
        comment_form = postcommentform()
    context = {
        'post':posts,  
        'comments':comments, 
        'comment_form':comment_form
        }
    return render(request, 'app/post_detail.html', context)
    
    
#add a new post 
def post_new(request):
    # if not request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST,request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('/',slug=post.slug)
        else:
            form = PostForm()
        return render(request, 'app/post_edit.html', {'form': form})
    # else:
    #     return redirect('/')
        

#edit post
def post_edit(request,slug):
    post = get_object_or_404(Post,slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/' ,slug=slug)
            # return redirect('/' ,slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'app/post_edit.html', {'form': form})


# add category 
def category_list(request):
    category = Category.objects.all()
    return render(request,'app/category_list.html',{'categories':category})

def category_detail(request,slug):
    categorydetails = get_object_or_404(Category,slug=slug)
    post = Post.objects.filter(category = categorydetails)
    return render(request, 'app/category_detail.html', {'cat': post})

def tag_list(request):
    # tag = Tag.objects.all()
    tag=Tag.objects.all()
    return render(request, 'app/tag_list.html',{'tags':tag})

def tag_detail(request,slug):
    tagdetails = get_object_or_404(Tag,slug=slug)
    post=Post.objects.filter(tag=tagdetails)
    return render(request,'app/tag_detail.html',{'cat':post})


#signup form
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            messages.success(request,"Register successfully....")
            form.save()
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request,'app/signup_form.html',{'form':form})





#login form 
def login_view(request):
    if not request.user.is_authenticated:
        if request.method ==  'POST':
            fm = LoginForm(request=request,data=request.POST)
            # fm = AuthenticationForm(request= request, data= request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname, password= upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully....')
                    return HttpResponseRedirect('/')
        else:
            fm= LoginForm()
            # fm = AuthenticationForm()
        return render(request,'app/login_view.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

#user profile
def profile(request):
    return render(request,'app/profile.html',{})


#user profile update
def profile_update(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = editprofileform(request.POST,request.FILES, instance = request.user)
            if fm.is_valid():
                messages.success(request, 'Profile updated successsfully....')
                fm.save()
                return HttpResponseRedirect('/profile/')
                #return redirect('/profile_view/')
        else:
            fm = editprofileform(instance = request.user)
        return render(request, 'app/profileupdate.html',{'name':request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login_view/')
        #fm = editprofileform(instance = request.user)
    #return render(request, 'app/profileupdate.html',{'name':request.user,'form':fm})


#logout 
def logout_view(request):
    logout(request)
    #messages.success(request,'successfully logout...')
    return HttpResponseRedirect('/')
    
   

