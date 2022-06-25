from rest_framework import serializers
from manage_customer.models import Customer
 
class CustomerSerializer(serializers):
    class Meta:
        model = Customer
        fields = '__all__'