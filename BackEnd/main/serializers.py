from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class SlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = ['name', 'url', 'image']


class DigiServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = ['name', 'url', 'image']


class OfferPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferPack
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
