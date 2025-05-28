from django.shortcuts import render
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework.generics import ListAPIView

class CustomerList(ListAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
