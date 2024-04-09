from rest_framework import serializers
from .models import Product

#using a serializer to convert my data to type i want 
class ListSerializers(serializers.ModelSerializer):
 class Meta:
  model = Product
  fields = '__all__'