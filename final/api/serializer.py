from rest_framework import serializers 
from .models import Product , ProductImage

'''
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'        
'''        
class ProductSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.URLField())
    
    class Meta:
        model = Product
        #fields = ['id', 'name', 'description', 'price', 'images']
        fields = '__all__'

    def create(self, validated_data):
        product = Product.objects.create(**validated_data)

        for image_url in images_data:
            # Fetch or create ProductImage instance based on the URL
            product_image, created = ProductImage.objects.get_or_create(image_url=image_url)
            product.images.add(product_image)

        return product
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'