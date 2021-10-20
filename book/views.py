from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .serializers import *
from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters
from rest_framework import filters as rest_filters


class BookReviewViewset(viewsets.ModelViewSet):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        return {
            "request": self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)


class BookLikesViewset(viewsets.ModelViewSet):
    queryset = BookLike.objects.all()
    serializer_class = BookLikesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        return {
            "request": self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    filter_backends = [
        filters.DjangoFilterBackend,
        rest_filters.SearchFilter
    ]
    filterset_fields = ['price', 'title', 'status']
    search_fields = ['title', 'description']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'delete':
            return BookListSerializer
        elif self.action == 'retrieve':
            return BookDetailSerializer
        return BookCreateSerializer


class BookCartViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return BookCart.objects.filter(username=self.request.user)
    serializer_class = BookCartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        return {
            "request": self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)
