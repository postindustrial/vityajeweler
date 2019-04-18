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

class Theme(Page):
    name = models.CharField(max_length=200)
    preview = models.TextField(default="Очередная ненужная тематика...", verbose_name="Краткое описание тематики")

    def __str__(self):
        return self.name

class Company(Page):
    name = models.CharField(max_length=200)
    preview = models.TextField(default="Еще одна рекламная система...", verbose_name="Краткое описание рекламной системы")

    def __str__(self):
        return self.name

class Place(Page):
    theme = models.ManyToManyField(Theme, help_text="Выберите тематику площадки", verbose_name="Тематика площадки")
    company = models.ManyToManyField(Company, help_text="Выберите поставщика рекламы", verbose_name="Поставщик рекламы")
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name="Название площадки")
    preview = models.TextField(default="Еще одна сомнительная площадка...", verbose_name="Краткое описание площадки")
    content = RichTextField(default="content", verbose_name="Комментарий о площадке")

    def __str__(self):
        return self.name
