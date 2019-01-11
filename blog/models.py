from django.db import models
from  django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField 
# Create your models here.


class BlogArticles(models.Model):

    title = models.CharField(max_length=20)
    content = RichTextUploadingField()
    timestamp = models.DateField(auto_now_add=True)
    tags = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    publish = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title