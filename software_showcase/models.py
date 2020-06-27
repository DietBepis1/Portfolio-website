from django.db import models

# Create your models here.
class ShowcaseItem(models.Model):
    """Holds info for showcase cards on main page"""

    title = models.CharField(max_length=50)
    path_to_site = models.URLField(blank=True)
    path_to_git = models.URLField(blank=True)
    pic = models.ImageField(default='', upload_to='gallery')
    text = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)


class AboutMe(models.Model):
    """Holds info for the 'about me page'"""

    pic = models.ImageField(default='', upload_to='gallery')
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    sw_langauges = models.CharField(max_length=100)
    schooling = models.CharField(max_length=100)
    blurb = models.CharField(max_length=1000)
    contact = models.CharField(max_length=1000)
    resume = models.FileField(upload_to='documents')
