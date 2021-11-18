from rest_framework import serializers
from .models import Quotes, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class QuoteSerializer(serializers.ModelSerializer):

    # category = CategorySerializer()

    class Meta:
        model = Quotes
        fields = '__all__'
