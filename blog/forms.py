from django import forms
from django.forms import ModelForm
from blog.models import BlogArticles
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class BlogArticlesForm(ModelForm):

    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = BlogArticles
        fields = ['title', 'title_image', 'content', 'tags', 'publish']