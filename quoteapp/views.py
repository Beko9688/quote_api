from .models import Quotes, Category
from .serializers import QuoteSerializer, CategorySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class PaginationClass(PageNumberPagination):
    page_size = 4
    page_query_param = 'page_size'
    max_page_size = 10


class APIViewQuotes(ListCreateAPIView):
    queryset = Quotes.objects.all()
    serializer_class = QuoteSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    pagination_class = PaginationClass


class APIQuoteDetail(RetrieveUpdateDestroyAPIView):
    queryset = Quotes.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class APIViewCategory(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
