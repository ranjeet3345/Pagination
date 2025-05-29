# from django.shortcuts import render
# from .serializers import CustomerSerializer
# from .models import Customer
# from rest_framework.generics import ListAPIView
# from .mypagination import myPageNumberPagination
# from rest_framework import filters

# class CustomerList(ListAPIView):
#     queryset=Customer.objects.all()
#     serializer_class=CustomerSerializer
#     pagination_class=myPageNumberPagination

from django.shortcuts import render
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework.generics import ListAPIView
from .mypagination import myPageNumberPagination

class CustomerList(ListAPIView):
    serializer_class = CustomerSerializer
    print(serializer_class)
    print("data=----")
    serializer = CustomerSerializer(Customer.objects.first())
    print(serializer.data)
    pagination_class = myPageNumberPagination
    print(myPageNumberPagination)
    def get_queryset(self):
        queryset = Customer.objects.all()
        print("queryset---started------")
        print(queryset)
        print("queryset--ended--")
        sort_by = self.request.query_params.get('sort_by')
        print("sorted by --")
        print(sort_by)

        # Allow sorting only on safe fields
        allowed_sort_fields = ['cname', 'cemail', '-cname', '-cemail']
        if sort_by in allowed_sort_fields:
            queryset = queryset.order_by(sort_by)
        
        print("sorted---queryset------")
        print(queryset)
        return queryset

    