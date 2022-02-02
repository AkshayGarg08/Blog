from django.db import models
from django.utils.html import format_html


# Create your models here.
class Category(models.Model):
    def __str__(self):
        return self.title
    
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def image_tag(self):
        return format_html('<img src= "/media/{}" style="width:36px; height:36px; border-radius:60%" />'.format(self.image))
        
    
    
class Post(models.Model):
    def __str__(self):
        return self.title
    
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField() 
    url = models.CharField(max_length=200)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    image  = models.ImageField(upload_to='post/')
    
    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:36px; height:36px; border-radius:60%" />'.format(self.image))
    
    
    
    
    
