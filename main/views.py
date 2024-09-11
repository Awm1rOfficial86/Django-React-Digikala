from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import *
from main.serializers import ProductSerializer


# Create your views here.

class ProductList(APIView):
    @staticmethod
    def get(request):
        all_products = Product.objects.all().order_by('-create_time')
        serializer = ProductSerializer(all_products, many=True)
        return Response(serializer.data)
