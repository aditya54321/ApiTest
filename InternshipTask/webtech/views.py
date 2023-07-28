from django.shortcuts import render, redirect ,get_object_or_404
import requests
import templates
from .models import Product
from .forms import ProductForm
from django.http import JsonResponse
import json
# Create your views here.

def base(request):
    return render(request, 'base.html')

def index(request):
    url = 'https://dummyjson.com/products'
    response = requests.get(url)
    data = response.json()

    context = {
        'products': data['products']
    }

    return render(request, "index.html", context)




def product_details(request, product_id):
    url = f'https://dummyjson.com/products/{product_id}'
    response = requests.get(url)
    data = response.json()
    product = None

    if 'products' in data:
        products = data['products']
        for p in products:
            if p['id'] == int(product_id):
                product = p
                break

    context = {
        'product': product
    }
    return render(request, 'product_details.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index.html")
        else:
            form = Productform()
    context = {
        'form': form
    }
    return render(request, "add_product.html", context)


def update_product(request, product_id):
    if request.method == 'POST':
        updated_product_data = json.loads(request.body)
        
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
        
        product.title = updated_product_data.get('title', product.title)
        product.description = updated_product_data.get('description', product.description)
        product.price = updated_product_data.get('price', product.price)
        product.discountPercentage = updated_product_data.get('discountPercentage', product.discountPercentage)
        product.rating = updated_product_data.get('rating', product.rating)
        product.stock = updated_product_data.get('stock', product.stock)
        product.brand = updated_product_data.get('brand', product.brand)
        product.category = updated_product_data.get('category', product.category)
        product.thumbnail = updated_product_data.get('thumbnail', product.thumbnail)
        product.images = updated_product_data.get('images', product.images)
    
        product.save()
        
        return JsonResponse({'message': 'Product updated successfully'})
    
    elif request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
        
        context = {
            'product': product
        }
        return render(request, 'update_product.html', context)



def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect("index.html")

    context = {
        'product': product
    }
    return render(request, 'delete_product.html', context)
