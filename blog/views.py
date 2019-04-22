from django.shortcuts import render, redirect
from blog.models import BlogArticles
from blog.forms import BlogArticlesForm
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import user_passes_test



def home(request):
    return render(request, 'home.html', {})


def blog(request):
    entries = BlogArticles.objects.filter(publish=True).order_by('-timestamp')
    return render(request, 'blog.html', {'entries': entries})

def contacts(request):
    return render(request, 'contacts.html', {})


def article_details(request, slug):
    article = get_object_or_404(BlogArticles, slug=slug)

    full_path = request.build_absolute_uri() 
    url = request.get_host()
    context = {
        'article':article,
        'full_path': full_path,
        'url': url
    }
    return render(request, 'article_details.html', context)

@user_passes_test(lambda u: u.is_superuser, login_url='login')
def DASH(request):

    articles = BlogArticles.objects.all().order_by('-timestamp')
    return render(request, 'dash.html', {'articles': articles})


@user_passes_test(lambda u: u.is_superuser, login_url='login')
def another_one(request):
    if request.method == 'POST':
        form = BlogArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dash')

    else:
        form = BlogArticlesForm()
    return render(request, 'another_one.html', {'form':form})
    

@user_passes_test(lambda u: u.is_superuser, login_url='login')
def edit_article(request, slug=None):
    article = get_object_or_404(BlogArticles, slug=slug)
    form = BlogArticlesForm(request.POST or None, instance=article)

    if form.is_valid():
        form.save()
        return redirect('dash')
    return render(request, 'another_one.html', {'form':form})