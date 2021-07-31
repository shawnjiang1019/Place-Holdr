from django.db import models
from django.db.models.fields import TextField

# Create your models here. Keeps data base all the infor mation sucas emails, name, password

from django.utils import timezone

from django.contrib.auth.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    text = models.CharField(max_length= 300)
    date_posted = models.DateTimeField(default = timezone.now)

class Post(models.Model):
    content = models.TextField(blank = False, null = False)
    date_posted = models.DateTimeField(default = timezone.now)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    likes_count = models.DecimalField(decimal_places=0, max_digits=1000, default= 0)
    likes = models.ManyToManyField(User, related_name="blog_likes")
    comments = models.ManyToManyField(Comment, related_name = 'comments')
    comments_count = models.DecimalField(decimal_places= 0, max_digits=1000, default= 0)
    event = models.TextField(blank = False, null = False, default= "Demo")
    date = models.TextField(blank= False, null = False, default= "Unknown")
    place = models.TextField(blank= False, null = False, default= "Unknown")

    
    




