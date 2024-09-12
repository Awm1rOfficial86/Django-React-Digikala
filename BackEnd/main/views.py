from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import *
from main.serializers import ProductSerializer


class ProductList(APIView):
    @staticmethod
    def get(request):
        queryset = Product.objects.all().order_by('-create_time')
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
