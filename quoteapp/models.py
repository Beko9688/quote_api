from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Quotes(models.Model):
    quote = models.TextField(verbose_name='Цитата', blank=True, unique=True)
    author = models.CharField(verbose_name='Автор', max_length=50)
    created_at = models.DateTimeField(verbose_name='Дата создание', auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.quote

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'
