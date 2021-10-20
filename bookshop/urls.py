from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from book.views import *

router = DefaultRouter()
router.register('reviews', BookReviewViewset)
router.register('books', BookViewset)
router.register('likes', BookLikesViewset)
router.register('cart', BookCartViewSet, basename='Book')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('account.urls'))
    ]
