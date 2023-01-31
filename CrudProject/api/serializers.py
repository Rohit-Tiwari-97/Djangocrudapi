from rest_framework import serializers
from api import models

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ApiModel
        fields = '__all__'
        #fields = ('category', 'subcategeory', 'name', 'amount')
