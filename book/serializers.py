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
    book_title = serializers.SerializerMethodField("get_book_title")

    class Meta:
        model = BookReview
        fields = "__all__"

    def get_book_title(self, book_review):
        title = book_review.book.title
        return title

    def validate_book(self, book):
        if self.Meta.model.objects.filter(book=book).exists():
            raise serializers.ValidationError("Вы уже оставляли отзыв на данный продукт")
        return book

    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise serializers.ValidationError(
                "Рейтинг должен быть от 1 до 5"
            )
        return rating

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if request == None:
            pass
        elif not request.user.is_anonymous:
            representation['author'] = request.user.name
        return representation


class BookLikesSerializer(serializers.ModelSerializer):
    book_title = serializers.SerializerMethodField("get_book_title")

    def get_book_title(self, book_likes):
        title = book_likes.book.title
        return title

    class Meta:
        model = BookLike
        fields = "__all__"

    def validate_product(self, book):
        if self.Meta.model.objects.filter(book=book).exists() == True:
            raise serializers.ValidationError("Вы уже лайкали данный продукт")
        return book

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if request == None:
            pass
        elif not request.user.is_anonymous:
            representation['author'] = request.user.name
        return representation
