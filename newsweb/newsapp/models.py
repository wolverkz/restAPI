from django.db import models


class Newsletter(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    desc = models.TextField(max_length=250)
    issue_number = models.IntegerField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='articles', on_delete=models.CASCADE)
    newsletter = models.ForeignKey('Newsletter', related_name='articles', on_delete=models.CASCADE, default=1)
    image = models.ImageField(allow_empty_file=True)