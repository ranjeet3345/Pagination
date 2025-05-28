from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.Serializer):
    class Meta:
        model=Customer
        fields=['id','cname','cid']