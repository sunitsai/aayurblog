from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    c_name = models.CharField(max_length=200)

class Post(models.Model):
    cat_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    shortcontent = models.TextField(max_length=200)
    content = RichTextField()
    keyword = models.CharField(max_length=100)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=80)
    image = models.ImageField(upload_to="app/img",default="abc.jpg")
    authorimg = models.ImageField(upload_to="app/authorimg",default="abc.jpg")


class PostComment(models.Model):
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=80)
    Lastname = models.CharField(max_length=80)
    Email = models.CharField(max_length=80)
    Contact = models.BigIntegerField()
    post_date = models.DateTimeField(auto_now=True)
    comment = models.TextField()
    


class Seller(models.Model):
    Firstname = models.CharField(max_length=80)
    Lastname = models.CharField(max_length=80)
    Email = models.CharField(max_length=80)
    Contact = models.BigIntegerField()
    State = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Businessname = models.CharField(max_length=200)
    is_created = models.DateTimeField(auto_now_add=True)
