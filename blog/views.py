from django import urls
from django.http import request
from django.shortcuts import render, redirect
from .form import *
from newsapi import NewsApiClient
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

# Create your views here.
def home(request):
    if(request.user.is_authenticated):
        return redirect('news/')
    else:
        context = {'blogs' : BlogModel.objects.all()}
        return render(request,'home.html', context)

def login_view(request):
    if (request.user.is_authenticated):
        return redirect('/')
    return render(request, 'login.html')

def signup_view(request):
    if (request.user.is_authenticated):
        return redirect('/')
    return render(request , 'signup.html')

def allBlog(request):
    context = {'blogs' : BlogModel.objects.all()}
    return render(request,'home.html', context)

@login_required(login_url='/login/')
def news(request):
    newsapi = NewsApiClient(api_key="834eefe8c49440ea805293d60b99a22e")
    topheadlines = newsapi.get_top_headlines(language="en", country="in", page_size=100)
    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    urls = []
    published_at = []
    author= []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        urls.append(myarticles['url'])
        published_at.append(myarticles['publishedAt'])
        author.append(myarticles['author'])
    mylist = zip(news, desc, urls, published_at, author, img)
    return render(request, 'news.html', context={"mylist": mylist})




@login_required(login_url='/login/')
def add_blog(request):
    context = {'form': BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']
            BlogModel.objects.create(
                user = user , title = title, 
                content = content, image = image
            )
            return redirect('/add_blog/')

    except Exception as e:
        print(e)
    return render(request, 'blog.html', context)

def details(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug = slug).first()
        context['blog_obj'] =  blog_obj
    except Exception as e:
        print(e)
    return render(request , 'details.html' , context)

@login_required(login_url='/login/')
def view_blog(request):
    context = {}
    try:
        blog_objs = BlogModel.objects.filter(user = request.user)
        context['blog_objs'] =  blog_objs
    except Exception as e: 
        print(e)
    
    print(context)
    return render(request , 'viewBlog.html' ,context)

@login_required(login_url='/login/')
def update(request, slug):
    context = {}
    try:
        
        blog_obj = BlogModel.objects.get(slug = slug)
       
        
        if blog_obj.user != request.user:
            return redirect('/')
        
        initial_dict = {'content': blog_obj.content}
        form = BlogForm(initial = initial_dict)

        if request.method == 'POST':
            form = BlogForm(request.POST)
            
            title = request.POST.get('title')
            user = request.user
            
            if form.is_valid():
                content = form.cleaned_data['content']
            
            blog_obj = BlogModel.objects.update(
                user = user , title = title, 
                content = content
            )
        
        context['blog_obj'] = blog_obj
        context['form'] = form
    except Exception as e :
        print(e)

    return render(request , 'update.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')


def delete(request, id):
    try:
        blog_obj = BlogModel.objects.get(id = id)
        
        if blog_obj.user == request.user:
            blog_obj.delete()
        
    except Exception as e :
        print(e)

    return redirect('/view_blog/')