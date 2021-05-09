from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('', customer_signup, name="signup"),
                  # path('login', customer_login, name="login"),
                  # path('logout', customer_logout, name="logout"),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
