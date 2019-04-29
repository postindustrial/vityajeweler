from django.conf import settings
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Page(models.Model):

    class Meta:
        abstract = True

    seo_title = models.CharField(max_length=200, blank=True, null=True, verbose_name="Тег Title")
    seo_description = models.CharField(max_length=300, blank=True, null=True, verbose_name="Тег Description")
    seo_h1 = models.CharField(max_length=200, blank=True, null=True, verbose_name="Тег H1")
    seo_keywords = models.CharField(max_length=200, blank=True, null=True, verbose_name="Тег Keywords")
    slug = models.SlugField(max_length=50, unique=True, default="slug", verbose_name="URL")

    def __str__(self):
        return self.name

class RealPage(Page):
    content = RichTextField(default="content", verbose_name="Содержимое страницы")

    def __str__(self):
        return self.seo_title

class Theme(Page):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True, default="slug", verbose_name="URL")

    def __str__(self):
        return self.name

class Post(Page):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    theme = models.ManyToManyField(Theme, help_text="Выберите тему этой статьи", verbose_name="Темы статьи")
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name="Название статьи (для людей)")
    preview = models.TextField(default="Еще одна отличная статья...", verbose_name="Описание для анонса статьи")
    content = RichTextField(default="content", verbose_name="Содержимое статьи")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    top = models.BooleanField(default=False, verbose_name="Лучший пост?")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
