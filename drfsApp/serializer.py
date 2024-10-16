from rest_framework import serializers
from .models import *

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'
class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'
class createProductSerialiser(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    quantity = serializers.IntegerField()
    category = serializers.IntegerField()
class creatProductListSerialiser(serializers.Serializer):
    products = createProductSerialiser(many = True)