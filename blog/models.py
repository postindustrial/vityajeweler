from django.conf import settings
from django.db import models
from django.utils import timezone

class Theme(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    theme = models.ManyToManyField(Theme, help_text="Выберите тему этой статьи")
    title = models.CharField(max_length=200)
    slink = models.CharField(max_length=200, default="slink")
    preview = models.TextField(default="Еще одна отличная статья...")

    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
