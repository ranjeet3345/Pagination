
from django.shortcuts import render
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework.generics import ListAPIView
from .mypagination import myPageNumberPagination
from django.db.models import Q

class CustomerList(ListAPIView):
    serializer_class = CustomerSerializer
    pagination_class = myPageNumberPagination

    def get_queryset(self):
        queryset = Customer.objects.all()

        # Search
        search_query = self.request.query_params.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(cname__icontains=search_query) | Q(cemail__icontains=search_query)
            )

        # Sort
        sort_by = self.request.query_params.get('sort_by')
        allowed_sort_fields = ['cname', 'cemail', '-cname', '-cemail']
        if sort_by in allowed_sort_fields:
            queryset = queryset.order_by(sort_by)

        return queryset

    