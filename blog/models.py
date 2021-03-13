from django.db import models
from django_editorjs import EditorJsField
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    Sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=150)
    author = models.CharField(max_length=20)
    content = RichTextField(blank=True,null=True)
    category = models.CharField(max_length=20,default='PC Games')
    timestamp = models.DateTimeField(blank=True)
    featureimg = models.ImageField(upload_to='post/featureimg', max_length=500)

    def __str__(self):
        return self.title + ' By ' + self.author
    