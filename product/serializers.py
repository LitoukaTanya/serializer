from django.db.models import Avg

from .models import Product, Comment, Rating
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'product', 'content')


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('id', 'score', 'product')


class ProductDetailSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()

    def validate_product_id(self, value):
        if not Product.objects.filter(id=value).exists():
            raise serializers.ValidationError("Product with this ID does not exist.")
        return value

    def get_rating_and_comment(self):
        product_id = self.validated_data["product_id"]
        product = Product.objects.get(id=product_id)
        rating = Rating.objects.filter(product=product)
        comment = Comment.objects.filter(product=product)
        average_rating = rating.aggregate(Avg('score'))

        return {
            'product': ProductSerializer(product).data,
            'average_rating': average_rating['score__avg'],
            'comment': CommentSerializer(comment, many=True).data
        }



