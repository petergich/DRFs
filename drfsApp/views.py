from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *


@api_view(['GET'])
def products(request):
    products = product.objects.all()
    serializedProducts = productSerializer(products,many = True)
    return Response(serializedProducts.data)

# Create your views here.
