from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
                  path('', customer_dashboard, name="dashboard"),
                  path('product_detail', product_detail, name="product_detail"),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
