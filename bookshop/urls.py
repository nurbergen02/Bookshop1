"""bookshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from product.views import ProductReviewViewset, ProductViewset

router = DefaultRouter()
router.register('reviews', ProductReviewViewset)
router.register('products', ProductViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('account.urls')),
    # path('cart/', include('cart.urls')),
    # path('', include('product.urls')),


    # url(r'^admin/', admin.site.urls),
    # # url(r'^cart/', include('cart.urls', namespace='cart')),
    # url(r'^', include('shop.urls', namespace='shop')),
]
# path('api/v1/', include('order.urls'))
# path('api/v1/', include('product.urls')),
# path('api/v1/', include('order.urls'))
# 127.0.0.1:8000/api/v1/products/,
# path('cart/', include('cart.urls', namespace='cart')),
# path('', include('bookshop.urls', namespace='bookshop')),
