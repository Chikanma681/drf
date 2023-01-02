from rest_framework import serializers
from .models import MenuItem
from .models import Category
from decimal import Decimal

# Relationship Serializers
class CategorySerialziers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','slug','title']

#Model Serializers
class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory') #use a different name from the model
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category = serializers.StringRelatedField()

    class Meta:
        model = MenuItem
        fields = ['id', 'title','stock', 'price_after_tax','category']

    def calculate_tax(self, product:MenuItem):
        return product.price+Decimal(1.1)

# class MenuItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         id = serializers.IntegerField()
#         title = serializers.CharField(max_length=255)

