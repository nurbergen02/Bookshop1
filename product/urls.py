
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
import product
from product import views
from product.views import ProductReviewViewset, ProductViewset

router = DefaultRouter()
router.register('reviews', ProductReviewViewset)
router.register('products', ProductViewset)

urlpatterns = [
    path('products/', product.views.ProductReviewViewset),
    path('products/<int:pk>/', views.ProductViewset),
    # path('admin/', include(admin.site.urls)),
    # path('cart/', include('cart.urls', namespace='cart')),
    # path('', include('shop.urls', namespace='shop')),
]

# urlpatterns = [
#    path('products/', product.views.ProductListView.as_view()),
#    path('products/<int:pk>/', views.ProductDetailView.as_view()),
#    path('products/<int:pk>/update/', views.ProductUpdateView.as_view()),
#    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view()),
#    path('products/create/', views.ProductCreateView.as_view()),
#    path('products/', views.ProductListView),
# ]
