from rest_framework import serializers
from .models import *


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ('description', 'image', 'created_at')


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def to_representation(self, instance):
        representation = super(
            BookDetailSerializer, self).to_representation(instance)
        representation['reviews'] = BookReviewSerializer(
            BookReview.objects.filter(book=instance.id), many=True
        ).data
        representation['total_likes'] = BookLike.objects.filter(
            book=instance.id).count()
        return representation


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta(BookDetailSerializer.Meta):
        pass

    def validate_price(self, price):
        if price < 100:
            raise serializers.ValidationError("Цена не может быть меньше ста")
        return price


class BookReviewSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.name')
    book_title = serializers.SerializerMethodField("get_book_title")

    class Meta:
        model = BookReview
        fields = "__all__"

    def get_book_title(self, book_review):
        title = book_review.book.title
        return title

    def validate_book(self, book):
        if self.Meta.model.objects.filter(book=book).exists():
            raise serializers.ValidationError("Вы уже оставляли отзыв на данную книгу")
        return book

    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise serializers.ValidationError(
                "Рейтинг должен быть от 1 до 5"
            )
        return rating

    def create(self, validated_data):
        request = self.context.get('request')
        review = BookReview.objects.create(
            username=request.user,
            **validated_data
        )
        return review


class BookLikesSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.name')
    book_title = serializers.SerializerMethodField("get_book_title")

    def get_book_title(self, book_likes):
        title = book_likes.book.title
        return title

    class Meta:
        model = BookLike
        fields = "__all__"

    def validate_book(self, book):
        if self.Meta.model.objects.filter(book=book).exists():
            raise serializers.ValidationError("Вы уже лайкали данную книгу")
        return book

    def create(self, validated_data):
        request = self.context.get('request')
        like = BookLike.objects.create(
            username=request.user,
            **validated_data
        )
        return like


class BookCartSerializer(serializers.ModelSerializer):
    book_title = serializers.SerializerMethodField("get_book_title")
    username = serializers.ReadOnlyField(source='username.name')

    def get_book_title(self, book_cart):
        title = book_cart.book.title
        return title

    class Meta:
        model = BookCart
        fields = "__all__"

    def create(self, validated_data):
        request = self.context.get('request')
        cart = BookCart.objects.create(
            username=request.user,
            **validated_data
        )
        return cart
