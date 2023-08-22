
from django.contrib import admin
from django.urls import path
from api.views import ImportDataView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ImportDataView.as_view()),
    #path('product-list/', ImportDataView.product_list,name='product-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
