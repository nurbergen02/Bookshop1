from django.db import models
from django.contrib.auth import get_user_model
from model_utils import Choices
from model_utils.fields import StatusField
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
# from likes.models import Like

User = get_user_model()


# class Product(models.Model):
#     body = models.CharField(max_length=140)
#     likes = GenericRelation(Like)

    # def __str__(self):
    #     return self.body
    #
    # @property
    # def total_likes(self):
    #     return self.like.count()


class CreatedatModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    """Создание абстрактной модели для добавления поля созданием продукта. Нужен для сокращение кода и расширяемости """

    class Meta:
        abstract = True


# class Author(models.Model):
#     name = models.CharField(max_length=55)
#     last_name = models.CharField(max_length=85, blank=True)
#     image = models.ImageField(blank=True, null=True, upload_to='authors')
#     date_of_birth = models.DateField()
#     parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.name}, {self.last_name}'


# class Genre(models.Model):
#     slug = models.SlugField(max_length=55, primary_key=True)
#     name = models.CharField(max_length=55)
#
#     def __str__(self):
#         return f'{self.name}'


class Book(CreatedatModel):
    STATUS = Choices(
        ('in stock', 'В наличии'),
        ('out of stock', 'Нет в наличии')
    )
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='books', null=True, blank=True)
    genre = models.CharField(max_length=50, null=True)

    status = StatusField()
    description = models.TextField()

    # products = models.Manager()

    class Meta:
        ordering = ['title', 'price']

    def __str__(self):
        return self.title


class ProductReview(CreatedatModel):
    product = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', null=True)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(default=1)

# review = ProductReview(product='Editor post', author='Zaid', text='Bad', rating=1)
# review.product.title, review.product.price
# product = Product('title'='New', 'price'=100, 'description'='Nothing to say', status="Available",image=Null)
# product.reviews.text


# STATUS = Choices(
#     ('Чингиз Айтматов'),
#     ('Джоан Кэтлин Роулинг'),
#     ('Пауло Коэльо'),
#     ('Халед Хоссейни'),
#     ('Эрика Леонард'),
# )


# STATUS = Choices(
#     ('роман'),
#     ('фантастика'),
#     ('приключения'),
# )
