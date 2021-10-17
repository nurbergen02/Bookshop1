from rest_framework import serializers
from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=200)
    product_price = serializers.FloatField()
    product_quantity = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = CartItem
        fields = ('__all__')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["total_sum"] = instance.product_price * instance.product_quantity
        print(representation)
        return representation