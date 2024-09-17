from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class CategoryList(APIView):
    @staticmethod
    def get(request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class ProductList(APIView):
    @staticmethod
    def get(request):
        queryset = Product.objects.all().order_by('-create_time')
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class BestProduct(APIView):
    @staticmethod
    def get(request):
        queryset = Product.objects.all().order_by('-buy_count')
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class SlideList(APIView):
    @staticmethod
    def get(request):
        queryset = Slide.objects.all().order_by('-create_time')
        serializer = SlideSerializer(queryset, many=True)
        return Response(serializer.data)


class DigiServiceList(APIView):
    @staticmethod
    def get(request):
        queryset = Digikala_Services.objects.all().order_by('-create_time')
        serializer = DigiServiceSerializer(queryset, many=True)
        return Response(serializer.data)


class OfferPackList(APIView):
    @staticmethod
    def get(request):
        queryset = OfferPack.objects.all()
        serializer = OfferPackSerializer(queryset, many=True)
        return Response(serializer.data)


class NewsList(APIView):
    @staticmethod
    def get(request):
        queryset = News.objects.all().order_by('-create_time')
        serializer = NewsSerializer(queryset, many=True)
        return Response(serializer.data)
