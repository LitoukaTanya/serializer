from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product, Comment, Rating
from product.serializers import ProductSerializer, CommentSerializer, RatingSerializer, ProductDetailSerializer


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class ProductDetailView(APIView):

    def post(self, request):
        serializer = ProductDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.get_rating_and_comment()
            print(data)
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)