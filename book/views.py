from .serializers import *
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
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
    filterset_fields = ['price', 'title']
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

    @action(['GET'], detail=True)
    def refuse(self, request, pk=None):
        book = self.get_object()
        reviews = book.reviews.all()
        serializer1 = BookReviewSerializer(
            reviews, many=True
        ).data
        likes = book.likes.all()
        serializer2 = BookLikesSerializer(
            likes, many=True
        ).data
        return Response(serializer1, serializer2, status=200)
