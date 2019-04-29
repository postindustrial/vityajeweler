from django.conf import settings
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

BANNER_PLACE = (
    ("head", "Код внутри <head>"),
    ("body_bottom", "Код перед закрывающим тегом <body>"),
    ("sidebar_left", "Баннер в левом сайдбаре"),
    ("sidebar_right", "Баннер в правом сайдбаре"),
    ("footer", "Баннер в футере"),
)

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

class Banner(models.Model):
    name = models.CharField(max_length=200)
    place = models.CharField(
        "Расположение", max_length=40, choices=BANNER_PLACE, default="body_bottom"
    )
    content = models.TextField(default="Здесь могла быть ваша реклама...", verbose_name="Вставьте сюда содержимое баннера")

    def __str__(self):
        return self.name
