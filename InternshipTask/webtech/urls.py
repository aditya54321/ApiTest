
from django.urls import path, include
from webtech import views

urlpatterns = [
    
    path("", views.index, name="index"),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('product/<int:product_id>/update/', views.update_product, name='update_product'),
    path('product/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('add-product/', views.add_product, name='add_product'),
]
