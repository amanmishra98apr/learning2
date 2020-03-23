from rest_framework import serializers
from .models import FirstTable

class FirstTableSerializer(serializers.ModelSerializer):
    class Meta:
        model=FirstTable
        fields=('id','name','branch','address','marks')
