from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductList.as_view(), name='products'),
    path('slides/', SlideList.as_view(), name='slides'),
    path('service/', DigiServiceList.as_view(), name='digi_service'),
    path('offerspack/', OfferPackList.as_view(), name='offers'),
    path('category/', CategoryList.as_view(), name='category'),
]
