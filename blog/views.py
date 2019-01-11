from django.shortcuts import render, redirect
from blog.models import BlogArticles
from blog.forms import BlogArticlesForm
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def blog(request):
    entries = BlogArticles.objects.filter(publish=True)
    return render(request, 'blog.html', {'entries': entries})

def contacts(request):
    return render(request, 'contacts.html', {})


def article_details(request, slug):
    article = get_object_or_404(BlogArticles, slug=slug)
    #article = BlogArticles.objects.get(slug=slug)
    return render(request, 'article_details.html', {'article':article})


class DASH(ListView):
    model = BlogArticles
    template_name = 'dash.html'

#@user_passes_test(lambda u: u.is_superuser, login_url='login')
def another_one(request):
    if request.method == 'POST':
        form = BlogArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('done')

    else:
        form = BlogArticlesForm()
    return render(request, 'another_one.html', {'form':form})

def done(request):
    return render(request, 'done.html', {})