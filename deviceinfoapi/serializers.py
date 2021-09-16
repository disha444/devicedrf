from rest_framework import serializers
from .models import Devicinfo


class devserializer(serializers.ModelSerializer):
   class Meta:
       model = Devicinfo
       fields = ["device_price"]