from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers

@api_view(['GET'])
def vegetables_ingredients(request):
    if request.method == 'GET':
        vegetables_ingredients = models.VegetablesIngridients.objects.all()
        serializer = serializers.VegetablesSerializers(vegetables_ingredients, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def meat_ingredients(request):
    if request.method == 'GET':
        meat_ingredients = models.MeatIngridients.objects.all()
        serializer = serializers.MeatSerializers(meat_ingredients, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def other_ingredients(request):
    if request.method == 'GET':
        other_ingredients = models.OtherIngridients.objects.all()
        serializer = serializers.OtherSerializers(other_ingredients, many=True)
        return Response(serializer.data)


