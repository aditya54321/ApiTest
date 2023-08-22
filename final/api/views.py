from django.shortcuts import render
import json
import requests
from django.http import JsonResponse
from django.core.files import File
from io import BytesIO
from .models import Product
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProductSerializer

class ImportDataView(APIView):
    
    '''
    def get(self, request):
        url = "https://dummyjson.com/products" 
        response = requests.get(url)
        data = response.json()

        for product_data in data:
            #images_data = product_data.pop("images", []) 
            product_serializer = ProductSerializer(data=product_data)
            if product_serializer.is_valid():
                product = product_serializer.save()

                for image_url in images_data:
                    image_data = {"product": product.id, "image_url": image_url}
                    image_serializer = ProductImageSerializer(data=image_data)
                    if image_serializer.is_valid():
                        image_serializer.save()
        return JsonResponse(product)
        #return Response({"message": "Products imported successfully"})

    
    '''
    def get(self, request):
        response = requests.get('https://dummyjson.com/products') 
        data = json.loads(response.content)

        products = data['products']
        for product_data in products:
            product_id = product_data['id']

            serializer = ProductSerializer(data=product_data)
            if serializer.is_valid():
                try:
                    product = Product.objects.get(id=product_id)
                    serializer.update(product, serializer.validated_data)
                except Product.DoesNotExist:
                    serializer.save()

                # Process and save images
                product = Product.objects.get(id=product_id)
                images = product_data.get('images', [])
                product.images.clear()  # Clear existing images
                for image_url in images:
                    product.images.create(image_url=image_url)

            else:
                return Response({'error': serializer.errors}, status=400)

        return Response({'message': 'Data imported successfully'}, status=200)
        
        
