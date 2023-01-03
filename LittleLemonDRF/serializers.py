from rest_framework import serializers
from .models import MenuItem
from .models import Category
from decimal import Decimal

# # Relationship Serializers
# class CategorySerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id','slug','title']

# #Model Serializers
# class MenuItemSerializer(serializers.ModelSerializer):
#     # stock = serializers.IntegerField(source='inventory') #use a different name from the model
#     # price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
#     # category = serializers.StringRelatedField()

#     category = CategorySerializers(source=Category, read_only=True)
#     class Meta:
#         model = MenuItem
#         fields = ['id', 'title','inventory','category']

#     # def calculate_tax(self, product:MenuItem):
#     #     return product.price

# # class MenuItemSerializer(serializers.ModelSerializer):
# #     class Meta:
#         id = serializers.IntegerField()
#         title = serializers.CharField(max_length=255)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']

class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title','inventory','price','category','category_id']
    
    # def create(self, validated_data,**kwargs):
    #     # category_data = validated_data.pop('category')
    #     # category, created = Category.objects.get_or_create(**category_data)
    #     # validated_data['category'] = category
    #     # return MenuItem.objects.create(**validated_data)

    #     category_data = Category.objects.get(pk=validated_data['category'])
    #     category = Category.objects.create(
    #         title
    #     )