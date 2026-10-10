from rest_framework import generics
from django.db.models import Avg, Count

from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.annotate(
        products_count=Count("products")
    )
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.annotate(
        products_count=Count("products")
    )
    serializer_class = CategorySerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ProductReviewsAPIView(generics.ListAPIView):
    queryset = Product.objects.prefetch_related("reviews").annotate(
        rating=Avg("reviews__stars")
    )
    serializer_class = ProductSerializer