from rest_framework import serializers
from .models import *

class VegetablesSerializers(serializers.ModelSerializer):
    class Meta:
        model = VegetablesIngridients
        fields = ['vegetables_ingredient',]

class MeatSerializers(serializers.ModelSerializer):
    class Meta:
        model = MeatIngridients
        fields = ['meat_ingredient',]

class OtherSerializers(serializers.ModelSerializer):
    class Meta:
        model = OtherIngridients
        fields = ['other_ingredient',]