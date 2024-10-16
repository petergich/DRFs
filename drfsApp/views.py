from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *


@api_view(['GET','POST'])
def products(request):
    if request.method == 'GET':
        products = product.objects.all()
        serializedProducts = productSerializer(products,many = True)
        return Response(serializedProducts.data)
    if request.method == 'POST':
        serializedProducts = creatProductListSerialiser(data =request.data)
        if serializedProducts.is_valid():
            created_products = []
            products = serializedProducts.validated_data['products']
            for product_data in products:
                if not category.objects.filter(id = product_data['category']).exists():
                    return Response("Category Not Found",status=status.HTTP_404_NOT_FOUND)
                product_category = category.objects.get(id = product_data['category'])
                created_product = product.objects.create(name = product_data["name"],price = product_data["price"],quantity = product_data['price'],category=product_category)
                created_products.append(created_product)
            return Response(productSerializer(created_products,many=True).data, status=status.HTTP_201_CREATED)
@api_view(['GET','POST'])
def categories(request):
    if request.method == 'GET':
        categories = category.objects.all()
        serializedCategories = categorySerializer(categories,many=True)
        return Response(serializedCategories.data,status=status.HTTP_200_OK)
                

# Create your views here.
