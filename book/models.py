from django.db import models
from django.contrib.auth import get_user_model
from model_utils import Choices
from model_utils.fields import StatusField

User = get_user_model()


class CreatedatModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True


class Book(CreatedatModel):
    STATUS = Choices("Available", "Not existed")
    title = models.CharField(max_length=50, unique=True)
    book_author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='book_cover', null=True, blank=True)
    genre = models.CharField(max_length=50, null=True)
    status = StatusField()
    description = models.TextField()

    class Meta:
        ordering = ['title', 'price']

    def __str__(self):
        return self.title


class BookReview(CreatedatModel):
    username = models.ForeignKey(
        'account.User', on_delete=models.CASCADE,
        related_name='reviews'
    )
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField()
    rating = models.PositiveIntegerField(default=1)


class BookLike(CreatedatModel):
    username = models.ForeignKey(
        'account.User', on_delete=models.CASCADE,
        related_name='likes'
    )
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="likes"
    )


class BookCart(CreatedatModel):
    username = models.ForeignKey(
        'account.User', on_delete=models.CASCADE,
        related_name='cart'
    )
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="cart"
    )