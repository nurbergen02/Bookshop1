from django.shortcuts import render
from django.shortcuts import render
from django.db.models.base import Model
from django.shortcuts import render
from .models import Book, ProductReview
from .serializers import ProductListSerializer, ProductDetailSerializer, ProductCreateSerializer, \
    ProductReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, \
    UpdateAPIView, DestroyAPIView, CreateAPIView

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework import filters as rest_filters
from rest_framework import permissions


class ProductReviewViewset(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        """
        Передаем request в сериализаторы чтобы оттуда получить юзера
        """
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        """
        Добавляем в наши аргументы  те данные которые мы возращаем в get_serializer_context
        """
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)


class ProductViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    filter_backends = [
        filters.DjangoFilterBackend,
        rest_filters.SearchFilter,
    ]
    filterset_fields = ['price', 'title']
    search_fields = ['title', 'id', 'description']
    # permission_classes = [permissions.IsAdminUser]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return []

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'delete':
            return ProductListSerializer
        elif self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductCreateSerializer

    @action(['GET'], detail=True)
    def reviews(self, request, pk=None):
        product = self.get_object()
        # reviews = ProductReview.objects.filter(product=product)
        reviews = product.reviews.all()
        serializer = ProductReviewSerializer(
            reviews, many=True
        ).data
        return Response(serializer, status=200)


# class ProductListView:
#     pass