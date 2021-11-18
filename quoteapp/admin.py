from django.contrib import admin
from .models import Quotes, Category


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['quote', 'author', 'created_at']
    list_filter = ['quote', 'author', 'created_at']


admin.site.register(Quotes)
admin.site.register(Category)
